from src.ingestion.nasa_extractor import NasaExtractor
extractor = NasaExtractor()

data = extractor.get_near_earth_objects()

print(data.keys())
extractor.save_bronze_data(data)