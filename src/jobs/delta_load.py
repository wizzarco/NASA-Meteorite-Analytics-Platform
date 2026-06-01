from src.ingestion.nasa_extractor import NasaExtractor
extractor = NasaExtractor()
data = extractor.get_daily_neos()
extractor.save_delta_data(data)