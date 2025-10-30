from mlproj.constants import *
from mlproj.utils.common import read_yaml, create_directories
from mlproj.entity.config_entity import TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories(Path(self.config.artifacts_root))
    
    def get_data_ingestion_config(self) -> TrainingPipelineConfig:
        config = self.config.data_ingestion

        data_ingestion_config = TrainingPipelineConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config 
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories
        ([
            Path (config.root_dir)
        ])

        data_validation_config = DataValidationConfig(
            root_dir= Path (config.root_dir),
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir= Path (config.unzip_data_dir),
            all_schema= self.schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_transformation_config = self.config.data_transformation

        create_directories([data_transformation_config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir= Path(data_transformation_config.root_dir),
            data_path= Path(data_transformation_config.data_path)
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories
        ([
            Path (config.root_dir),
            Path (config.train_model_dir),
            Path (config.test_model_dir)
        ])

        model_trainer_config = ModelTrainerConfig(
            root_dir= Path (config.root_dir),
            train_model_dir= Path (config.train_model_dir),
            test_model_dir= Path (config.test_model_dir),
            model_file_name= config.model_file_name,
            alpha = self.params.alpha,
            l1_ratio = self.params.l1_ratio,
            target_column= self.schema.target_column
        )

        return model_trainer_config