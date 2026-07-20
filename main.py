import sys
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
from networkSecurity.components.data_validation import DataValidation


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


  except Exception as e:
    raise NetworkSecurityException(e,sys)