import time


def pad(x, y):
    while len(x) < y:
        x = "0" + x
    return x

def binarize(x, x1=""):
    temp = pad(bin(int(x, 16)).zfill(4)[2:], 4)
    for i in range(len(temp)):
        if i % 4 == 0 and i != 0:
            x1 += temp[i] + temp[i - 1]
        x1 += temp[i]
    return temp[len(temp) - 1] + x1 + temp[0]

def Cyclic_Shift(x, i):
    return x[i:] + x[:i]

def XOR(x, y, tmp=""):
    for i in range(len(y)):
        tmp += str(int(x[i]) ^ int(y[i]))
    return tmp

KEY = input("Enter Key: ")
t1 = time.time()
with open("hex_file.txt", "r") as f:
    with open("SDESEncrypted.txt", "w") as f2:
        for i in f.readlines():
            p = pad(i.strip(), 2)
            # print(p)
            L = bin(int(p, 16))[2:]
            # print(L,"\tL")
            K = pad(KEY, 10)
            # print(K)
            K = K[2] + K[4] + K[1] + K[6] + K[3] + K[9] + K[0] + K[8] + K[7] + K[5]
            K1 = Cyclic_Shift(K[:5], 1) + Cyclic_Shift(K[5:], 1)
            K1 = K1[5] + K1[2] + K1[6] + K1[3] + K1[7] + K1[5] + K1[9] + K1[8]
            # print("Key 1 = ",K1)
            K2 = Cyclic_Shift(K[:5], 2) + Cyclic_Shift(K[5:], 2)
            K2 = K2[5] + K2[2] + K2[6] + K2[3] + K2[7] + K2[5] + K2[9] + K2[8]
            # print("Key 2 = ",K2)
            CT = XOR(XOR(L, K1), K2)
            # print("Cipher Text = ",CT)
            f2.write(CT + "\n")
            # print("Decrypted Text = ",XOR(XOR(CT,K2),K1))
print("Exec Time: ", time.time() - t1)