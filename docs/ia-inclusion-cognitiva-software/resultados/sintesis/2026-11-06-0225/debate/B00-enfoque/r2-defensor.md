# B00-enfoque — Ronda 2 — Defensor

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | La oración de bases omite los ítems con `n_base` = 73 (RQ1-I3, RQ1-I4 y RQ3-I1, presentes en ambas hojas) | Acepto. Verificado en `matriz.json`: hay 3 ítems con `n_base` = 73, 5 con 49 y 5 con 43 | Se añade el tercer caso sin códigos internos: «…, y los tres ítems comunes a ambas hojas, sobre los 73 estudios» |

## Texto propuesto

<!-- inicio -->
### 3.2. Enfoques metodológicos empleados

Del total de 73 artículos seleccionados, el 41% (n=30) emplea un enfoque cualitativo, el 33% (n=24) un enfoque cuantitativo y el 26% restante (n=19) métodos mixtos. En consecuencia, los ítems cualitativos del formulario se analizan sobre los 49 estudios con enfoque cualitativo o mixto, los ítems cuantitativos sobre los 43 estudios con enfoque cuantitativo o mixto, y los tres ítems comunes a ambas hojas, sobre los 73 estudios.
<!-- fin -->

## Decisiones

- Cifras de `tablas/B00-enfoque.json` (30/24/19; N = 73). Las bases 49 = 30 + 19 y 43 = 24 + 19 coinciden con `items_meta.<ítem>.n_base`.
- Se mantiene la oración en 3.2 en lugar de repartirla, porque es el primer lugar donde el lector conoce el reparto por enfoque. Cada bloque RQ seguirá declarando su propia base.
