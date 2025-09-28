import os
import urllib
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Variables de entorno
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = urllib.parse.quote(os.getenv("MONGO_PASSWORD"))
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")

# URI de MongoDB
MONGO_URI = (
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Cluster0"
)

# Certificados
ca = certifi.where()

def db_connection():
    """Conectar a MongoDB y devolver la base de datos."""
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client[MONGO_DB]
        print("Database connection successful")
        return db
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
