import { createServerFn } from '@tanstack/react-start'
import fs from 'node:fs'
import path from 'node:path'

import { THEME_SLUG } from '../constants/theme'
import {
  repoRootFromPrismaFlowCwd,
  resolveLatestPrismaRelPath,
} from '../lib/resolve-latest-prisma'

export type ThemePrismaPayload = {
  data: Record<string, unknown>
  relPath: string
}

export const getThemePrismaData = createServerFn({ method: 'GET' })
  .inputValidator((slug: string) => slug)
  .handler(async ({ data: themeSlug }): Promise<ThemePrismaPayload | null> => {
    try {
      const repoRoot = repoRootFromPrismaFlowCwd()
      const rel = resolveLatestPrismaRelPath(repoRoot, themeSlug)
      if (!rel) return null
      const full = path.join(repoRoot, rel)
      const data = JSON.parse(fs.readFileSync(full, 'utf-8')) as Record<
        string,
        unknown
      >
      return { data, relPath: rel }
    } catch (e) {
      console.error('Error loading theme prisma.json:', e)
      return null
    }
  })

/** @deprecated Usa getThemePrismaData; mantiene compatibilidad con el slug por defecto. */
export const getLatestPrismaData = createServerFn({ method: 'GET' }).handler(
  async () => {
    const result = await getThemePrismaData({ data: THEME_SLUG })
    return result?.data ?? null
  },
)
