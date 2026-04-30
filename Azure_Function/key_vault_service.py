from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultService:
    def __init__(self, vault_url: str):
        credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=vault_url, credential=credential)

    def get_secret(self, secret_name: str) -> str:
        secret = self.client.get_secret(secret_name)
        return secret.value
