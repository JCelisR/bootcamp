# Predicción inteligente de gasto en clientes e-commerce

Este proyecto utiliza técnicas de **Aprendizaje Automatizado (Machine Learning)** para predecir el gasto anual de los clientes de una plataforma de comercio electrónico basándose en su comportamiento digital y perfil demográfico.

## Descripción del Problema
El Departamento de Analítica Comercial busca identificar qué factores impulsan el gasto de los clientes para optimizar sus estrategias de marketing y fidelización. El objetivo es construir un modelo de **Regresión Supervisada** que estime el gasto anual con alta precisión.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.13
* **Librerías Principales:** * `Pandas` y `NumPy` para manipulación de datos.
    * `Scikit-Learn` para modelado, escalamiento y optimización.
    * `Matplotlib` y `Seaborn` para visualización de datos.

## Pipeline del Proyecto
El desarrollo se dividió en 8 lecciones estratégicas:
1. **Fundamentos:** Definición del problema de regresión.
2. **Ajuste y Validación:** Implementación de K-Fold Cross Validation.
3. **Preprocesamiento:** Escalamiento de datos (`StandardScaler`) y tratamiento de outliers.
4. **Modelado Inicial:** Comparación entre Regresión Lineal y Polinomial.
5. **Análisis Conceptual:** Comparación entre tareas de Clasificación y Regresión.
6. **Métricas:** Evaluación mediante MAE, RMSE y $R^2$.
7. **Optimización:** Ingeniería de características y regularización (Ridge/Lasso).
8. **Algoritmos Avanzados:** Implementación de **Gradient Boosting Regressor**.

## Resultados Finales
Tras la optimización, el modelo alcanzó un desempeño excepcional:
* **Modelo Seleccionado:** Regresión Lineal (por su alta interpretabilidad).
* **Precisión ($R^2$):** 0.99
* **Error Medio Absoluto (MAE):** 10.94 unidades monetarias.

**Conclusión clave:** Los años de membresía y el tiempo de uso de la aplicación móvil son los predictores más influyentes en el volumen de ventas por cliente.

---
*Proyecto desarrollado como parte del Módulo 6 del programa de Data Science.*