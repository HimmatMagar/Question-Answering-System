from src.QaSys import logger
from src.QaSys.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.QaSys.pipeline.model_training_pipeline import ModelTrainingPipeline


# STAGE_NAME = "Data Ingestion Stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = DataIngestionPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e


stage_name = "Model Training Stage"
try:
      logger.info(f">>>>>> {stage_name} started <<<<<<")
      obj = ModelTrainingPipeline()
      obj.Train_Model()
      logger.info(f">>>>>> {stage_name} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e