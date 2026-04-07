# Pipeline de Datos RetailMax: Procesamiento con Apache Spark

Este repositorio contiene la resolución del proyecto final del **Módulo 9: Fundamentos de Big Data**. Se implementó un flujo completo de ingeniería de datos utilizando el motor de procesamiento distribuido Apache Spark.

## Tecnologías utilizadas
* **Lenguaje:** Python 3.13
* **Motor de Procesamiento:** Apache Spark (PySpark 3.x)
* **ML Library:** Spark MLlib (Algoritmo K-Means)
* **Entorno de Ejecución:** Google Colab (Nube)

> **Nota Técnica sobre el Entorno:** > Inicialmente se intentó la ejecución en un entorno local (VS Code en Windows 11). Debido a restricciones de seguridad del sistema operativo y bloqueos en la comunicación de red interna de los "Python Workers" (error `java.io.EOFException`), se migró el desarrollo a **Google Colab**. Esta transición permitió una ejecución nativa y estable sobre un entorno Linux optimizado para Big Data, eliminando cuellos de botella de infraestructura local.

## Estructura del Pipeline
1. **Ingesta y Optimización (AE3):** Carga de datos estructurados mediante DataFrames de Spark y aplicación de `.cache()` para optimizar el uso de memoria RAM.
2. **Análisis con Spark SQL (AE4):** Implementación de consultas de agregación para determinar los ingresos totales por categoría de producto.
3. **Machine Learning (AE5):** Construcción de un pipeline de clustering no supervisado para segmentar clientes según su volumen de inversión.
4. **Visualización de Resultados:** Generación de reportes gráficos para la toma de decisiones estratégicas.

## Resultados del Análisis
Una vez ejecutado el pipeline, se obtuvieron los siguientes hallazgos estratégicos para RetailMax:

1. Líder de Ventas: La categoría de Tecnología representa el mayor volumen de ingresos con un total de $650.0.
2. Segmentación de Clientes: El modelo K-Means clasificó exitosamente a los clientes, detectando perfiles de alta inversión (Cliente C1) frente a compradores de volumen moderado.

## Cómo ejecutar en Google Colab
1. Sube el archivo `Proyecto_RetailMax.ipynb` a tu Google Drive.
2. Ábrelo con **Google Colab**.
3. Ejecuta la primera celda (`!pip install pyspark`) para preparar el entorno.
4. Ejecuta el resto de las celdas para visualizar las tablas de Spark y los gráficos de resultados.

---