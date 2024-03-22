import os
from waterpurity import logger
from waterpurity.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    import pandas as pd

    def validate_schema_conformity(self) -> bool:
        """
            Validate the schema conformity of the input data file.

            This function checks if all the columns present in the input data file
            are part of the expected schema defined in the configuration. It reads
            the data file specified in the configuration, compares the columns in
            the data with the keys in the schema dictionary, and performs the
            following steps:

            1. If any column in the data is not present in the schema, it logs an
               error message with the missing columns, writes the validation status
               (False) to the status file, and returns False.

            2. If all columns in the data are present in the schema, it logs a
               success message, writes the validation status (True) to the status
               file, and returns True.

            The validation status is also written to a status file specified in the
            configuration for further reference.

            Args:
                None

            Returns:
                bool: True if the schema validation is successful, False otherwise.

            Raises:
                Exception: If any exception occurs during the validation process,
                           it logs the error message and re-raises the exception.
            """
        try:
            logger.info(f"Validating schema conformity for file: {self.config.data_filepath}")
            data = pd.read_csv(self.config.data_filepath)
            all_cols = set(data.columns)
            schema_cols = set(self.config.schema_dict.keys())

            if not all_cols.issubset(schema_cols):
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
                logger.error(f"Schema validation failed. Missing columns: {', '.join(all_cols - schema_cols)}")
                return validation_status

            validation_status = True
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            logger.info(f"Schema validation successful.")

            return validation_status

        except Exception as e:
            logger.error(f"Error occurred during schema validation: {str(e)}")
            raise e


