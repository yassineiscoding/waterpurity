import os
from box.exceptions import BoxValueError
import yaml
from waterpurity import logger
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other exception occurs while reading the file.

    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        logger.error(f"Error reading YAML file '{path_to_yaml}': {e}")
        raise e


def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.

    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool, optional): Whether to log the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at '{path}'.")
        except Exception as e:
            logger.error(f"Error creating directory '{path}': {e}")


def save_json(path: Path, data: dict):
    """
    Save data as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at '{path}'.")
    except Exception as e:
        logger.error(f"Error saving JSON file '{path}': {e}")


def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from the JSON file as a ConfigBox object.
    """
    try:
        with open(path, 'r') as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from '{path}'.")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading JSON file '{path}': {e}")
        raise e


def save_bin(data: Any, path: Path):
    """
    Save data as a binary file.

    Args:
        data (Any): Data to be saved as a binary file.
        path (Path): Path to the binary file.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at '{path}'.")
    except Exception as e:
        logger.error(f"Error saving binary file '{path}': {e}")


def load_bin(path: Path) -> Any:
    """
    Load data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from '{path}'.")
        return data
    except Exception as e:
        logger.error(f"Error loading binary file '{path}': {e}")
        raise e


def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes, formatted as a string.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting size of file '{path}': {e}")
        raise e
