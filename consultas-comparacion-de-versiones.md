### Faltantes

- La gráfica G-4 no muestra el tooltip que deberia de mostrar cuando se pasa el mouse por encima de un cambio
  Documento: "Tooltip por cambio: máquina, molde de origen → destino, turno y horas de setup."

- La interfaz no permite intercambiar A ↔ B en la comparación. El "FSC-CF-004_Comparacion_de_Versiones_del_Plan_v0.3" lo menciona en "RN-04 (§8.1)", "RN-06" y "Criterio de aceptación #5 (§9)", pero en el Brief no esta documentado. Por lo que la UI no tiene esta funcionalidad. Entonces, esta caracteristica no estará disponible?

### Recomendaciones

- En la tarjeta de Reglas se entiende que muestre "Conforme", pero lo muestra de manera duplicada: Conforme → Conforme. Se puede interpretar que tanto la version vigente como candidata estan conformes, pero se recomienda o eliminar el duplicado o cambiar el texto por "Vigente" o "Candidata" segun sea el caso.

- Se recomienda que las 8 tarjetas no salgan tan pegadas y mejor se dispongan en dos filas para que no se vea tan pegado.
  Documento: "Ocho tarjetas compactas en una fila, con el mismo contenido que FSC-CF-004 V3:"

- En el gráfico **G-1 ¿Llega cada pedido a tiempo?**: se recomienda pasar de usar un rombo a usar una línea para representar la fecha de compromiso, pues un rombo da la impresión de que la zona sombreada, que ya se considera tarde, aún está dentro de sus esquinas.

- Una cosa que confunde y va en contra del "estandar" o similitud entre otras vistas es usar el icono ▲ para indicar un atraso o pérdida; en otras vistas esto se representa con el triángulo hacia abajo, por lo que se recomienda cambiar el icono por el triángulo hacia abajo. Para mantener la coherencia visual

- En la UI temporal sale el siguiente titulo: "indisponible (E-41)" y se recomienda cambiarlo por "indisponible". Asi mismo, que significa "(E-41)"? No esta documentado ni en el FSC ni en el Brief, solo esta citado

- En la grafica G-3, se recomienda cambiar el tipo de evento: en lugar de ser un evento clic para abrir el modal, que sea un tooltip con un evento hover, es mas limpio y estandarizado al comportamiento de otras graficas
  Documento: "...al pulsar una celda se abre un panel flotante con A y B..."

- En la tabla G-4 se recomienda mostrar por turno y que solo salgan los turnos donde hayan cambios, en lugar de ser diarios y tener todos los turnos juntos, porque puede haber muchos turnos y eso rompería la UI, ya ahora mismo, los turnos se apilan orizontalmente, uno al lado de otro.
  Documento: "Forma: barras verticales pareadas por día (A y B)... rotulado con el turno (T1, T2 o T3)."

### Agente

- En las funcionalidades del agente se menciona que este guarda el estado de plegado o no del panel de Rupert, esto no esta habilitado para ningun agente de funcion, esta propiedad sera unica de esta vista?
  Documento: "Panel Rupert: acoplado a la derecha, de 380 px y abierto por defecto. Se pliega a un botón flotante y recuerda su estado por usuario. ⏳ DD-01"

- Al dar clic sobre un punto numerado (1...5), el panel de Rupert da la explicación de ese punto, al dar clic en el tour, el agente responde cada punto del tour. al pedir una explicacion desde la grafica, el agente responde la explicacion de la grafica con el punto.
  ¿Debería reutilizarse el comentario que da Rupert en cada una de las gráficas, o debería responder el agente cada vez que alguien hace clic en un punto numerado? Pj: en 1 (responde), luego en 2 (responde), luego en 1 (vuelve a responder), etc.

- El narrador lee el significado de ese punto numerado del 1 al 5. ¿Se mantiene el uso de la API del mismo navegador o se implementará alguna herramienta extra?
  Documento: "Recorrer los puntos ▶": recorrido guiado de un punto por paso, con "Siguiente" y "Anterior", en el que Rupert narra cada paso. ⏳ DD-02

- Las acciones de las recomendaciones, ¿abren vistas de la página de Rupert o despliegan diálogos con un formulario por rellenar? Tengo entendido que abren vistas de la página de Rupert, y en los dialogos del mockup aclaran que se despliegan diálogos temporales pero si redirige a la vista de Rupert, pero lo pregunto por las dudas.

### Dudas que desconocía:\*\*

- ¿Cuándo se considera publicado un turno?
  Documento: "marca de turno publicado en el encabezado de la columna."

- El ámbito en "Puntos de atención" puede ser "Demanda" o "Producción". Con "Demanda", ¿nos referimos al proceso de Demanda, previo a Producción? Tengo entendido que no. Pero en "S-7 Tarjeta de recomendación" se habla de "plan de demanda". LO destaco porque tenia entendido que plan de demanda no se tocaba porque estamos en plan de producción.
