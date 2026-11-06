# RQ2-B2 — Ronda 1 — Defensor

Propongo un mapa de calor de 7 × 5: perfiles específicos (RQ1-I1 cerrado) frente a familias de IA (RQ2-I1 recodificado en RQ2-B1). La columna genérica «IA» desaparece con la recodificación de RQ2-I1, sin filtro. «Sin perfil específico» sí sigue en `tablas/RQ2-B2.json`, porque no edito RQ1-I1, así que la figura la excluye declarándolo en la spec (ver Decisiones).

## Texto propuesto

<!-- inicio -->
### 3.?. Perfiles neurodivergentes frente a familias de inteligencia artificial (RQ2)

El cruce entre el perfil declarado y la familia de técnica de IA se calculó sobre los 42 estudios cualitativos o mixtos con dato en ambos ítems; uno de ellos no declara un perfil específico y no se representa. Las frecuencias de cada perfil y de cada familia por separado se presentan en los apartados de perfiles y de familias de técnica. Como se observa en la Figura {{F1}}, la combinación más frecuente es la discapacidad intelectual con los LLM, en el 26% (n=11) de los estudios, seguida del trastorno del espectro autista (TEA) con los LLM, en el 24% (n=10), y del trastorno por déficit de atención con hiperactividad (TDAH) con los LLM, en el 19% (n=8). El TEA con el procesamiento del lenguaje natural o del habla aparece en el 17% (n=7), y la discapacidad cognitiva, como término genérico, se combina en el 14% (n=6) tanto con los LLM como con el procesamiento del lenguaje natural.

La distribución es heterogénea entre perfiles. Los LLM son la familia más frecuente en la discapacidad intelectual, el TEA, el TDAH y el síndrome de Down. En la dislexia, en cambio, el procesamiento del lenguaje natural o del habla se reporta en 5 estudios y los LLM en 1, y en las dificultades de aprendizaje el procesamiento del lenguaje natural (n=5) y los LLM (n=4) tienen frecuencias similares. El TEA y la discapacidad cognitiva son los únicos perfiles que aparecen en las cinco familias con al menos 2 estudios en cada una. El síndrome de Down solo se cruza con los LLM (n=2), y el aprendizaje profundo y la visión por computador no superan los 5 estudios en ningún perfil.

**Figura {{F1}}**

*Perfiles de discapacidad cognitiva o neurodivergencia según la familia de técnica de inteligencia artificial*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027). Base: 42 estudios cualitativos o mixtos con dato de perfil y de familia de IA; se representan los 41 que declaran un perfil específico. Un estudio puede declarar más de un perfil y aplicar más de una familia, por lo que un mismo estudio puede figurar en varias celdas.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** mapa de calor.
- **Por qué este tipo:** relación entre dos variables nominales multivalor (7 perfiles × 5 familias). El color resalta qué combinaciones se concentran y cuáles están vacías.
- **Qué muestra:** el número de estudios que combina cada perfil específico con cada familia de técnica de IA.
- **Datos a dibujar:** filas (perfil, en este orden): TEA, DI, discapacidad cognitiva, dificultades de aprendizaje, TDAH, dislexia y síndrome de Down. Columnas (familia, en este orden): LLM, PLN o habla, aprendizaje automático, aprendizaje profundo y visión por computador. Matriz:
  - TEA: [10, 7, 4, 5, 2]
  - DI: [11, 5, 2, 1, 4]
  - Discapacidad cognitiva: [6, 6, 2, 2, 2]
  - Dificultades de aprendizaje: [4, 5, 3, 1, 2]
  - TDAH: [8, 2, 3, 2, 1]
  - Dislexia: [1, 5, 3, 2, 1]
  - Síndrome de Down: [2, 0, 0, 0, 0]

  La fila «Sin perfil específico» ([0, 0, 1, 1, 0]) de `tablas/RQ2-B2.json` no se dibuja.
- **Ejes:** en el eje X, la familia de técnica en el orden de la tabla (de mayor a menor frecuencia en el cruce); en el eje Y, el perfil, con el TEA arriba. Escala de color lineal de 0 a 11.
- **Etiquetas sobre los datos:** el número de estudios en cada celda, incluidos los ceros.
- **Leyenda:** barra de color «Número de estudios coincidentes» (0–11).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «Un estudio puede figurar en varias celdas: puede declarar más de un perfil y aplicar más de una familia (base n = 42 estudios cualitativos o mixtos; se representan los 41 con perfil específico)».
- **Estilo:** escala secuencial de azules sobrios (blanco = 0), texto oscuro sobre celdas claras y blanco sobre las oscuras, 16 × 10 cm.
<!-- fin -->

## Decisiones

- **Recodificación.** No edito ningún jsonl en este bloque: hereda RQ1-I1 (cerrado en RQ1-B1) y RQ2-I1 (recodificado en RQ2-B1, 49 de 49 filas). Volví a correr `sintesis:aggregate RQ2-B2` y la base sigue en n=42. La de antes contaba la fila paraguas «Neurodivergencia» y la columna «IA»; la de ahora sale de los 42 estudios con perfil y familia (49 − 7 sin técnica de IA).
- **Columna «IA».** Desaparece de `tablas/RQ2-B2.json` porque RQ2-I1 ya no la tiene (R106 pasa a NLP, ML, DL y LLM). No hace falta un filtro.
- **Fila «Sin perfil específico». Sí hace falta un filtro**, porque RQ1-I1 no se edita. El agregador la deja como octava fila (un estudio con ML y DL). La figura la excluye y la spec lo declara en `excluidas`. **Pido al orquestador** que la conserve así o, si prefiere un filtro en el agregador, que excluya «Sin perfil específico» de las filas del cruce. Las cifras no cambian.
- **Cifras.** Todas las celdas salen de `cruce.matriz`. Los porcentajes del texto usan la base del cruce (42): 11/42 = 26%, 10/42 = 24%, 8/42 = 19%, 7/42 = 17% y 6/42 = 14%. «41 con perfil específico» es 42 menos el único estudio de la fila «Sin perfil específico» (RQ1-I1: n=1, sin otro perfil).
- **Marginales.** No se repiten, como acordó el plan. La prosa remite a los apartados de RQ1-B1 y RQ2-B1 con palabras, porque los números de sección se asignan al montar.
- **Síntesis argumental.** Cada perfil se describe por la familia que lo concentra, y el conjunto, por las celdas vacías y por los perfiles con cobertura en las cinco familias. No se atribuye causa a las diferencias.
- **Límite.** Varias celdas son pequeñas (1 o 2 estudios); el texto solo destaca las de n ≥ 5 y los patrones de ausencia. Un estudio con varios perfiles y varias familias suma en varias celdas, así que la matriz no se puede sumar por filas ni por columnas para obtener estudios.
