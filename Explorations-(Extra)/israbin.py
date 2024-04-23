
def isprime(num):
	for i in range(2, int(num/2)+1):
		if (num%i) == 0:
			return False
	else:
		return True

n = int(input("enter number of digits: "))

for i in range(10**n, 100**n):
	if i%4 == 3 and isprime(i):
		print(i, end=" ")

