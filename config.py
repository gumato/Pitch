import os

class Config:
    SECRET_KEY = 'gumeshi1'
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pricilla:715385641@localhost/pitch'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    
