from dotenv import load_dotenv
import os

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY") # Key env check

if NASA_API_KEY:
    print("Key found")
else:
    print("Key not found")