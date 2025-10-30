
from mlproj.config.configuration import ConfigurationManager
from mlproj.components.model_trainer import ModelTrainer
from mlproj import logger

STAGE_NAME = "Model Trainer Stage"


class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train_model()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME} successfully")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e