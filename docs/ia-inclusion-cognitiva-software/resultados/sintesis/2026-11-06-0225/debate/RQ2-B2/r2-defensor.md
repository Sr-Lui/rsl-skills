# RQ2-B2 — Ronda 2 — Defensor

Acepto las cuatro objeciones. Volví a correr `sintesis:aggregate RQ2-B2` después de la recodificación de RQ2-I1 (R453 pasa a NR) y con el `excluir` del operador. El cruce queda con base **40**, 7 filas × 5 columnas y `cruce.excluidas = {"RQ1-I1": ["Sin perfil específico"]}`. La matriz de la figura y de la spec es ahora la de la tabla tal cual. El orden de las filas cambia: el agregador pone primero la DI.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | Porcentajes sobre 42 | **Acepto** | Con base 40: DI × LLM 28% (n=11), TEA × LLM 23% (n=9), TDAH × LLM 20% (n=8) y 15% (n=6) para TEA × PLN y para la discapacidad cognitiva con LLM y con PLN |
| 2 | La apertura describe la base anterior | **Acepto** | «… sobre los 40 estudios cualitativos o mixtos que declaran un perfil específico y aplican una familia de IA; se excluye el estudio que no declara un perfil específico» |
| 3 | *Nota.*, Detalle gráfica y spec describen la tabla anterior | **Acepto** | Se borra la fila no dibujada. La *Nota.* y la nota del gráfico dan la base 40 y la exclusión. En la spec, `excluidas` copia `cruce.excluidas`, la matriz es la de la tabla y la escala va de 0 a 11 |
| 4 | R453 arrastra TEA × LLM y TEA × NLP | **Acepto.** Es la misma cascada que en RQ2-B1 | TEA × LLM = 9, TEA × NLP = 6 y base 40. Sigue siendo cierto que el TEA y la discapacidad cognitiva tienen al menos 2 estudios en las cinco familias (TEA: 9, 6, 4, 5, 2) |

## Texto propuesto

<!-- inicio -->
### 3.?. Perfiles neurodivergentes frente a familias de inteligencia artificial (RQ2)

El cruce entre el perfil declarado y la familia de técnica de IA se calculó sobre los 40 estudios cualitativos o mixtos que declaran un perfil específico y aplican una familia de IA; se excluye el estudio que no declara un perfil específico. Las frecuencias de cada perfil y de cada familia por separado se presentan en los apartados de perfiles y de familias de técnica. Como se observa en la Figura {{F1}}, la combinación más frecuente es la discapacidad intelectual (DI) con los LLM, en el 28% (n=11) de los estudios. Le siguen el trastorno del espectro autista (TEA) con los LLM, en el 23% (n=9), y el trastorno por déficit de atención con hiperactividad (TDAH) con los LLM, en el 20% (n=8). Con el 15% (n=6) aparecen el TEA con el procesamiento del lenguaje natural o del habla y la discapacidad cognitiva, como término genérico, tanto con los LLM como con el procesamiento del lenguaje natural.

La distribución es heterogénea entre perfiles. Los LLM son la familia más frecuente en la DI, el TEA, el TDAH y el síndrome de Down. En la dislexia, en cambio, el procesamiento del lenguaje natural o del habla se reporta en 5 estudios y los LLM en 1. En las dificultades de aprendizaje, el procesamiento del lenguaje natural (n=5) y los LLM (n=4) tienen frecuencias similares. El TEA y la discapacidad cognitiva son los únicos perfiles que aparecen en las cinco familias con al menos 2 estudios en cada una. El síndrome de Down solo se cruza con los LLM (n=2), y el aprendizaje profundo y la visión por computador no superan los 5 estudios en ningún perfil.

**Figura {{F1}}**

*Perfiles de discapacidad cognitiva o neurodivergencia según la familia de técnica de inteligencia artificial*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027). Base: 40 estudios cualitativos o mixtos con perfil específico y familia de IA; se excluye el estudio sin perfil específico. Un estudio puede declarar más de un perfil y aplicar más de una familia, por lo que un mismo estudio puede figurar en varias celdas.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** mapa de calor.
- **Por qué este tipo:** relación entre dos variables nominales multivalor (7 perfiles × 5 familias). El color resalta qué combinaciones se concentran y cuáles están vacías.
- **Qué muestra:** el número de estudios que combina cada perfil específico con cada familia de técnica de IA.
- **Datos a dibujar:** filas (perfil, en este orden): DI, TEA, discapacidad cognitiva, dificultades de aprendizaje, TDAH, dislexia y síndrome de Down. Columnas (familia, en este orden): LLM, PLN o habla, aprendizaje automático, aprendizaje profundo y visión por computador. Matriz:
  - DI: [11, 5, 2, 1, 4]
  - TEA: [9, 6, 4, 5, 2]
  - Discapacidad cognitiva: [6, 6, 2, 2, 2]
  - Dificultades de aprendizaje: [4, 5, 3, 1, 2]
  - TDAH: [8, 2, 3, 2, 1]
  - Dislexia: [1, 5, 3, 2, 1]
  - Síndrome de Down: [2, 0, 0, 0, 0]
- **Ejes:** en el eje X, la familia de técnica en el orden de la tabla (de mayor a menor frecuencia en el cruce); en el eje Y, el perfil, con la DI arriba. Escala de color lineal de 0 a 11.
- **Etiquetas sobre los datos:** el número de estudios en cada celda, incluidos los ceros.
- **Leyenda:** barra de color «Número de estudios coincidentes» (0–11).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «Un estudio puede figurar en varias celdas: puede declarar más de un perfil y aplicar más de una familia (base n = 40 estudios cualitativos o mixtos con perfil específico y familia de IA; se excluye el estudio sin perfil específico)».
- **Estilo:** escala secuencial de azules sobrios (blanco = 0), texto oscuro sobre celdas claras y blanco sobre las oscuras, 16 × 10 cm.
<!-- fin -->

## Decisiones

- **Sin recodificación propia.** El bloque hereda RQ1-I1 (cerrado) y RQ2-I1 (R2 de RQ2-B1). Lo reagregué después de esa recodificación.
- **Cifras.** Las celdas salen de `cruce.matriz` y la base de `cruce.base` = 40 (`tablas/RQ2-B2.json`). Los porcentajes de las celdas usan la base 40, redondeados al entero con el medio hacia arriba: 11/40 = 27,5 → 28%; 9/40 = 22,5 → 23%; 8/40 = 20%; 6/40 = 15%.
- **Spec** (`graficos/RQ2-B2.spec.json`): matriz, filas y columnas copiadas de la tabla; `excluidas` igual a `cruce.excluidas`; base 40 en `muestra` y `nota`.
