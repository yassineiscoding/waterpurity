import os
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from waterpurity import logger
from waterpurity.entity.config_entity import DataPreprocessingConfig


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def scale_and_split(self):
        data = pd.read_csv(self.config.data_filepath)

        imputer = SimpleImputer(strategy='median').set_output(transform="pandas")
        data = imputer.fit_transform(data)
        logger.info("Imputed missing values with median")

        scaler = MinMaxScaler(feature_range=(0, 1)).set_output(transform="pandas")
        data_scaled = scaler.fit_transform(data)
        logger.info("Scaled data using MinMaxScaler")

        train, test = train_test_split(data_scaled, random_state=0)
        logger.info("Splitted data into training and test sets")
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Testing data shape: {test.shape}")

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info(f"Saved data to {self.config.root_dir}")
