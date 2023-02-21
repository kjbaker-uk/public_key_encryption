from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes


# Load the private key from the PEM file
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# Load the encrypted data from a file
with open('encrypted.bin', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data using the private key
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Write the decrypted data to a file
with open('decrypted_data.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)
