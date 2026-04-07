from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Inicializar sesión de Spark
spark = SparkSession.builder.appName("ML_Escalable_Ecommerce").getOrCreate()

# 1. Carga de datos (Preparación de entrada)
# El dataset debe contener registros de navegación, compras y calificaciones.
df = spark.read.csv("datos_ecommerce.csv", header=True, inferSchema=True)

# 2. Transformación y Vectorización
# Convertimos categorías a índices y agrupamos características en un vector
indexer = StringIndexer(inputCol="categoria_producto", outputCol="cat_index")
assembler = VectorAssembler(
    inputCols=["tiempo_navegacion", "compras_previas", "calificacion_media", "cat_index"], 
    outputCol="features"
)

# 3. Implementación del Modelo (Random Forest)
rf = RandomForestClassifier(labelCol="realizo_compra", featuresCol="features")

# 4. División de datos (80% Entrenamiento, 20% Prueba)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# 5. Ajuste de Hiperparámetros con Validación Cruzada
paramGrid = ParamGridBuilder().addGrid(rf.numTrees, [10, 30]).build()
crossval = CrossValidator(
    estimator=Pipeline(stages=[indexer, assembler, rf]),
    estimatorParamMaps=paramGrid,
    evaluator=BinaryClassificationEvaluator(labelCol="realizo_compra"),
    numFolds=3
)

# Entrenamiento distribuido
model = crossval.fit(train_data)