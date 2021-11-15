import os

class Config:

    
    SQLALCHEMY_DATABASE_URI = 'postgresql://qpbzntypxoxtru:d697aeba98bca2a973554ab25e8617bb45086902792925fa1add4d9eedd0688e@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d1v1hl204cn7cu'

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-school:12345@localhost/blogs'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ('kimutaiamos82@gmail.com')
    MAIL_PASSWORD = ('12345')
    SECRET_KEY= ('54a12f8986b077954dcf2ad7f14d07ae')
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
    SQLALCHEMY_DATABASE_URI = ('postgresql://qpbzntypxoxtru:d697aeba98bca2a973554ab25e8617bb45086902792925fa1add4d9eedd0688e@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d1v1hl204cn7cu')



class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql://qpbzntypxoxtru:d697aeba98bca2a973554ab25e8617bb45086902792925fa1add4d9eedd0688e@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d1v1hl204cn7cu'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost/blogs"

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}