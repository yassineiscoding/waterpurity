from waterpurity.config.configuration import ConfigurationManager
from waterpurity.components.data_validation import DataValidation
from waterpurity import logger
import os
from pathlib import Path

STAGE_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_schema_conformity()


if __name__ == '__main__':
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        os.chdir(Path(__file__).parents[3])
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e
