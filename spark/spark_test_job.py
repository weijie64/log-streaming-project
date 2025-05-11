from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder \
    .appName("WordCountTest") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")

# Sample data
lines = spark.read.text("file:///opt/spark-apps/test_data.txt")
words = lines.selectExpr("explode(split(value, ' ')) as word")

# Count word frequencies
word_counts = words.groupBy("word").count()

# Show the result
word_counts.show()

# Stop the Spark session
spark.stop()
