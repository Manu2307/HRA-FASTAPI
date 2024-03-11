import os
import dotenv
dotenv.load_dotenv()


DB_URL = os.environ.get('DB_URL')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
DB_DRIVER = os.environ.get('DB_DRIVER')

SQLALCHEMY_DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
