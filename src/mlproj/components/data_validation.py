import os
from mlproj import logger
from mlproj.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)

    def validate_all_columns(self) -> None:
        data_file_path = self.config.unzip_data_dir / "data.csv"  # Assuming the data file is named 'data.csv'
        
        if not data_file_path.exists():
            logger.error(f"Data file not found at {data_file_path}")
            raise FileNotFoundError(f"Data file not found at {data_file_path}")

        data = pd.read_csv(data_file_path)
        missing_columns = [col for col in self.config.all_schema['COLUMNS'] if col not in data.columns]

        if missing_columns:
            logger.error(f"Missing columns in data: {missing_columns}")
            raise ValueError(f"Missing columns in data: {missing_columns}")
        else:
            logger.info("All required columns are present in the data.")
            