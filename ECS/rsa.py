#user inputs 2 prime numbers
#(check not same) phi of n
#all possible values of E
#user chooses one e
#enter plain text
#display cipher text and then plaintext again
#find time complexity

def gcd(a,b):
	if a==0:
		return b
	return(gcd(b%a, a))

def modinverse(a,m):
	m0, x0, x1 = m, 0, 1
	while a>1:
		q = a//m
		m, a = a%m, m
		x0, x1 = x1 - q*x0, x0
	if x1<0:
		return x1 + m0
	else:
		return x1

p = int(input("enter p: "))
q = int(input("enter q: "))

n = p*q
phi = (p-1)*(q-1)

possibleE = [e for e in range(2, min(1001, phi)) if gcd(e, phi) == 1]

print(f"list of possible e values (upto 1000): {possibleE}")
InvalidE = True
while InvalidE:
	chosenE = int(input("choose an e: "))
	if chosenE in possibleE:
		InvalidE = False

d = modinverse(chosenE, phi)

publickey = (n, chosenE)
privatekey = (n, d)

print("chosen e: ", chosenE)
print("calculated d: ", d)

plain_text = int(input("enter plain text: "))

cipher_text = (plain_text**chosenE)%n
print("Cipher text: ", cipher_text)

decrypted_text = (cipher_text**d)%n
print("Decrypted text: ", decrypted_text)