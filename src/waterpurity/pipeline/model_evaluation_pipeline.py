import os
from pathlib import Path
from waterpurity.components.model_evaluation import ModelEvaluation
from waterpurity.config.configuration import ConfigurationManager
from waterpurity import logger

STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        os.chdir(Path(__file__).parents[3])
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e
