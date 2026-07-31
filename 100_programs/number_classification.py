#1. Write a program to read a number and check whether it is prime or not.
n=int(input())
is_prime=True
for i in  range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print("The given number is a prime number")
else:
    print("The given number is not prime number")

#2.Write a program to display all prime numbers from 1 to n.
n=int(input())

for num in range(2, n+1):
    is_prime=True

    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    if is_prime:
        print(num)
        

#3. Write a program to display the first n prime numbers.

n= int(input())
count=0
num=2

while count<n:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

    if is_prime:
        print(num)
        count+=1
    num+=1

#4. Write a program to check whether a number is an Armstrong number.
n=int(input())

original=n
count=0
sum=0
while n!=0:
    N=n%10
    n//=10
    count+=1
n=original

while n!=0:
     power=1
     digit=n%10
     for i in range(count):
          power=power*digit
     sum+=power
     n=n//10

if sum==original:
     print("Armstrong Number")
else:
     print("Not Armstrong Number")
    
#5. Write a program to display all Armstrong numbers from 1 to n.

n=int(input())

for  num in range(1,n):
     original= num
     count=0
     temp=num

     while temp!=0:
          temp//=10
          count+=1

     sum=0
     temp=num
     while temp!=0:
          digit=temp%10

          power=1
          for i in range(count):
               power=power*digit

          sum+=power
          temp//=10

     if sum==original:
          print(original)

#6. Write a program to check whether a number is a perfect number.
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("its perfect number")
else:
    print("Its not perfect number")
        
           
#7. Write a program to check whether a number is a strong number (sum of factorials of its digits).
n=int(input())
original=n

sum=0
while n!=0:
    N=n%10

    factorial=1
    for i in range(1,N+1):
        factorial*=i

    sum+=factorial
    n//=10

if sum==original:
    print("Strong Number")
else:
    print("Not Strong")




#8. Write a program to check whether a number is an automorphic number.
n= int(input())
original=n


square =n*n
count=0
while n!=0:
    n//=10
    count+=1
divisor=1
for _ in range(count):
    divisor=divisor*10

reminder=square%divisor
if reminder==original:
    print("Automorphic number")
else:
    print("Not Automorphic")

#9. Write a program to check whether a number is a Harshad (Niven) number.
n = int(input())
original=n
sum=0
while n!=0:
    N=n%10
    sum+=N
    n//=10
if sum!=0 and  original%sum==0:
    print("Harshad Number")
else:
    print("Not harshad number")

#10. Write a program to find all factors (divisors) of a number n.
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)


#11. Write a program to count the number of factors of a number n.
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1

print(count)
    

#12. Write a program to find the GCD (HCF) of two numbers.
a=int(input())
b=int(input())
hcf=1
if a>b:
    min=b
else:
    min=a
for i in range (1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)

#13. Write a program to find the LCM of two numbers.
a=int(input())
b=int(input())
lcm=0

if a>b:
        start=a
else:
    start=b

for i in range(start,a*b+1):
    if i%a==0 and i%b==0:
        lcm=i

print(lcm)
        