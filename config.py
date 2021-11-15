import os

class Config:

    
    exportSQLALCHEMY_DATABASE_URI='postgresql+psycopg2://{moringa-school}:{12345}@localhost/{blogs}'

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-school:12345@localhost/blogs'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY= os.environ.get('54a12f8986b077954dcf2ad7f14d07ae')
    SENDER_EMAIL = 'kimutaiamos82@gmail.com'
  
   #simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa-school:12345@localhost/blogs'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost/blogs"

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}