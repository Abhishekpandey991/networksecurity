import sys
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.data_transformation import DataTransformation

from networkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig



if __name__=="__main__":
  try:
    trainingpipelineconfig=TrainingPipelineConfig()
    dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
    data_ingestion=DataIngestion(dataingestionconfig)
    logging.info("Initiate the data ingestion")
    dataingestionartifact=data_ingestion.initiate_data_ingestion()
    logging.info("Data Initiation Completed")
    print(dataingestionartifact)
    

    datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
    data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
    logging.info("Initiate the data Validation")
    data_validation_artifact=data_validation.initiate_data_validation()
    logging.info("data Validation Completed")
    print(data_validation_artifact)


    datatransformationconfig=DataTransformationConfig(trainingpipelineconfig)
    data_transformation=DataTransformation(data_validation_artifact,datatransformationconfig)
    logging.info("Initiate the data Transformation")
    data_transformation_artifact=data_transformation.initiate_data_transformation()
    logging.info("data Transformation Completed")
    print(data_transformation_artifact)



  except Exception as e:
    raise NetworkSecurityException(e,sys)