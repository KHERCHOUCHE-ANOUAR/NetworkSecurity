from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfigEntity, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact, DataTransformationArtifact
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
import sys






if __name__ == "__main__":
    logging.info("Logging is working")
    try:
        training_pipeline_config = TrainingPipelineConfigEntity()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact: DataIngestionArtifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
        )
        data_validation_artifact: DataValidationArtifact = data_validation.initiate_data_validation()
        logging.info(f"Data validation artifact: {data_validation_artifact}")
        data_transformation_config =  DataTransformationConfig(training_pipeline_config)
        
        data_transformation = DataTransformation(
            data_validation_artifact=data_validation_artifact,
            data_transformation_config=data_transformation_config
        )
        data_transformation_artifact: DataTransformationArtifact = data_transformation.initiate_data_transformation()
        logging.info(f"Data transformation artifact: {data_transformation_artifact}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

