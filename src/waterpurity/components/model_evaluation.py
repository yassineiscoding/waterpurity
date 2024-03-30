import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from waterpurity.entity.config_entity import ModelEvaluationConfig
from waterpurity.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluation_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1).values
        y_test = test_data[[self.config.target_column]].squeeze()

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predictions = model.predict(X_test)
            (rmse, mae, r2) = self.evaluation_metrics(y_test, predictions)

            scores = {"RMSE": rmse, "MAE": mae, "R2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("RMSE", rmse)
            mlflow.log_metric("R2", r2)
            mlflow.log_metric("MAE", mae)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="waterpurityModel")
            else:
                mlflow.sklearn.log_model(model, "model")


