from waterpurity.config.configuration import ConfigurationManager
from waterpurity.components.data_ingestion import DataIngestion
from waterpurity import logger
import os
from pathlib import Path
STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()

if __name__ == '__main__':
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        os.chdir(Path(__file__).parents[3])
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e