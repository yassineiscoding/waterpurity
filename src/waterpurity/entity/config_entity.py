from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    data_filepath: Path
    schema_dict: dict


@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    data_filepath: Path
