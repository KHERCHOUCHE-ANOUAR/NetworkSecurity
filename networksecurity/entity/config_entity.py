from datetime import datetime
import os
from networksecurity.constant import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACTS_DIR)


class TrainingPipelineConfigEntity:
    def __init__(self, timestamp=datetime.now()):
        self.timestamp: str = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifacts_name: str = training_pipeline.ARTIFACTS_DIR
        self.artifacts_dir: str = os.path.join(self.artifacts_name, self.timestamp)


class DataIngestionConfig:
    def __init__(self, training_pipeline_config_entity: TrainingPipelineConfigEntity):
        
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config_entity.artifacts_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
        )
        self.feature_store_file_name: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAINING_FILE_NAME
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TESTING_FILE_NAME
        )
        self.data_ingestion_train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.data_ingestion_collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.data_ingestion_database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME