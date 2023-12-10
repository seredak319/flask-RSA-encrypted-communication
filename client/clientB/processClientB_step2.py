from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from rsa_server_client.client.client import Client

# Step 2.1 - get public key

# Client name who send the public key to the server
client_name = 'ClientA'

# Server IP and port
client = Client("http://127.0.0.1:5000")

# Receive clientA's key from the server
public_key = client.get_key(client_name)
print(f'Received {client_name} key is {public_key}')

# Step 2.2 - encrypt with received key

key = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(key)
encrypted = cipher.encrypt(b"Message from ClientB to ClientA")

# Step 2.3 - send encrypted message

client.send_binary_message(client_name, encrypted)
