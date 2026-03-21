# Segmentador Inteligente de Clientes - Retail Insights S.A. 📊🛒

## Descripción del Proyecto
Este proyecto aplica técnicas avanzadas de Aprendizaje No Supervisado (Machine Learning) para descubrir estructuras ocultas y perfiles de consumo en una base de datos de clientes de retail, sin necesidad de etiquetas previas.

La consultora Retail Insights S.A. requiere transformar datos brutos en grupos de consumidores accionables. El objetivo es construir un pipeline que combine Clustering y Reducción de Dimensionalidad para optimizar estrategias de fidelización y detectar comportamientos atípicos o posibles fraudes.

## Características Principales
Estructura del Repositorio
* Proyecto_Modulo7.ipynb: Notebook con el flujo completo documentado (Clases 1-5).
* test.csv: Dataset fuente de comportamiento de clientes.
* README.md: Documentación técnica del proyecto.
* Informe_Final.pdf: Resumen ejecutivo con las recomendaciones comerciales para la consultora.

## Stack Tecnológico
* **Lenguaje:** Python 3.13
* **Librerías de modelado:** 
  * `Scikit-Learn` K-Means, DBSCAN, PCA, t-SNE y Escalado.
  * `SciPy` Generación de dendrogramas para agrupamiento jerárquico.
* **Visualización:** 
  * `Pandas` y `NumPy` para manipulación de datos. 
  * `SciPy` Generación de dendrogramas para agrupamiento jerárquico.

## Estructura del Repositorio
El desarrollo se estructuró en 5 lecciones estratégicas:
* `Fundamentos`: Definición de tareas no supervisadas y casos de uso en marketing.
* `Técnicas de Clusterización`: Comparativa teórica y técnica entre K-Means, DBSCAN y Jerárquico.
* `Reducción de Dimensionalidad`: Implementación de PCA (lineal) y t-SNE (no lineal) para visualización en 2D.
* `Implementación y Métricas`: Selección de K mediante el Método del Codo y evaluación con el Coeficiente de Silueta.
* `Evaluación Comercial`: Interpretación de clústeres y detección de ruido (outliers) para toma de decisiones.

## Resultados Clave
Tras la ejecución del pipeline, se obtuvieron resultados clave para la estrategia de negocio:
* **Segmentación Óptima:** Se identificaron 5 clústeres diferenciados (incluyendo Clientes VIP y Clientes con Potencial de Crecimiento).
* **Calidad del Modelo:** Coeficiente de Silueta de 0.2480, validado visualmente mediante una proyección t-SNE que mostró una separación clara de grupos.
* **Detección de Anomalías:** DBSCAN identificó 344 puntos de ruido, permitiendo aislar comportamientos de compra erráticos o atípicos.
* **Eficiencia de Datos:** Mediante PCA, se logró capturar el 80% de la varianza acumulada utilizando únicamente los 2 primeros componentes principales.

*Proyecto desarrollado como parte del Módulo 7 del programa de Data Science: Aprendizaje No Supervisado.*