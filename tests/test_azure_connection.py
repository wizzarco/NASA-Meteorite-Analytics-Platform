from src.storage.azure_blob_client import AzureBlobClient

client = AzureBlobClient()
containers = client.blob_service_client.list_containers()

for container in containers:
    print(container["name"])