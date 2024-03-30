import os
from pathlib import Path
from waterpurity import logger
from waterpurity.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from waterpurity.pipeline.data_validation_pipeline import DataValidationPipeline
from waterpurity.pipeline.data_preprocessing_pipeline import DataPreprocessingPipeline
from waterpurity.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from waterpurity.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

stages = {
    "Data Ingestion": DataIngestionPipeline(),
    "Data Validation": DataValidationPipeline(),
    "Data Preprocessing": DataPreprocessingPipeline(),
    "Model Trainer": ModelTrainerPipeline(),
    "Model Evaluation": ModelEvaluationPipeline()
}

for STAGE_NAME, pipeline in stages.items():
    try:
        logger.info(f"============= Starting {STAGE_NAME} stage ==============")
        obj = pipeline
        obj.main()
        logger.info(f"======= {STAGE_NAME} stage completed successfully ======")
    except Exception as e:
        logger.error(f"An error occurred during {STAGE_NAME} stage", exc_info=True)
        raise e
