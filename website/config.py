from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TESTING = os.getenv('TESTING')
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')