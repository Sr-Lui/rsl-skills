#!/usr/bin/env node
// Expone .cursor/skills, .agents/skills y .cursor/agents en .claude/ mediante symlinks relativos.
// Uso: node scripts/claude-sync.mjs [--check] [--copy]
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = new Set(process.argv.slice(2));
const CHECK = args.has("--check");
const COPY = args.has("--copy");

const errors = [];
const log = [];

const skillSources = [".cursor/skills", ".agents/skills"];
const agentSource = ".cursor/agents";

function rel(p) {
  return path.relative(ROOT, p);
}

function linkEntry(targetAbs, linkAbs) {
  const relTarget = path.relative(path.dirname(linkAbs), targetAbs);
  let st = null;
  try {
    st = fs.lstatSync(linkAbs);
  } catch {}
  if (st) {
    if (st.isSymbolicLink()) {
      if (fs.readlinkSync(linkAbs) === relTarget && fs.existsSync(linkAbs)) return "ok";
      if (CHECK) return "stale";
      fs.unlinkSync(linkAbs);
    } else {
      return "real"; // entrada real (p. ej. openspec-*): se respeta
    }
  } else if (CHECK) {
    return "missing";
  }
  fs.mkdirSync(path.dirname(linkAbs), { recursive: true });
  if (COPY) fs.cpSync(targetAbs, linkAbs, { recursive: true });
  else fs.symlinkSync(relTarget, linkAbs);
  return "linked";
}

// 1) skills
for (const src of skillSources) {
  const dir = path.join(ROOT, src);
  if (!fs.existsSync(dir)) continue;
  for (const name of fs.readdirSync(dir)) {
    const abs = path.join(dir, name);
    if (!fs.existsSync(path.join(abs, "SKILL.md"))) continue;
    const r = linkEntry(abs, path.join(ROOT, ".claude/skills", name));
    log.push(`skill ${name}: ${r}`);
    if (r === "missing" || r === "stale") errors.push(`skill ${name} ${r} (ejecuta pnpm claude:sync)`);
  }
}

// 2) agentes (+ frontmatter)
const agDir = path.join(ROOT, agentSource);
if (fs.existsSync(agDir)) {
  for (const f of fs.readdirSync(agDir).filter((x) => x.endsWith(".md"))) {
    const abs = path.join(agDir, f);
    const head = fs.readFileSync(abs, "utf8").split("\n").slice(0, 12).join("\n");
    if (!/^---\nname: .+/m.test(head) || !/description:/.test(head)) errors.push(`agente ${f}: frontmatter sin name/description`);
    const r = linkEntry(abs, path.join(ROOT, ".claude/agents", f));
    log.push(`agent ${f}: ${r}`);
    if (r === "missing" || r === "stale") errors.push(`agente ${f} ${r} (ejecuta pnpm claude:sync)`);
  }
}

// 3) rutas citadas existen (desde la raíz del repo)
const files = [];
for (const src of skillSources) {
  const dir = path.join(ROOT, src);
  if (!fs.existsSync(dir)) continue;
  for (const n of fs.readdirSync(dir)) {
    const p = path.join(dir, n, "SKILL.md");
    if (fs.existsSync(p)) files.push(p);
  }
}
if (fs.existsSync(agDir)) for (const f of fs.readdirSync(agDir)) if (f.endsWith(".md")) files.push(path.join(agDir, f));

const pathRe = /(?<![\w./-])((?:playbooks|scripts|global|\.agents\/skills|\.cursor\/skills)\/[A-Za-z0-9_./-]*[A-Za-z0-9_])/g;
for (const file of files) {
  if (rel(file).includes("openspec-") || rel(file).startsWith(".agents/")) continue; // terceros: rutas propias
  const lines = fs.readFileSync(file, "utf8").split("\n");
  lines.forEach((line, i) => {
    if (/(\.\.\/)+(playbooks|\.agents|scripts|global)\//.test(line)) errors.push(`${rel(file)}:${i + 1} ruta relativa (usa ruta desde la raíz)`);
    for (const m of line.matchAll(pathRe)) {
      const p = m[1].replace(/[.,;:)]+$/, "");
      if (/[<*{[]/.test(p) || /\$/.test(p)) continue;
      if (!fs.existsSync(path.join(ROOT, p))) errors.push(`${rel(file)}:${i + 1} no existe ${p}`);
    }
  });
}

if (!CHECK) for (const l of log) if (!l.endsWith("ok")) console.log(l);
if (errors.length) {
  console.error(errors.join("\n"));
  console.error(`FAIL: ${errors.length} problema(s)`);
  process.exit(1);
}
console.log(`OK: ${log.length} entradas sincronizadas${CHECK ? " (check)" : ""}.`);
