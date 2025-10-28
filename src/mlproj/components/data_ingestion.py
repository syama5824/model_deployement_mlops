import os
import shutil
import urllib.request as request
import zipfile
from mlproj import logger
from mlproj.utils.common import get_size
from mlproj.entity.config_entity import TrainingPipelineConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: TrainingPipelineConfig):
        self.config = config
        # Ensure the root directory for ingestion exists
        # You should have created artifacts/data_ingestion earlier, but creating it here adds robustness
        os.makedirs(self.config.root_dir, exist_ok=True) 

    # We modify download_data to be more generic and handle both local/remote
    def download_or_copy_data(self) -> Path:
        source_url = self.config.source_URL
        dest_path = self.config.local_data_file

        # 1. Handle Remote Download (e.g., starts with http)
        if source_url.lower().startswith('http'):
            if not os.path.exists(dest_path):
                # Ensure local directory for saving the file exists
                os.makedirs(dest_path.parent, exist_ok=True) 

                filename, headers = request.urlretrieve(
                    url = source_url,
                    filename = dest_path
                )
                logger.info(f"Remote file: {filename} downloaded successfully.")
            else:
                logger.info(f"Remote file already exists.")

        # 2. Handle Local Copy (if source_URL is a local file path)
        elif os.path.exists(source_url):
            # The destination path needs its parent directory created first
            os.makedirs(dest_path.parent, exist_ok=True) 
            
            # Use shutil.copy to copy the CSV file locally
            shutil.copy(source_url, dest_path)
            logger.info(f"Local file copied from {source_url} to {dest_path}")
            
        else:
            logger.error(f"Source URL/Path is invalid or does not exist: {source_url}")
            raise FileNotFoundError(f"Data source not found at {source_url}")

        return dest_path
    
    # We rename this to reflect the unzipping step which may not always be needed
    def extract_if_zip(self, file_path: Path, extract_to: Path) -> None:
        if file_path.suffix == '.zip':
            # This is your existing unzip logic, only run for zip files
            os.makedirs(extract_to, exist_ok=True)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            logger.info(f"File extracted to: {extract_to}")
        else:
            # If it's not a zip (e.g., CSV), the extraction step is essentially complete
            logger.info(f"File {file_path} is not a zip; skipping extraction step.")
            # For a CSV, the data is now in local_data_file, which is the final path

    def initiate_data_ingestion(self) -> Path:
        # Step 1: Download or Copy the data
        ingested_file_path = self.download_or_copy_data()
        
        # Step 2: Extract the data (Only runs if it's a zip)
        self.extract_if_zip(ingested_file_path, self.config.unzip_dir)
        
        # We need to return the path to the actual CSV file.
        # Since you are likely copying a CSV file, the final data path is usually the local_data_file.
        return self.config.unzip_dir # If unzipped, or local_data_file if copied CSV