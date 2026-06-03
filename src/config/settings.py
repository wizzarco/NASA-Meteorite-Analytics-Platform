from dotenv import load_dotenv
import os

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY") # Key env check

AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
AZURE_STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY")

# check both key
if NASA_API_KEY:
    print("Nasa API Key found")
else:
    print("Nasa API Key not found")

if AZURE_STORAGE_KEY:
    print("Azure Storage Key found")
else:
    print("Azure Storage Key not found")