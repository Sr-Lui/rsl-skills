import fs from 'node:fs'
import path from 'node:path'

/** Misma convención que `scripts/picoc_versions.py` (PICOC_DIR_RE). */
const PICOC_DIR_RE = /^(\d{4}-\d{2}-\d{2})(?:-([2-9]|[1-9]\d+))?-([A-Za-z]+)$/

export function repoRootFromPrismaFlowCwd(cwd = process.cwd()): string {
  return path.resolve(cwd, '../..')
}

/**
 * Ruta relativa al root del repo del `prisma.json` más reciente en `docs/<slug>/picoc/`.
 * Orden: fecha ISO, luego número de versión del mismo día (…-3-PIO).
 */
export function resolveLatestPrismaRelPath(
  repoRoot: string,
  themeSlug: string,
): string | null {
  const picocDir = path.join(repoRoot, 'docs', themeSlug, 'picoc')
  if (!fs.existsSync(picocDir)) return null

  type Row = { date: string; n: number; folder: string }
  const rows: Row[] = []

  for (const name of fs.readdirSync(picocDir)) {
    const m = PICOC_DIR_RE.exec(name)
    if (!m) continue
    const prismaFile = path.join(picocDir, name, 'prisma.json')
    if (!fs.existsSync(prismaFile)) continue
    rows.push({
      date: m[1],
      n: m[2] ? Number.parseInt(m[2], 10) : 1,
      folder: name,
    })
  }

  if (rows.length === 0) return null
  rows.sort((a, b) => a.date.localeCompare(b.date) || a.n - b.n)
  const latest = rows.at(-1)!
  return path.join('docs', themeSlug, 'picoc', latest.folder, 'prisma.json')
}
