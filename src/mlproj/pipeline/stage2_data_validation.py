from mlproj.config.configuration import ConfigurationManager
from mlproj.components.data_validation import DataValidation
from mlproj import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.data_validation_config = self.config_manager.get_data_validation_config()

    def run_pipeline(self):
        try:
            logger.info(f"Starting {STAGE_NAME}")
            data_validation = DataValidation(config=self.data_validation_config)
            data_validation.validate_all_columns()
            logger.info(f"Completed {STAGE_NAME} successfully")
        except Exception as e:
            logger.exception(f"Error in {STAGE_NAME}: {e}")
            raise e
        
    def main(self):
        self.run_pipeline() 

if __name__ == "__main__":
    pipeline = DataValidationPipeline()
    pipeline.main()