from QaSys import logger
from QaSys.entity import * 
from QaSys.utils import *
from QaSys.constants import *


class ConfigurationManager:

      def __init__(self, config = config):
            self.config = read_yaml(config)
            
            create_dir([self.config.root_artifact])
            logger.info("Root artifact directory created")
      
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_dir([config.root_dir])

            return DataIngestionConfig (
                  root_dir=config.root_dir,
                  source_url=config.source_url,
                  zip_file=config.zip_file,
                  unzip_file=config.unzip_file
            )
      

      def get_model_training_config(self) -> ModelTrainingConfig:
            config = self.config.model_training
            create_dir([config.root_dir])

            return ModelTrainingConfig (
                  root_dir=config.root_dir,
                  data_path=config.data_path,
                  adapter=config.adapter
            )