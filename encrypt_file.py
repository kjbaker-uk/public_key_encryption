from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Load the public key from a PEM file
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# Open the file you want to encrypt
with open('secret.txt', 'rb') as f:
    plaintext = f.read()

# Encrypt the file
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Write the encrypted data to a file
with open('encrypted.bin', 'wb') as f:
    f.write(ciphertext)
