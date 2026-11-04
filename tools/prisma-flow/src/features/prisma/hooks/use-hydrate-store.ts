import { useEffect } from 'react'
import { toast } from 'sonner'

import { THEME_SLUG } from '../constants/theme'
import { getPrismaFromPath } from '../server/get-prisma-from-path'
import { getThemePrismaData } from '../server/get-latest-prisma'
import { usePrismaStore } from '../store/use-prisma-store'

/**
 * Hidrata el diagrama desde `prisma.json`.
 * Por defecto: última carpeta `picoc/<fecha>-<MARCO>/` del tema (no por mtime).
 * Si se pasa `prismaRelPath`, esa ruta fija tiene prioridad (depuración).
 */
export function useHydrateStore(
  themeSlug: string = THEME_SLUG,
  prismaRelPath?: string,
) {
  const loadFromJson = usePrismaStore((state) => state.loadFromJson)
  const setSourceRelPath = usePrismaStore((state) => state.setSourceRelPath)

  useEffect(() => {
    void usePrismaStore.persist.rehydrate()

    const apply = (data: Record<string, unknown>, relPath: string) => {
      loadFromJson(data)
      setSourceRelPath(relPath)
      toast.success(`PRISMA cargado desde ${relPath}`)
    }

    const load = prismaRelPath
      ? getPrismaFromPath({ data: prismaRelPath }).then((data) =>
          data ? { data, relPath: prismaRelPath } : null,
        )
      : getThemePrismaData({ data: themeSlug })

    void load
      .then((result) => {
        if (result) apply(result.data, result.relPath)
      })
      .catch(console.error)
  }, [loadFromJson, prismaRelPath, setSourceRelPath, themeSlug])
}
