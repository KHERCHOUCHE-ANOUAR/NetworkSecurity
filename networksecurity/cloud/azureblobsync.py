import os

class AzureBlobSync:
    def sync_folder_to_blob(self, folder, container_url):
        command = f"azcopy sync '{folder}' '{container_url}' --recursive"
        os.system(command)

    def sync_folder_from_blob(self, folder, container_url):
        command = f"azcopy sync '{container_url}' '{folder}' --recursive"
        os.system(command)
