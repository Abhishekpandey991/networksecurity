import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd
import pymongo
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

class NetworkDataExtract():
  def __init__(self):
    try:
      pass
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    

  def cv_to_json_conversion(self,file_path):
    try:
      data=pd.read_csv(file_path)
      data.reset_index(drop=True,inplace=True)
      records=list(json.loads(data.T.to_json()).values())
      return records
    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
  def insert_data_mongodb(self,records,database,collection):
    try:
      self.records=records
      self.collection=collection
      self.database=database
      self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
      self.database=self.mongo_client[self.database]
      self.collection=self.database[self.collection]
      self.collection.insert_many(self.records)

      return len(self.records)


    except Exception as e:
      raise NetworkSecurityException(e,sys)
    
    
if __name__=="__main__":
  FILE_PATH="Network_Data\phisingData.csv"
  DATABASE="Abhishek"
  COLLECTION="NetworkData"
  network=NetworkDataExtract()
  records=network.cv_to_json_conversion(FILE_PATH)
  print(records)
  no_of_record=network.insert_data_mongodb(records=records,database=DATABASE,collection=COLLECTION)
  print(no_of_record)


