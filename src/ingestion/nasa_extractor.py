import requests
import json
from pathlib import Path
from datetime import datetime
from src.config.settings import NASA_API_KEY

class NasaExtractor:
    BASE_URL = "https://api.nasa.gov"
    def get_near_earth_objects(self):
        today = datetime.now().strftime("%Y-%m-%d")
        url = (
            f"{self.BASE_URL}/neo/rest/v1/feed"
            f"?start_date={today}"
            f"&end_date={today}"
            f"&api_key={NASA_API_KEY}"
        )

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    def save_bronze_data(self, data):
        bronze_folder = Path("data/bronze")
        bronze_folder.mkdir(parents=True, exist_ok=True)
        file_name = f"{datetime.now().strftime('%Y-%m-%d')}.json"
        file_path = bronze_folder / file_name
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"File saved: {file_path}")