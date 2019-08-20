import os

class DevelopmentConfig:

  # Flask
  DEBUG = True

  # SQLAlchemy
  # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://UUU:PPP@HHH/DDD?charset=utf8mb4' # in instance
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False

  # Japanese in JSONify
  JSON_AS_ASCII = False

Config = DevelopmentConfig
