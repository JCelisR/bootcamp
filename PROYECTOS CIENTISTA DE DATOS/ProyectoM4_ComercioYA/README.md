# Proyecto Módulo 4: Análisis de Datos para ComercioYA

## Descripción
Este proyecto realiza un flujo completo de **Análisis Exploratorio de Datos (EDA)** y **Modelado Estadístico** sobre el dataset de ComercioYA. El objetivo es identificar patrones de compra y evaluar si la actividad web predice el gasto de los clientes.

## Tecnologías Utilizadas
- **Python 3.10+**
- **Pandas / NumPy**: Limpieza y procesamiento.
- **Seaborn / Matplotlib**: Visualización estadística avanzada.
- **Statsmodels**: Regresión Lineal OLS.
- **Scikit-learn**: Métricas de evaluación (MSE, MAE, R2).

## Estructura del Repositorio
- `Proyecto_Modulo4.ipynb`: Notebook documentado paso a paso (Clases 1-6).
- `comercio_ya_datos.csv`: Datos fuente de clientes y ventas.
- `grafico_final_comercioya.png`: Visualización resumen de gasto por género y visitas.
- `Proyecto_Modulo4.pdf`: Exportación del análisis final.

## Principales Hallazgos
- **Integridad de Datos:** Se eliminaron registros con edades inconsistentes y montos negativos.
- **Análisis de Correlación:** Se obtuvo una correlación de Pearson de **[0,01]** entre visitas y monto. Esto confirma que el comportamiento de gasto es independiente de la frecuencia de navegación, sugiriendo que otros factores (como promociones o necesidad del producto) son los verdaderos motores de venta.
- **Predicción:** El modelo de regresión lineal simple mostró que las visitas web no son un predictor suficiente para el volumen de ventas ($R^2$ bajo).
- **Segmentación:** El análisis de violín y pairplot confirmó que el comportamiento de gasto es homogéneo entre géneros.

## ¿Cómo ejecutar?:
1. Clona el repositorio.
2. Instala las dependencias: `pip install pandas seaborn statsmodels scikit-learn`
3. Abre el archivo `.ipynb` en VS Code o Jupyter Notebook.