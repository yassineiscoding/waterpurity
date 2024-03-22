import os
import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

from waterpurity.entity.config_entity import ModelTrainerConfig
from waterpurity import logger
from waterpurity.utils.common import write_yaml
from waterpurity.constants import PARAMS_FILE_PATH


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_and_save_best_model(self):

        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data.drop([self.config.target_column], axis=1).values
        X_test = test_data.drop([self.config.target_column], axis=1).values

        y_train = train_data[[self.config.target_column]].squeeze()
        y_test = test_data[[self.config.target_column]].squeeze()

        models = {
            'LogisticRegression': LogisticRegression(),
            'RandomForestClassifier': RandomForestClassifier(),
            'SVM': SVC(kernel='rbf'),
            'GaussianNB': GaussianNB(),
            'AdaBoostClassifier': AdaBoostClassifier()
        }

        params_path = PARAMS_FILE_PATH

        best_model = None
        best_accuracy = 0
        best_model_params = None

        for name, model in models.items():
            logger.info(f"Training {name}...")
            scores = cross_val_score(model, X_train, y_train, cv=5)
            mean_accuracy = scores.mean()
            logger.info(f" - {name} Cross-Validation Accuracy: {mean_accuracy:.2f}")

            if mean_accuracy > best_accuracy:
                best_accuracy = mean_accuracy
                best_model = model
                best_model.fit(X_train, y_train)
                y_pred = best_model.predict(X_test)
                test_accuracy = accuracy_score(y_test, y_pred)
                logger.info(f" - {name} Test Accuracy: {test_accuracy:.2f}")
                best_model_params = model.get_params()

        write_yaml(best_model_params, params_path)

        joblib.dump(best_model, os.path.join(self.config.root_dir, self.config.model_name))
