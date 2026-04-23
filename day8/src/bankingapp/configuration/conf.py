#create mongo db connection
import os
import sys
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
 
class Config:
    def __init__(self):
        self.client = MongoClient(os.getenv("conn_string"))
        self.db = self.client["bankingapp"]
 