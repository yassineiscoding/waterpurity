import os
import logging
from pathlib import Path
from waterpurity.components.data_preprocessing import DataPreprocessing
from waterpurity.config.configuration import ConfigurationManager
from waterpurity import logger

STAGE_NAME = "Data Preprocessing"


class DataPreprocessingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            logging.info(f"Data validation status: {status}")

            if status == "True":
                config = ConfigurationManager()
                data_preprocessing_config = config.get_data_preprocessing_config()
                data_preprocessing = DataPreprocessing(config=data_preprocessing_config)
                data_preprocessing.scale_and_split()

            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            logging.error(str(e))


if __name__ == '__main__':
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        os.chdir(Path(__file__).parents[3])
        obj = DataPreprocessingPipeline()
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e
