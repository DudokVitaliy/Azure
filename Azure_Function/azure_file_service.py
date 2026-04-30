from azure.storage.fileshare import ShareServiceClient
import os

class AzureFileService:
    def __init__(self, connection_string: str, share_name: str):
        self.service_client = ShareServiceClient.from_connection_string(connection_string)
        self.share_client = self.service_client.get_share_client(share_name)

    def create_directory(self, dir_path: str):
        dir_client = self.share_client.get_directory_client(dir_path)
        dir_client.create_directory()

    def delete_directory(self, dir_path: str):
        dir_client = self.share_client.get_directory_client(dir_path)

        for item in dir_client.list_directories_and_files():
            if item['is_directory']:
                self.delete_directory(f"{dir_path}/{item['name']}")
            else:
                file_client = dir_client.get_file_client(item['name'])
                file_client.delete_file()

        dir_client.delete_directory()

    def list_directory(self, dir_path: str):
        dir_client = self.share_client.get_directory_client(dir_path)
        return [item['name'] for item in dir_client.list_directories_and_files()]

    def download_directory(self, dir_path: str, local_path: str):
        os.makedirs(local_path, exist_ok=True)
        dir_client = self.share_client.get_directory_client(dir_path)

        for item in dir_client.list_directories_and_files():
            if item['is_directory']:
                self.download_directory(
                    f"{dir_path}/{item['name']}",
                    os.path.join(local_path, item['name'])
                )
            else:
                self.download_file(
                    f"{dir_path}/{item['name']}",
                    os.path.join(local_path, item['name'])
                )

def download_file(self, remote_file_path: str, local_file_path: str):
    file_client = self.share_client.get_file_client(remote_file_path)

    dir_name = os.path.dirname(local_file_path)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    with open(local_file_path, "wb") as f:
        data = file_client.download_file()
        f.write(data.readall())

    def download_file(self, remote_file_path: str, local_file_path: str):
        file_client = self.share_client.get_file_client(remote_file_path)

        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

        with open(local_file_path, "wb") as f:
            data = file_client.download_file()
            f.write(data.readall())

    def delete_file(self, remote_file_path: str):
        file_client = self.share_client.get_file_client(remote_file_path)
        file_client.delete_file()

    def rename_file(self, old_path: str, new_path: str):
        source_file = self.share_client.get_file_client(old_path)
        target_file = self.share_client.get_file_client(new_path)

        source_url = source_file.url

        target_file.start_copy_from_url(source_url)
        source_file.delete_file()