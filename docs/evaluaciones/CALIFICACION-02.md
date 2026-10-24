# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Julian Esteban Suarez Gallego · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `41d5c3c`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 12 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 14 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **72 / 100** |
| **Nota (0–5)** | **3.60** |

## 1. Corrección conceptual (12 / 20)
**Lo que hizo bien:**
- En la pregunta 4 explica bien que, para hallar el máximo de un arreglo, dividir no ayuda: combinar cuesta un paso constante y la recurrencia `T(n) = 2T(n/2) + O(1)` da `Θ(n)`, igual que recorrer una vez.
- En la pregunta 5 recomienda divide y vencerás y avisa que el tiempo a 1.000.000 de registros es una estimación.

**Lo que puede mejorar:**
- Pregunta 3: dice que desde n = 100 divide y vencerás gana "significativamente", pero en su gráfica los tamaños pequeños no se distinguen y no incluyó una tabla con los valores. La afirmación no se apoya en datos que el lector pueda ver.
- Pregunta 5: las cifras (1 a 2 segundos, "muchas semanas") no vienen de un cálculo mostrado. Con la fuerza bruta de su propia gráfica (cerca de 2.8 s en n = 8000), crecer 125 veces en tamaño daría del orden de horas, no semanas. Muestre el paso a paso de la estimación.
- En la pregunta 4 repite la misma idea de `Θ(n)` dos veces; mejor use ese espacio para comparar con claridad el costo de combinar en ambos problemas.

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término (dos mitades y el barrido del caso cruzado).
- Aplica el método maestro con a = 2, b = 2, compara con `n^(log₂ 2) = n` y concluye el caso 2 con `Θ(n log n)`.

**Lo que puede mejorar:**
- La justificación de `Θ(n²)` para la fuerza bruta es muy breve ("dos ciclos anidados"). Falta contar cuántos pares de días se revisan (`n(n+1)/2`) para llegar al resultado.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista.
- `pruebas.py` cubre la serie de ocho días, un elemento, todos negativos, todos positivos, un caso cruzado y 20 listas aleatorias.
- Todas las funciones tienen type hints y docstrings en estilo Google.

**Lo que puede mejorar:**
- Falta dejar dos líneas en blanco entre funciones y antes del bloque final en `subarreglo.py`, `pruebas.py` y `medicion.py` (PEP 8).

## 4. Calidad del análisis de las gráficas (14 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños (de 10 a 8000).
- Interpreta bien que la fuerza bruta crece como parábola y que divide y vencerás queda casi plana.

**Lo que puede mejorar:**
- Los números de la pregunta 2 no coinciden con su gráfica publicada: dice que la fuerza bruta pasa de 0.21 s a 0.85 s entre 4000 y 8000, pero la gráfica muestra cerca de 1.1 s y 2.8 s. Para divide y vencerás dice 0.004 a 0.008 y la gráfica muestra valores cercanos a 0.01 y 0.03. Las cifras deben salir de la gráfica o de una tabla que usted publique.
- No calcula de forma clara el factor de crecimiento de divide y vencerás ni lo compara con lo que predice `Θ(n log n)` (algo un poco mayor que 2).
- Con una sola medición por tamaño y sin decirlo en el informe, el ruido afecta los factores. Repita cada medición y agregue una tabla con los tiempos medidos.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta `lab2-divide-y-vencer/` con todos los archivos del entregable, README en el orden pedido, nombre, instrucciones, enlaces al código en cada parte y gráfica visible.
- Cuatro commits del laboratorio con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción solo sirven para Windows; agregue también el comando para macOS/Linux.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en cada tamaño medido y el script de medición corre sin errores y genera la gráfica.

## Para el próximo laboratorio
- Apoye cada cifra del análisis en un valor que se pueda leer en su gráfica o en una tabla incluida en el informe.
- Muestre el cálculo paso a paso de las estimaciones para tamaños grandes.
- Repita cada medición varias veces y dígalo en el informe.
- Deje dos líneas en blanco entre funciones y antes del bloque final en todos los archivos.
- Justifique con cuentas, no solo con una frase, la complejidad de cada algoritmo.
