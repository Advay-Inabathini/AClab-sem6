def mod_inv(x,y):
	for i in range (y):
		if (x*i)%y ==1 :
			return i
         		
def pointDoubling(x1,y1, a, p, k):
	Ln = 3*x1*x1 + a
	Ld = 2*y1
	L = (Ln%p*mod_inv(Ld,p))
	x2 = (L*L - 2*x1)%p
	y2 = (L*(x1 - x2) - y1)%p
	i = 0
			
	while i < k-2:
		L = (y2 - y1)%p * mod_inv((x2 - x1),p)
		x3 = (L*L - x1- x2)%p
		y3 = (L*(x2 - x3) - y2)%p
		x1 = x2
		x2 = x3
		y1 = y2
		y2 = y3
		i += 1
	return x2, y2

a,b = [int(i) for i in input("Enter a,b of y^2 = x^3 + a*x + b :").split()]
x1,y1 = [int(i) for i in input("Enter base point:").split()]
d = int(input("Enter d: "))
k = int(input("Enter k: "))
p = int(input("Enter prime number: "))
Px,Py = [int(i) for i in input("Enter Pm point:").split()]

Cx1, Cy1 = pointDoubling(x1, y1, a, p, k) 

Qx, Qy = pointDoubling(x1, y1, a, p, d)
Sx, Sy = pointDoubling(Qx, Qy, a, p, k)

LC = (Py - Sy)%p * mod_inv((Px - Sx),p)
Cx2 = (LC*LC - Sx- Px)%p
Cy2 = (LC*(Px - Cx2) - Py)%p

print("C1=(",Cx1,",",Cy1,");C2=(",Cx2,",",Cy2,")")

sX, sTempY = pointDoubling(Cx1, Cy1, a, p, d)
sTempY = - (sTempY)
sY = sTempY % p

LC2= (Cy2 - sY)%p * mod_inv((Cx2 - sX),p)
Px2 = (LC2*LC2 - sX- Cx2)%p
Py2 = (LC2*(Cx2 - Px2) - Cy2)%p
print("P=(",Px2,",",Py2,")")
