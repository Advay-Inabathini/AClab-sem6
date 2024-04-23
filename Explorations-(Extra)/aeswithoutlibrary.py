def pad(x, y):
    while len(x) > y:
        x = x[:-1]
    while len(x) < y:
        x += ' '
    return x

def hexify(x):
    return [format(ord(i), '02x') for i in x]

def add_round_key(x, y):
    new_state = []
    for i in range(len(y)):
        new_state.append(format(int(x[i], 16) ^ int(y[i], 16), '02x'))
    return new_state

def shift_rows(x):
    x1 = x[:4]
    for j in range(4, 16, 4):
        i = j // 4
        x1 += x[j + i:j + 4] + x[j:j + i]
    return x1

def mix_cols(x):
    x1 = [int(i, 16) for i in x]
    c_mat = [
        2, 3, 1, 1,
        1, 2, 3, 1,
        1, 1, 2, 3,
        3, 1, 1, 2
    ]
    ar = [0] * 16

    for i in range(4):
        for j in range(4):
            for k in range(4):
                ar[i * 4 + j] ^= x1[i * 4 + k] * c_mat[k * 4 + j]

    ar = [format(i % 256, '02x') for i in ar]
    return ar

def aes(input_str, key_str):
    pt = hexify(pad(input_str, 16))
    key = hexify(pad(key_str, 16))
    ct = add_round_key(pt, key)

    for _ in range(9):
        ct = shift_rows(ct)
        ct = mix_cols(ct)
        ct = add_round_key(ct, key)

    # Last round without MixCols
    ct = shift_rows(ct)
    ct = add_round_key(ct, key)

    return ''.join(i for i in ct)

# Example usage
input_text = input("Enter Plain Text: ")
key_text = input("Enter Key: ")
cipher_text = aes(input_text, key_text)
print("Cipher Text:", cipher_text)
