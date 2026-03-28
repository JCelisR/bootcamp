# 💼 Proyecto Módulo 8: Clasificador Inteligente StyleNet

## 📋 Descripción del Proyecto
Este proyecto fue desarrollado para el Área de Ciencia de Datos de la tienda virtual **StyleNet**. El objetivo principal es automatizar la clasificación de imágenes de prendas de vestir subidas a la plataforma de comercio electrónico, reduciendo el trabajo manual y los errores de categorización.

El modelo utiliza Deep Learning para clasificar imágenes en 10 categorías distintas utilizando el dataset **Fashion-MNIST**.

## 🛠️ Tecnologías y Entorno
* **Lenguaje:** Python 3.13.12
* **Framework:** PyTorch & Torchvision
* **Entorno de Desarrollo:** Visual Studio Code (VS Code)
* **Librerías Adicionales:** Matplotlib (visualización)

## 🏗️ Arquitectura del Proyecto y Decisiones Técnicas

El proyecto aborda la problemática mediante la implementación y comparación de dos arquitecturas:
1. **Modelo Baseline (Red Densa - MLP):** Un enfoque tradicional aplanando las imágenes.
2. **Modelo Avanzado (CNN):** Una Red Neuronal Convolutiva que incluye extracción de características espaciales y técnicas de regularización (Dropout) para evitar el sobreajuste.

### ⚠️ Nota sobre la Ejecución y Estructura del Código
Durante la fase de desarrollo, se intentó modularizar el código ejecutando cada lección y componente (carga de datos, definición de modelos, bucles de entrenamiento) en celdas o archivos estrictamente separados. Sin embargo, esto generaba inconsistencias de memoria y errores de alcance de variables (como `NameError`). 

**Decisión técnica:** Para asegurar un flujo de ejecución estable, eficiente y sin interrupciones en el entrenamiento de los tensores en PyTorch, **se decidió unificar el pipeline completo en un solo bloque secuencial dentro del notebook**. En flujos de trabajo de Deep Learning, mantener vivas en memoria las instancias del Dataloader, el optimizador y la arquitectura del modelo de forma unificada garantiza que el *backpropagation* se ejecute correctamente y facilita la reproducibilidad del experimento.

## 🚀 Cómo ejecutar el proyecto
1. Clonar este repositorio.
2. Asegurar tener instalado Python 3.13+.
3. Instalar las dependencias: `pip install torch torchvision matplotlib`.
4. Ejecutar el archivo `.ipynb` o el script de Python en un entorno compatible (se recomienda VS Code). El código descargará automáticamente el dataset `FashionMNIST` y comenzará el entrenamiento, finalizando con una visualización predictiva.

## 📊 Resultados
La implementación de la arquitectura Convolutiva superó a la red densa, logrando extraer eficazmente los patrones de las prendas de vestir y realizando predicciones visuales precisas en el conjunto de datos de prueba.