import os
from box.exceptions import BoxValueError
import yaml
from mlproj import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.
    Args:
        filepath (Path): The path to the YAML file. 
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """ 

    try:
        with open(filepath, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {filepath} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        logger.error(f"Error reading YAML file: {filepath}. Error: {e}")
        raise e
    
@ensure_annotations
def write_yaml(filepath: Path, content: ConfigBox) -> None:
    """Writes a ConfigBox object to a YAML file.
    Args:
        filepath (Path): The path to the YAML file.
        content (ConfigBox): The content to write to the YAML file.
    """
    try:
        os.makedirs(filepath.parent, exist_ok=True)
        with open(filepath, 'w') as yaml_file:
            yaml.dump(dict(content), yaml_file)
            logger.info(f"YAML file: {filepath} written successfully")
    except Exception as e:
        logger.error(f"Error writing YAML file: {filepath}. Error: {e}")
        raise e   
    
@ensure_annotations
def create_directory(path_to_directory: Path) -> None:
    """Creates a directory if it does not exist.
    Args:
        path_to_directory (Path): The path to the directory to create.
    """
    try:
        os.makedirs(path_to_directory, exist_ok=True)
        logger.info(f"Directory created at: {path_to_directory}")
    except Exception as e:
        logger.error(f"Error creating directory at: {path_to_directory}. Error: {e}")
        raise e
        
@ensure_annotations
def save_json(filepath: Path, data: Any) -> None:
    """Saves data to a JSON file.
    Args:
        filepath (Path): The path to the JSON file.
        data (Any): The data to save to the JSON file.
    """
    try:
        os.makedirs(filepath.parent, exist_ok=True)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"JSON file: {filepath} saved successfully")
    except Exception as e:
        logger.error(f"Error saving JSON file: {filepath}. Error: {e}")
        raise e

@ensure_annotations
def load_json(filepath: Path) -> Any:
    """Loads data from a JSON file.
    Args:
        filepath (Path): The path to the JSON file. 
    Returns:
        Any: The data loaded from the JSON file.
    """ 
    try:
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"JSON file: {filepath} loaded successfully")
            return data
    except Exception as e:
        logger.error(f"Error loading JSON file: {filepath}. Error: {e}")
        raise e
    
@ensure_annotations
def save_bin(filepath: Path, data: Any) -> None:
    """Saves data to a binary file using joblib.
    Args:
        filepath (Path): The path to the binary file.
        data (Any): The data to save to the binary file.
    """
    try:
        os.makedirs(filepath.parent, exist_ok=True)
        joblib.dump(data, filepath)
        logger.info(f"Binary file: {filepath} saved successfully")
    except Exception as e:
        logger.error(f"Error saving binary file: {filepath}. Error: {e}")
        raise e

@ensure_annotations
def load_bin(filepath: Path) -> Any:
    """Loads data from a binary file using joblib.
    Args:
        filepath (Path): The path to the binary file.
    Returns:
        Any: The data loaded from the binary file.
    """ 
    try:
        data = joblib.load(filepath)
        logger.info(f"Binary file: {filepath} loaded successfully")
        return data
    except Exception as e:
        logger.error(f"Error loading binary file: {filepath}. Error: {e}")
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.
    Args:
        path (Path): The path to the file.  
    Returns:
        str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"Size of file: {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB" 