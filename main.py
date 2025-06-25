from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfigEntity
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import sys






if __name__ == "__main__":
    logging.info("Logging is working")
    try:
        training_pipeline_config = TrainingPipelineConfigEntity()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact: DataIngestionArtifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
