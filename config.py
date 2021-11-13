from logging import DEBUG
import os
from flask import config

from flask_sqlalchemy import SQLAlchemy


class Config:
    """
    general configuration class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class prodConfig(Config):
    """
    production configuration child class
    Arghs:
         Config: The parent configuration class with general configuration settings
    """

    SQLAlchemy_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLAlchemy_DATABASE_URI.startswith("postgres://"):
        SQLAlchemy_DATABASE_URI = SQLAlchemy_DATABASE_URI.replace("postgres://", "postgresql://")


class TestConfig(Config):


    pass



class DevConfig(Config):
    """
    development configuration chilsd class
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-school@localhost/blog'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'productio':prodConfig,
    'test':TestConfig
}