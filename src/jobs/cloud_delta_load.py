from src.ingestion.nasa_extractor import NasaExtractor
extractor = NasaExtractor()
data = extractor.get_delta_neos()
extractor.upload_delta_data(data)