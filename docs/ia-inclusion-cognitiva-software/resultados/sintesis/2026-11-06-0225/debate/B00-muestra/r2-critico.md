**En desacuerdo** (2 objeciones)

# B00-muestra — Ronda 2 — Crítico

Resueltas:

- **Objeción 2 de R1.** Se retiró la oración sobre «revisión bibliográfica».
- **Objeción 3 de R1.** La frase de la muestra no humana ya no atribuye unidades.
- **Objeción 1 de R1.** Con el criterio del orquestador (los B00 salen del Excel y no se recodifican), acepto mantener las cifras de `tablas/B00-muestra.json` (51/15/4/3; rango 1–1 536; mediana 14). La verificación en el MD queda escalada para corregir el formulario.

Ese mismo criterio exige dos condiciones que la versión actual no cumple:

1. La discrepancia se declara en la *Nota.*, no como frase del texto.
2. Ninguna cifra publicada contradice lo verificado en RQ1-B2.

| # | Fragmento | Problema | Corrección |
|---|---|---|---|
| 1 | «el 21% (n=15) no incluye participantes humanos» | Contradice RQ1-B2. En `tablas/RQ1-B2.json` (RQ1-I3, base 73), seis de esos 15 estudios figuran con «Presencia: Sí»: si_order 10, 14, 26, 38, 60 y 64. Publicar en 3.5 que el 21% «no incluye participantes humanos» y en RQ1 que esos mismos estudios cuentan con personas con la condición son dos afirmaciones incompatibles. Además, cuatro de esos seis (14, 26, 38 y 60) son discrepancias que el propio defensor verificó en el MD. | Mantener n=15 y 21%, pero redactar la categoría como lo que es, un registro: «el 21% (n=15) figura en el formulario sin participantes humanos registrados». No afirmar que el estudio no los tiene. |
| 2 | «En al menos siete estudios, el tamaño de muestra registrado en el formulario de extracción no coincide con el declarado en el texto completo; las cifras se presentan tal como figuran en el formulario.» | Va en la prosa de Resultados, como si fuera un hallazgo, cuando el criterio exige declararla en la *Nota.*. Tampoco avisa al lector del choque con la sección de participación (RQ1). | Retirar la oración del párrafo y añadir, bajo el párrafo, una *Nota.*: «*Nota.* Las categorías proceden del registro de muestra del formulario de extracción. En al menos siete estudios, ese registro no coincide con el tamaño declarado en el texto completo, y seis de los registrados sin participantes humanos figuran con participación de personas con la condición en la sección de participación (RQ1).» Si el lint no admite una *Nota.* sin tabla, el bloque pasa a una **Tabla** de cuatro filas (Frecuencia (n), Porcentaje) con esa *Nota.*; las cifras no cambian. |
