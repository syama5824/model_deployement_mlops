from mlproj.config.configuration import ConfigurationManager
from mlproj.components.data_transofrmation import DataTransformation
from mlproj import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            with open("artifacts/stage3.txt", "w") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()

        except Exception as e:
            logger.exception(f"Error in {STAGE_NAME}: {e}")
            raise Exception("Data Validation Failed. Cannot proceed to Data Transformation.")

if __name__ == "__main__":
    try:
            logger.info(f"Starting {STAGE_NAME}")
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
            logger.info(f"Completed {STAGE_NAME} successfully")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e