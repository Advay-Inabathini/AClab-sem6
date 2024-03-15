import struct

def md5_padding(message):
    original_bit_length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'
    message += b'\x00' * ((56 - len(message) % 64) % 64)
    message += struct.pack('<Q', original_bit_length)
    return message

def left_rotate(value, shift):
    return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))

def md5_process_chunk(chunk, h0, h1, h2, h3):
    constants = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
    shifts = [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21]

    def F(b, c, d): return (b & c) | (~b & d)
    def G(b, c, d): return (b & d) | (c & ~d)
    def H(b, c, d): return b ^ c ^ d
    def I(b, c, d): return c ^ (b | ~d)

    for i in range(0, len(chunk), 4):
        if i < 16:
            f, g = F(h1, h2, h3), i
        elif i < 32:
            f, g = G(h1, h2, h3), (5 * i + 1) % 16
        elif i < 48:
            f, g = H(h1, h2, h3), (3 * i + 5) % 16
        else:
            f, g = I(h1, h2, h3), (7 * i) % 16

        temp = h3
        h3 = h2
        h2 = h1
        h1 = (h1 + left_rotate((h0 + f + constants[i // 16] + int.from_bytes(chunk[i:i + 4], 'little')) & 0xFFFFFFFF, shifts[i % 16])) & 0xFFFFFFFF
        h0 = temp

    return h0, h1, h2, h3

def md5(message):
    h0, h1, h2, h3 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    message = md5_padding(message)

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        h0, h1, h2, h3 = md5_process_chunk(chunk, h0, h1, h2, h3)

    return struct.pack('<I', h0) + struct.pack('<I', h1) + struct.pack('<I', h2) + struct.pack('<I', h3)

# Example usage:
plaintext = input("enter plaintext:")
hashed_text = md5(plaintext.encode('utf-8'))
print(f"Plaintext: {plaintext}")
print(f"MD5 Hash: {hashed_text.hex()}")