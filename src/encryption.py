def xor_encrypt_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    key_length = len(key_bytes)
    return bytes([data[i] ^ key_bytes[i % key_length] for i in range(len(data))])

'''
def xor_encrypt_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    key_length = len(key_bytes)

    # Create a mutable bytearray of the same length as data
    result = bytearray(len(data))

    # Fill each position with plaintext_byte XOR key_byte
    for i in range(len(data)):
        plain_byte = data[i]
        key_byte   = key_bytes[i % key_length]
        result[i]  = plain_byte ^ key_byte

    # Convert bytearray back to immutable bytes
    return bytes(result)

'''
