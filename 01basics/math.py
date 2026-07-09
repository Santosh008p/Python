import math
x=2.3
print(round(x))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))
#Hackerrank problems
import cmath
z=complex(input())

r=abs(z)
theta=cmath.phase(z)
print(r)
print(theta)

#2.
import math
AB=int(input())
BC=int(input())
angle = round(math.degrees(math.atan(AB / BC)))
print(f"{angle}\u00B0")

#3
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)**2)

#4
a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

#5
a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))

#6
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(pow(a,b)+pow(c,d))

#7
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*((10**i)//9))