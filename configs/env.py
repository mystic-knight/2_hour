import os
from dotenv import load_dotenv
load_dotenv()

APP_ENV=os.getenv("APP_ENV")

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT  = os.getenv("REDIS_PORT")
REDIS_USERNAME  = os.getenv("REDIS_USERNAME")
ENVIRONMENT_TYPE    = os.getenv("ENVIRONMENT_TYPE")
SECRET_KEY = os.getenv("SECRET_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
FIREBASE_AUTH_DOMAIN = os.getenv("FIREBASE_AUTH_DOMAIN")
FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")
FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET")
FIREBASE_MESSAGING_SENDER_ID = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
FIREBASE_APP_ID = os.getenv("FIREBASE_APP_ID")
FIREBASE_MEASUREMENT_ID = os.getenv("FIREBASE_MEASUREMENT_ID")