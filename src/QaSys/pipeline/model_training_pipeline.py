from QaSys import logger
from QaSys.config import ConfigurationManager
from QaSys.components.model_training import ModelTraining
from QaSys.components.model_preprocessing import ModelProcess


stage_name = "Model Training Stage"

class ModelTrainingPipeline:

      def __init__(self):
            pass
      
      def Train_Model(self):
            config = ConfigurationManager()
            train_model_config = config.get_model_training_config()
            model_process = ModelProcess("google/flan-t5-base")
            
            trainModel = ModelTraining(model_process, train_model_config)
            trainModel.train_model()


if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {stage_name} started <<<<<<")
            obj = ModelTrainingPipeline()
            obj.Train_Model()
            logger.info(f">>>>>> {stage_name} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e