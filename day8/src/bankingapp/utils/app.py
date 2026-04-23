#test mongodb connection
import sys
import os
 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
 
from bankingapp.configuration.conf import Config
if __name__ == "__main__":
    config = Config()
collection=config.db.create_collection("accounts")
collection.insert_one({"account_no": 1234, "balance": 1000.0})
print(config.db.list_collection_names())
print(collection.find_one({"account_no": 1234}))
 