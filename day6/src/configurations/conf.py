#read env from dotenv import load_doten
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    def __init__(self):
        self.url = os.getenv('url')
