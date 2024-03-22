import os
from pathlib import Path

from waterpurity.components.model_trainer import ModelTrainer
from waterpurity.config.configuration import ConfigurationManager
from waterpurity import logger

STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train_and_save_best_model()

if __name__ == '__main__':
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        os.chdir(Path(__file__).parents[3])
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e

