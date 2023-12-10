from rsa_server_client.client.client import Client

# Client A
client_name = 'ClientA'

# Get public key
with open('clientA.pub', 'r') as file:
    public_key = file.read()

print("Client's A public key is: [" + public_key + "]")

# Server IP and port
client = Client("http://127.0.0.1:5000")

# Send key to the server
response = client.send_key(client_name, public_key.encode())
print(response)
