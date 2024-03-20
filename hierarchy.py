import os
from pathlib import Path

import logging.config

MY_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s - [%(levelname)s] - %(message)s (%(filename)s:%(lineno)d)'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
    },
    'loggers': {
        'waterpurityLogger': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(MY_LOGGING_CONFIG)
logger = logging.getLogger('waterpurityLogger')
# File hierarchy 
project_name = "waterpurity"
file_hierarchy = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "application.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebook/eda.ipynb",
    "templates/index.html",
    "test.py"
]

# Making directories and files
for filepath in file_hierarchy:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Creating directory; {filedir} for the file: {filename}")
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logger.info(f"Creating empty file: {filepath}")
    elif filepath.is_file():
        logger.info(f"{filename} already exists")
