import ecdsa
import bech32

# Create the Private Key
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
private_key_bytes = private_key.to_string()
print("Private Key: ", private_key_bytes.hex())

# Generate Public Key from Private Key
verifying_key = private_key.get_verifying_key()
public_key_compressed_bytes = verifying_key.to_string("compressed")
print("Public Key (Compressed): ", public_key_compressed_bytes.hex())

# Convert Compressed Public Key into a Radix Engine Address
readdr_bytes = b"\x04" + public_key_compressed_bytes

# Convert Radix Engine Address to Bech32 Radix Wallet Address
readdr_bytes5 = bech32.convertbits(readdr_bytes, 8, 5)
wallet_address = bech32.bech32_encode("rdx", readdr_bytes5)
print("Wallet Address: ", wallet_address)
