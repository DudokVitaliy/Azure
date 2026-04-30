from azure_file_service import AzureFileService
import os

connection_string =  os.getenv("AZURE_STORAGE_CONNECTION_STRING")

share_name = "myshare"

afs = AzureFileService(connection_string, share_name)

afs.create_directory("test-folder")

with open("local.txt", "w") as f:
    f.write("Hello Azure!")

afs.upload_file("local.txt", "test-folder/remote.txt")

print("Files:", afs.list_directory("test-folder"))

afs.download_file("test-folder/remote.txt", "downloaded.txt")

afs.rename_file("test-folder/remote.txt", "test-folder/new.txt")

afs.delete_file("test-folder/new.txt")


afs.delete_directory("test-folder")