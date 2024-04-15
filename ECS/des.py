def pad(x, y):
    while len(x) < y:
        x = '0' + x
    return x

def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    return pad(binary_string, 4 * len(hex_string))

def binarize(x, x1=''):
    temp = pad(hex_to_binary(x)[2:], 32)
    for i in range(len(temp)):
        if i % 4 == 0 and i != 0:
            x1 += temp[i] + temp[i - 1]
        x1 += temp[i]
    return temp[len(temp) - 1] + x1 + temp[0]

def XOR(x, y, tmp=''):
    for i in range(len(y)):
        tmp += str(int(x[i]) ^ int(y[i]))
    return tmp

p = pad(input("Enter Plain Text: "), 16)
L, R = binarize(p[:8]), binarize(p[8:])
K = pad(hex_to_binary(input("Enter Key: "))[2:], 48)

for i in range(16):
    L1, R1 = R, XOR(L, XOR(R, K))
    L, R = L1, R1
    K = K[6:] + '110010'

L, R = ''.join(L[i:i + 4] for i in range(1, len(L) - 1, 6)), ''.join(R[i:i + 4] for i in range(1, len(R) - 1, 6))

cipher_text = hex(int(L, 2))[2:] + hex(int(R, 2))[2:]
print("Cipher Text:", cipher_text)
