import sys
import numpy as np
import pandas as pd



"""defining common constant variables for training pipeline """

TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "network_security_training_pipeline"
ARTIFACTS_DIR : str = "artifacts"

FILE_NAME : str = "phishingData.csv"

TRAINING_FILE_NAME : str = "training_file.csv"
TESTING_FILE_NAME : str = "testing_file.csv"



"""Data Ingestion constant variables"""

DATA_INGESTION_COLLECTION_NAME : str = "network_security_collection"
DATA_INGESTION_DATABASE_NAME : str = "network_security"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2