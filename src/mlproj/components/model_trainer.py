import os
import pandas as pd
from mlproj import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlproj.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> ElasticNet:
        train_data = pd.read_csv(self.config.data_ingestion.train_file_path)
        test_data = pd.read_csv(self.config.data_ingestion.test_file_path)

        train_x = train_data.drop(columns=[self.schema.target_column], axis=1)
        train_y = train_data[self.schema.target_column]
        test_x = test_data.drop(columns=[self.schema.target_column], axis=1)
        test_y = test_data[self.schema.target_column]

        lr = ElasticNet(
            alpha=self.model_trainer_config.alpha,
            l1_ratio=self.model_trainer_config.l1_ratio,
            random_state=42
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.model_trainer_config.train_model_dir, self.model_trainer_config.model_file_name))

        