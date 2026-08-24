from cryptography.hazmat.primitives.asymmetric import ed25519

print("=" * 70)
print("PROJECT 4 - BLUE TEAM")
print("AGENT MESSAGE SIGNATURE VERIFICATION")
print("=" * 70)

# Generate an Ed25519 key pair for this simulation
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# Original trusted agent message
message = b"APPROVED: Execute the requested agent operation."

# Sign the original message
signature = private_key.sign(message)

print("\nORIGINAL MESSAGE")
print("-" * 70)
print(message.decode())

print("\nSIGNATURE CREATED")
print("-" * 70)
print("Ed25519 signature generated successfully.")

# Verify the original message
try:
    public_key.verify(signature, message)
    print("Original message verification: SUCCESS")
except Exception:
    print("Original message verification: FAILED")

# Tamper with one character
tampered_message = b"APPROVED: Execute the requested agent operatioN."

print("\nTAMPERED MESSAGE")
print("-" * 70)
print(tampered_message.decode())

# Try verifying the tampered message using the original signature
print("\nSIGNATURE VERIFICATION")
print("-" * 70)

try:
    public_key.verify(signature, tampered_message)
    print("Tampered message verification: SUCCESS")
except Exception:
    print("STATUS: REJECTED")
    print("REASON: Signature verification failed.")
    print("SECURITY ACTION: Tampered message was not processed.")