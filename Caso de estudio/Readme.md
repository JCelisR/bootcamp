Caso de Estudio 1: Modelo Analítico de Predicción para E-commerce

Desarrollé un pipeline integral de datos (end-to-end) con el objetivo de construir un modelo analítico capaz de predecir el gasto de los clientes dentro de una plataforma de e-commerce.

El mayor reto técnico consistió en procesar un conjunto de datos crudo que presentaba un alto grado de ruido y valores atípicos. Estas anomalías distorsionaban fuertemente las predicciones iniciales y dificultaban la lectura real del comportamiento de compra de los usuarios, lo que requería una estrategia de limpieza sumamente rigurosa.

Implementé un proceso exhaustivo de depuración y transformación de datos. Para abordar los valores atípicos, apliqué el método de Rango Intercuartílico (IQR), lo que me permitió aislar y tratar las anomalías sin perder información de valor. Posteriormente, realicé un modelado comparativo evaluando el rendimiento de una Regresión Lineal tradicional frente a un modelo más avanzado de Gradient Boosting, seleccionando finalmente la arquitectura que mejor se ajustaba a los patrones del negocio.

Todo el desarrollo lo llevé a cabo en mi entorno local de VS Code sobre Windows, utilizando Python 3.13.12. Me apoyé sólidamente en las librerías Pandas y NumPy para la manipulación y el tratamiento de los datos, y utilicé Scikit-Learn para la construcción, el entrenamiento y la validación de los modelos predictivos.

Comprendí profundamente cómo la calidad de los datos de entrada define el éxito de cualquier modelo predictivo. Trabajar con el método IQR me enseñó a no descartar datos a la ligera, sino a entender su impacto estadístico y de negocio. Además, consolidé mi capacidad para evaluar arquitecturas de machine learning, observando de primera mano cómo un modelo de ensamble como Gradient Boosting puede superar ampliamente a modelos lineales en escenarios complejos.

Logré una reducción significativa en el margen de error de las predicciones al limpiar los datos con IQR y al implementar el modelo de Gradient Boosting, mejorando la precisión general del pronóstico de gasto del cliente frente al modelo base de Regresión Lineal, con precisión de (R^2): 0.99 y un MAE de 10.94 unidades monetarias.

Habilidades técnicas aplicadas: 
	Análisis Exploratorio de Datos (EDA) y limpieza exhaustiva.
	Detección y tratamiento matemático de outliers (Método IQR).
	Modelado Predictivo y Machine Learning.
	Evaluación comparativa de algoritmos (Regresión Lineal vs. Gradient Boosting).

Elegí incluir este proyecto en la sección principal de mi portafolio porque refleja fielmente mi enfoque analítico y mi autonomía para ejecutar un ciclo de vida de datos de principio a fin. Demuestra que no solo domino la implementación de algoritmos, sino que poseo el criterio técnico necesario para preparar los datos adecuadamente y aportar soluciones tecnológicas que impactan directamente en las decisiones comerciales.

