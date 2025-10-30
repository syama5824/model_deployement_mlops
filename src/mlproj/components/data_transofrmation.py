import os
from mlproj import logger
from mlproj.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        try:
            df = pd.read_csv(self.config.data_path)
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            train_file_path = self.config.root_dir / "train.csv"
            test_file_path = self.config.root_dir / "test.csv"

            train_df.to_csv(train_file_path, index=False)
            test_df.to_csv(test_file_path, index=False)

            logger.info(f"Train and test data saved at {train_file_path} and {test_file_path} respectively.")

        except Exception as e:
            logger.exception(e)