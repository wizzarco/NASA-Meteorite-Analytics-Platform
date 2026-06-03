from src.ingestion.nasa_extractor import NasaExtractor
extractor = NasaExtractor()
data = extractor.get_all_neos()
extractor.upload_full_data(data)