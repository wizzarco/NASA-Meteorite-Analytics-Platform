from src.ingestion.nasa_extractor import NasaExtractor
from src.storage.parquet_writer import ParquetWriter

extractor = NasaExtractor()
writer = ParquetWriter()
data = extractor.get_near_earth_objects()

writer.save(data)