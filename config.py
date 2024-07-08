import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/rh_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
