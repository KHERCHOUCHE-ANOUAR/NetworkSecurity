
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


load_dotenv()

uri = os.getenv('URI')


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    def csv_to_json_convertor(self, csv_file):
        try:
            df = pd.read_csv(csv_file)
            df.reset_index(drop=True,inplace=True)

            json_data = list(json.loads(df.T.to_json()).values())
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def push_data_to_mongo(self, json_data, database, collection_name):
        try:
            self.databese = database
            self.collection_name = collection_name
            self.record = json_data

            self.mongo_client=pymongo.MongoClient(uri, tlsCAFile=certifi.where())
            self.database = self.mongo_client[self.databese]  
            self.collection = self.database[self.collection_name]
            self.collection.insert_many(self.record)
            logging.info(f"Data pushed to MongoDB collection: {self.collection_name} in database: {self.databese}")
            return True
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    try:
        logging.info("Logging is working")
        network_data = NetworkDataExtract()
        json_data = network_data.csv_to_json_convertor("/home/anouar/Desktop/networksecurity/Network_Data/phisingData.csv")
        network_data.push_data_to_mongo(json_data, "network_security", "network_security_collection")
    except Exception as e:
        raise NetworkSecurityException(e, sys)