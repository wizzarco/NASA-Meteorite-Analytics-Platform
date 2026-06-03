import requests
import json
from pathlib import Path
from datetime import datetime
from src.config.settings import NASA_API_KEY
from src.storage.azure_blob_client import AzureBlobClient

class NasaExtractor:
    ### CONFIG ###
    @staticmethod
    def get_date():
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    BASE_URL = "https://api.nasa.gov"
    def __init__(self):
        self.azure_client = AzureBlobClient()

    ### DELTA ###
    def get_delta_neos(self):
        url = (
            f"{self.BASE_URL}/neo/rest/v1/feed"
            f"?start_date={self.get_date()}"
            f"&end_date={self.get_date()}"
            f"&api_key={NASA_API_KEY}"
        )
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    # DELTA SAVE LOCAL STORAGE
    def save_delta_data(self, data):
        delta_folder = Path("data/bronze/delta")
        delta_folder.mkdir(parents=True, exist_ok=True)
        file_name = f"neo_delta_{self.get_timestamp()}.json"
        file_path = delta_folder / file_name
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Delta file saved: {file_path}")

    # DELTA SAVE CLOUD STORAGE WITH AZURE
    def upload_delta_data(self, data):
        blob_name = (
            f"delta/neo_delta_{self.get_timestamp()}.json"
        )

        self.azure_client.upload_json(
            container_name="bronze",
            blob_name=blob_name,
            data=data
        )

    ### FULL ###
    def get_all_neos(self, max_pages=10): # Limit pages because we have to much data for my little storage :(
        all_neos = []
        page = 0
        while page < max_pages:
            url = (
                f"{self.BASE_URL}/neo/rest/v1/neo/browse"
                f"?page={page}"
                f"&size=20"
                f"&api_key={NASA_API_KEY}"
            )
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            all_neos.extend(data["near_earth_objects"])
            total_pages = data["page"]["total_pages"]
            if page >= total_pages - 1:
                break
            page += 1
        return all_neos

    # FULL SAVE LOCAL STORAGE
    def save_full_data(self, data):
        full_folder = Path("data/bronze/full")
        full_folder.mkdir(parents=True, exist_ok=True)
        file_name = f"neo_full_{self.get_timestamp()}.json"
        file_path = full_folder / file_name
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Full file saved: {file_path}")

    # FULL SAVE CLOUD STORAGE
    def upload_full_data(self, data):
        blob_name = (
            f"full/neo_full_{self.get_timestamp()}.json"
        )

        self.azure_client.upload_json(
            container_name="bronze",
            blob_name=blob_name,
            data=data
        )