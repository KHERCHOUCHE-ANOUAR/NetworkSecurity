from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import sys
import os 
import numpy as np
from sklearn.model_selection import train_test_split
from typing import List
import pymongo

import pandas as pd




from dotenv import load_dotenv
load_dotenv()   


MONGO_DB_URI = os.getenv('URI')

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_dataframe(self):
        """ Export MongoDB collection as a Pandas DataFrame."""
        try:
            # Create a MongoDB client
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)

            # Access the specified database and collection
            collection = self.mongo_client[self.data_ingestion_config.data_ingestion_database_name][
                self.data_ingestion_config.data_ingestion_collection_name
            ]

            # Fetch all documents from the collection
            data = pd.DataFrame(list(collection.find()))
            if '_id' in data.columns.tolist():
                data.drop(columns=['_id'], axis=1)
            data.replace("na", np.nan, inplace=True)
            if data.empty:
                raise ValueError("No data found in the collection.")

            return data
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process...")

            # Export collection as DataFrame
            data = self.export_collection_as_dataframe()        

            logging.info("Data exported from MongoDB collection successfully.")
            data=self.export_data_to_feature_store(data)
            logging.info("Data exported to feature store successfully.")
            # Split the data into training and testing sets
            self.split_data_as_train_test(data)
            logging.info("Data split into training and testing sets successfully.")
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                            testing_file_path=self.data_ingestion_config.testing_file_path)
            logging.info("Data ingestion process completed successfully.")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_data_to_feature_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_name
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)

            logging.info(f"Feature store file created at: {feature_store_file_path}")
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.data_ingestion_train_test_split_ratio,
                random_state=42
            )

            logging.info("Data split into training and testing sets successfully.")

            directory = os.path.dirname(self.data_ingestion_config.training_file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Created directory for training and testing files: {directory}")

            # Save the train and test sets to CSV files
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Training data saved to: {self.data_ingestion_config.training_file_path}")
            logging.info(f"Testing data saved to: {self.data_ingestion_config.testing_file_path}")

        except Exception as e:
            raise NetworkSecurityException(e, sys)