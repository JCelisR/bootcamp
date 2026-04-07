# Pipeline de Datos RetailMax

Repositorio con la resolución del proyecto final del Módulo 9: Fundamentos de Big Data.

## Tecnologías utilizadas
* **Python 3.13**
* **Pandas** (Procesamiento de datos)
* **Scikit-Learn** (Modelado K-Means)
* **Lógica de Pipeline:** Inspirada en la arquitectura de Apache Spark.

## Estructura del Pipeline
1. **Carga de Datos:** Simulación de ingesta distribuida de ventas.
2. **Procesamiento:** Conversión a estructuras de datos optimizadas.
3. **Análisis SQL:** Agrupación de ventas por categoría para reportes financieros.
4. **Machine Learning:** Algoritmo de clustering para segmentación de clientes.

## Resultados del Análisis
Una vez ejecutado el pipeline, se obtuvieron los siguientes hallazgos estratégicos para RetailMax:

1. Líder de Ventas: La categoría de Tecnología representa el mayor volumen de ingresos con un total de $650.0.
2. Segmentación de Clientes: El modelo de Machine Learning identificó exitosamente dos perfiles de comportamiento:
    - Inversión Alta: Clientes con compras superiores (ej. Cliente C1 con $500.0).
    - Inversión Baja: Clientes con compras frecuentes pero de menor monto (ej. Clientes C2, C3 y C4).

## Cómo ejecutar
1. Abrir el archivo `Proyecto_RetailMax.ipynb` en VS Code o Jupyter.
2. Ejecutar todas las celdas en orden.
3. Los resultados se mostrarán directamente en las celdas de salida.


--- 

## Desafíos Técnicos y Soluciones
Durante el desarrollo del proyecto en un entorno local (Windows 11), se presentaron limitaciones de comunicación entre el motor Java de Spark y las restricciones de seguridad de la versión de Python (Microsoft Store).

1. Problema: Error java.io.EOFException y cierres inesperados de los "Python Workers" al intentar visualizar datos con Spark nativo.

2. Solución Aplicada: Se implementó una Arquitectura de Simulación de Big Data. Se mantuvo la lógica de pipeline solicitada (Ingesta -> SQL -> ML), pero se utilizó el motor de procesamiento en memoria de Python para garantizar la estabilidad y visualización de los resultados, emulando fielmente el comportamiento de un cluster distribuido.

---