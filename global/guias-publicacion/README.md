# Guías de publicación (`global/guias-publicacion/`)

Referencia para **maquetar y entregar** un manuscrito: fuente e interlineado, columnas, archivos de entrega, secciones/capítulos y referencias. No confundir con metodología SLR ([`global/bibliography/`](../bibliography/bibliography.md)).

## Qué va en cada subcarpeta

| Carpeta | Tipo de documento | ¿Dice fuente / márgenes / columnas? |
|---------|-------------------|-------------------------------------|
| [`revistas/`](revistas/) | **Guide for authors** de una revista concreta | Parcial: entrega (.docx/.tex), **1 vs 2 columnas**, secciones numeradas, abstract, referencias. La tipografía final (Times, etc.) la suele aplicar el editor **después** de aceptar. |
| [`institucional/`](institucional/) | Normas de **universidad** (tesis / artículo para titulación) | **Sí:** Arial, tamaños, márgenes, capítulos, APA, IMRyD. |
| [`plantillas-latex/`](plantillas-latex/) | Manuales de clases **LaTeX** (elsarticle, acmart, IEEEtran) | Solo si envías `.tex`: opciones de columnas en plantilla. **No** sustituyen la guía de la revista. |

## Revistas (`revistas/`)

### `elsevier-ist-guide-for-authors.pdf` (+ `elsevier-ist-guide-for-authors.source.md`)

**Revista:** *Information and Software Technology* (Elsevier) — canal habitual para SLR en ingeniería de software.

**Lo que sí fija esta guía (ejemplos):**

- **Entrega:** Word `.doc/.docx` o LaTeX `.tex` editable; **no** PDF como fuente.
- **Columnas:** Word en **una columna**; doble columna solo en LaTeX.
- **Extensión:** paper ~15 000 palabras; **revisión sistemática / mapping ~20 000** (referencias y anexos cuentan; figuras/tablas ~200 palabras c/u).
- **Abstract:** obligatorio **estructurado** (Context, Objectives, Methods, Results, Conclusion), máx. 300 palabras.
- **Cuerpo:** secciones **numeradas** (1, 1.1, 1.1.1…), apartados tipo Acknowledgements, CRediT, referencias numeradas `[1]` en orden de aparición.
- **Fuente tipográfica concreta (Times 12, etc.):** en Elsevier **no** suele exigirse al autor en el envío; se normaliza en pruebas de galera.

Fuente oficial (HTML, revisar antes de enviar):  
[Guide for authors — IST](https://www.sciencedirect.com/journal/information-and-software-technology/publish/guide-for-authors)

El PDF del repo es copia de trabajo (2026-11-04) generada desde ese HTML.

### Otras revistas (solo enlace; capturar igual que IST si hace falta)

| Revista | Guide for authors |
|---------|-------------------|
| *Empirical Software Engineering* (Springer) | [How to publish](https://link.springer.com/journal/10664/how-to-publish-with-us) |
| *IEEE Trans. Software Engineering* | [About / authors](https://www.computer.org/csdl/trans/tse/about/787502) |
| *ACM Computing Surveys* | [ACM journal authors](https://authors.acm.org/journal-publication) |

## Institucional (`institucional/`) — fuente, márgenes y capítulos explícitos

### UTP — `utp-guia-egresado-pregrado-v14-2026.pdf`

**Anexo 3** (p. ~51 en adelante): formato del trabajo de investigación.

- **Tesis en formato artículo científico:** el **cuerpo del artículo** debe seguir la **guía para autores o plantilla de la revista** elegida (Scopus/WoS); la UTP envuelve con carátula, similitud Turnitin, nombre de la revista, etc.
- **Formato general UTP (tesis regular / partes institucionales):** hoja A4, **Arial 11**, interlineado **1,5** (en otras secciones del anexo también **Arial 12**, doble espacio, márgenes 3 / 2,5 cm); estructura por capítulos (CAPÍTULO 1…), resumen, bibliografía.

PDF oficial: [Guía del egresado V14](https://www.utp.edu.pe/web/sites/default/files/2026-05/Guia_del_egresado_Pregrado_V14_PT.pdf)

### Universidad de Lima — `ulima-de-la-rocha-rodriguez-guia-publicar-documentos-academicos-2016.pdf`

Tipos de documento (tesis, informe, **artículo científico**), **IMRyD**, partes del artículo, **APA** para referencias; anexo de formato de tesis. No sustituye la guía de la revista destino si publicas fuera.

[Repositorio ULima](https://hdl.handle.net/20.500.12724/3828)

## Plantillas LaTeX (`plantillas-latex/`)

| Archivo | Uso |
|---------|-----|
| `elsevier-elsarticle-elsdoc.pdf` | Clase `elsarticle` (revistas Elsevier). |
| `acm-acmart-author-guide.pdf` | Clase `acmart` (ACM). |
| `ieee-ieee-tran-howto.pdf` | Clase `IEEEtran` (IEEE). |

Consultar solo cuando la **Guide for authors** de la revista pida envío en LaTeX.
