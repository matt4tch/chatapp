from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')