from mlproj.constants import *
from mlproj.utils.common import read_yaml, create_directory
from mlproj.entity.config_entity import TrainingPipelineConfig

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

        create_directory(Path(self.config.artifacts_root))
    
    def get_data_ingestion_config(self) -> TrainingPipelineConfig:
        config = self.config.data_ingestion

        data_ingestion_config = TrainingPipelineConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config 
