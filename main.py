from src.QaSys import logger
from src.QaSys.pipeline.data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e