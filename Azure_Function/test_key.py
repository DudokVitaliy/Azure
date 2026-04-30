from key_vault_service import KeyVaultService

vault_url = "https://my-keyvault-123.vault.azure.net/"

kv = KeyVaultService(vault_url)

connection_string = kv.get_secret("StorageConnectionString")

print(connection_string)