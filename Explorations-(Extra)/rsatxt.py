import string

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def modinverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        return x1 + m0
    else:
        return x1

def text_to_numeric(text):
    return [ord(char) for char in text]

def numeric_to_text(numeric_values):
    return ''.join([chr(value) for value in numeric_values])

p = int(input("enter p: "))
q = int(input("enter q: "))

n = p * q
phi = (p - 1) * (q - 1)

possibleE = [e for e in range(2, min(1001, phi)) if gcd(e, phi) == 1]

print(f"list of possible e values (upto 1000): {possibleE}")

invalidE = True
while invalidE:
    chosenE = int(input("choose an e: "))
    if chosenE in possibleE:
        invalidE = False

d = modinverse(chosenE, phi)

publickey = (n, chosenE)
privatekey = (n, d)

print("chosen e: ", chosenE)
print("calculated d: ", d)

plain_text = input("enter plain text: ")
numeric_plain_text = text_to_numeric(plain_text)

cipher_text = [(char**chosenE) % n for char in numeric_plain_text]
print("Cipher text: ", cipher_text)

decrypted_text = [(char**d) % n for char in cipher_text]
decrypted_plain_text = numeric_to_text(decrypted_text)
print("Decrypted text: ", decrypted_plain_text)
