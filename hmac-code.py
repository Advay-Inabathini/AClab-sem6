import hashlib

def hmac_sha256(key, message):
    # Convert the key and message to bytes if they are not already
    key = bytes(key, 'utf-8') #if not isinstance(key, bytes) else key
    message = bytes(message, 'utf-8') #if not isinstance(message, bytes) else message

    # Pad the key if it is longer than the block size
    block_size = 64
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    key_padding = key + (b'\x00' * (block_size - len(key)))

    # Calculate the inner and outer paddings
    inner_padding = bytes(c ^ 0x36 for c in key_padding)
    outer_padding = bytes(c ^ 0x5c for c in key_padding)

    # Calculate the HMAC
    inner_hash = hashlib.sha256(inner_padding + message).digest()
    hmac = hashlib.sha256(outer_padding + inner_hash).hexdigest()

    return hmac

# Example usage
secret_key = input("enter secret key: ")
message = input("enter message: ")

hmac_digest = hmac_sha256(secret_key, message)
print(f'HMAC digest: {hmac_digest}')

#claude