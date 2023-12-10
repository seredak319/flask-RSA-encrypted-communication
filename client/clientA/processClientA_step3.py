from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from rsa_server_client.client.client import Client

client_name = 'ClientA'

# Step 3.1 - get private key
with open("clientA", "r") as file:
    private_key = file.read()

# Server IP and port
client = Client("http://127.0.0.1:5000")

# Get message
encrypted_message = client.get_binary_message(client_name)

print(f'Received encrypted message {encrypted_message}')

# Step 3.2 - encrypt with private key

key = RSA.import_key(private_key)
cipher = PKCS1_OAEP.new(key)
decrypted_message = cipher.decrypt(encrypted_message)

# Result

print(decrypted_message)
