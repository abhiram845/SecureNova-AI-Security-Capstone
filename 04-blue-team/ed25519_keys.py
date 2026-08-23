from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

print("=" * 70)
print("PROJECT 4 - BLUE TEAM")
print("ED25519 KEY PAIR GENERATION")
print("=" * 70)

# Generate Ed25519 private key
private_key = ed25519.Ed25519PrivateKey.generate()

# Get public key
public_key = private_key.public_key()

# Save private key
with open("ed25519_private.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Save public key
with open("ed25519_public.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("\nEd25519 key pair generated successfully.")
print("Private key file: ed25519_private.pem")
print("Public key file : ed25519_public.pem")

print("\nFILES CREATED:")
print("-" * 70)
print("✓ ed25519_private.pem")
print("✓ ed25519_public.pem")
print("\nKEY GENERATION STATUS: SUCCESS")