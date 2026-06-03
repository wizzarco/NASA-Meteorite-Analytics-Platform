from azure.storage.blob import BlobServiceClient
from src.config.settings import (AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_KEY)
import json

class AzureBlobClient:
    def __init__(self):
        account_url = (
            f"https://{AZURE_STORAGE_ACCOUNT}.blob.core.windows.net"
        )
        self.blob_service_client = BlobServiceClient(
            account_url=account_url,
            credential=AZURE_STORAGE_KEY
        )

    def upload_json(
        self,
        container_name,
        blob_name,
        data
    ):

        blob_client = self.blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_name
        )

        blob_client.upload_blob(
            json.dumps(data, indent=4),
            overwrite=True
        )

        print(
            f"Uploaded : {container_name}/{blob_name}"
        )