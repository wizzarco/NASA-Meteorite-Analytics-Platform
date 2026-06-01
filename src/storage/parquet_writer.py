import pandas as pd
import json
from pathlib import Path
from datetime import datetime

class ParquetWriter:
    def save(self, data):
        output_folder = Path("data/bronze")
        output_folder.mkdir(parents=True, exist_ok=True)
        file_name = f"{datetime.now().strftime('%Y-%m-%d')}.parquet"
        output_file = output_folder / file_name
        df = pd.DataFrame({
            "ingestion_timestamp": [datetime.now()],
            "payload": [json.dumps(data)]
        })
        df.to_parquet(output_file, index=False)
        
        print(f"Saved: {output_file}")