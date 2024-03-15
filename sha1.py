
# Helper function: left rotate
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

# Helper function: prepare the message
def prepare_message(message):
    bits = ""
    for char in message:
        bits += '{0:08b}'.format(ord(char))
    bits += '1'
    bits += '0' * ((448 - len(bits) % 512) % 512)
    bits += '{0:064b}'.format(len(message) * 8)
    return bits

# Helper function: divide message into 32-bit words
def divide_into_words(message_bits):
    return [int(message_bits[i:i + 32], 2) for i in range(0, len(message_bits), 32)]

def sha1(data):
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0


    # Process the message
    message_bits = prepare_message(data)
    words = divide_into_words(message_bits)

    for i in range(0, len(words), 16):
        chunk = words[i:i + 16]
        w = chunk.copy()

        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + w[j] & 0xFFFFFFFF
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

# Example usage:
user_input = input("Enter the message to hash: ")
hashed_result = sha1(user_input)
print(f"SHA-1 Hash: {hashed_result}")