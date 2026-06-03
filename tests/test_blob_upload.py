from src.storage.azure_blob_client import AzureBlobClient

client = AzureBlobClient()

client.upload_json(
    container_name="bronze",
    blob_name="test.json",
    data={
        "message": "Hello Azure Blob"
    }
)