# Curso de Análisis de Algoritmos - ITM

## Propósito del repositorio

Este repositorio sirve como espacio de trabajo para el curso de análisis de algoritmos del ITM. Aquí se organizarán los materiales de laboratorio, los ejercicios de clase y los scripts de medición de desempeño que se utilizarán durante el semestre.

## Estructura del repositorio

La organización del proyecto está pensada para mantener el trabajo ordenado y reproducible:

- `laboratorios/`: aquí se almacenarán, en el futuro, los cinco informes de laboratorio evaluativos.
- `ejercicios-clase/`: aquí se guardarán los ejercicios prácticos no evaluativos, incluyendo los trabajos de la Semana 2.
- `benchmarks/`: aquí se colocarán los scripts compartidos para medición de tiempos y visualización de resultados.
- `README.md`: documento principal que describe el repositorio y sirve como plantilla base para documentar cada informe.
- `.gitignore`: archivo con patrones para excluir archivos temporales o de entorno que no deben versionarse.

## Plantilla para informes de laboratorio

### Objetivo

Describir el problema planteado, el enfoque utilizado y los resultados obtenidos en cada actividad evaluativa.

### Metodología

1. Definir el problema.
2. Implementar la solución.
3. Ejecutar la validación.
4. Registrar los resultados y las conclusiones.

### Ejemplo de ejecución

```bash
python -m pytest
python benchmarks/benchmark.py
```

## Flujo de trabajo recomendado

Para mantener el repositorio consistente durante el curso, conviene seguir este orden:

1. Crear o actualizar el contenido de cada carpeta según la actividad.
2. Documentar el procedimiento y los resultados en el informe correspondiente.
3. Ejecutar las pruebas o benchmarks necesarios.
4. Registrar cada avance con un commit específico y sincronizarlo con GitHub.

## Seguimiento del curso

Este repositorio también permite mantener un historial claro del trabajo realizado mediante commits incrementales, de modo que cada avance del proyecto quede documentado con precisión.
