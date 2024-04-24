import random
import time

def generators(n):
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            results.append(a)
    return results

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def elgamal_sign(message, private_key, p, g):
    while True:
        k = random.randint(1, p - 2)  # Generate a random k
        if gcd(k, p - 1) == 1:
            break  # k is relatively prime to p - 1, so we can use it

    r = pow(g, k, p)
    s = ((message - private_key * r) * pow(k, -1, p - 1)) % (p - 1)
    return r, s

def elgamal_verify(message, signature, public_key, p, g):
    r, s = signature
    v1 = pow(g, message, p)
    v2 = (pow(public_key, r, p) * pow(r, s, p)) % p
    return v1 == v2

# Example usage
p = int(input("Enter a prime number: "))
begin = time.time()

e1 = -1
for i in generators(p):
    if gcd(i, p) == 1:
        e1 = i
        break

d = random.randint(e1 + 1, p - 2)
e2 = pow(e1, d, p)

message = int(input("Enter the message (as an integer): "))

# Generate private and public keys
private_key = d
public_key = e2

# Sign the message
signature = elgamal_sign(message, private_key, p, e1)
print(f"Signature: {signature}")

# Verify the signature
if elgamal_verify(message, signature, public_key, p, e1):
    print("Signature is valid.")
else:
    print("Signature is invalid.")

end = time.time()
print(f"Total time of the program is {end - begin}")