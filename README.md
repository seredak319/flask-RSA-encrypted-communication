# Encrypted Communication Flask Project

## Overview

This project demonstrates a simple encrypted communication system using RSA encryption between clients and a server. The server is implemented in Flask, and clients can securely exchange messages using public and private keys for encryption and decryption.

## Components

### Server

The server is implemented using Flask and provides endpoints for key exchange and secure message communication. It manages public keys for clients and facilitates secure communication between them.

### Client

#### Client A

1. **Key Exchange (ClientA)**:
    - ClientA uses generated pair of RSA keys (public and private).
    - The public key is stored in a file (`clientA.pub`) and is sent to the server for registration.

    ```python
    from rsa_server_client.client.client import Client

    client_name = 'ClientA'
    
    with open('clientA.pub', 'r') as file:
        public_key = file.read()

    client = Client("http://127.0.0.1:5000")
    response = client.send_key(client_name, public_key.encode())
    ```

2. **Secure Message Exchange (ClientB to ClientA)**:
    - ClientA retrieves the public key of ClientB from the server.
    - ClientA encrypts a message with the received key and sends the encrypted message to ClientB.

    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from rsa_server_client.client.client import Client

    client_name = 'ClientA'
    
    client = Client("http://127.0.0.1:5000")
    public_key = client.get_key(client_name)

    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(b"Message from ClientB to ClientA")

    client.send_binary_message(client_name, encrypted)
    ```

3. **Message Decryption (ClientA)**:
    - ClientA retrieves an encrypted message from the server.
    - ClientA decrypts the message using its private key.

    ```python
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from rsa_server_client.client.client import Client

    client_name = 'ClientA'

    with open("clientA", "r") as file:
        private_key = file.read()

    client = Client("http://127.0.0.1:5000")
    encrypted_message = client.get_binary_message(client_name)

    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message)

    print(decrypted_message)
    ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/encrypted-communication-flask.git
   cd flask-RSA-encrypted-communication
   ```
2. Install required dependencies:
 
   ```bash
   pip install -r requirements.txt
   ```

3. Run application:
 
   ```bash
   cd flask-RSA-encrypted-communication/server
   flask run --host=0.0.0.0
   ```

### Or use start.sh after fetching project to do it automatically :)

## Communication Simulation

Simulate the key exchange, secure message exchange, and message decryption processes step by step using the provided client scripts.

   ```bash
   cd client
   python clientA/processClientA_step1.py
   python clientB/processClientB_step2.py
   python clientA/processClientA_step3.py
   ```




