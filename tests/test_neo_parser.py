from src.ingestion.nasa_extractor import NasaExtractor
from src.transformation.neo_parser import NeoParser

extractor = NasaExtractor()
parser = NeoParser()

data = extractor.get_near_earth_objects()
records = parser.parse(data)
print(records[0])