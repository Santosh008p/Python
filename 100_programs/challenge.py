#1. Write a program to check whether a number is prime, using a function/method.
def check_prime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    return is_prime


n=int(input("Enter a number:"))
result=check_prime(n)
if result:
        print('The given number is a prime number')
else:
        print('The given number is not prime number')

#2. Write a program to print all prime numbers between two given numbers a and b.
def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False

    return True


a=int(input("Enter a starting number:"))
b=int(input("enter ending number:"))

for n in range(a,b+1):
    if check_prime(n):
        print(n)


#3. Write a program to find the sum of digits of a number repeatedly until a single digit remains.
def find_sum(n):
   while n>=10:
      total=0
      while n>0:
         digit=n%10
         total+=digit
         n//=10
      n=total

   return n
   


n=int(input("enter a number:"))
print(find_sum(n))

#4. Write a program to count the number of prime digits present in a number n.

    
def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False

    return True

def count_prime(n):
    count=0
    while n>0:
        digit=n%10
        if check_prime(digit):
            count+=1
        n//=10
    return count

n = int(input("Enter a number: "))

result = count_prime(n)

print("Number of prime digits:", result)

#5. Write a program to check whether a number is a palindrome and a prime at the same time.

def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False

    return True


def check_palindrome(n):
    palindrome=False
    original=n
    rev=0
    while n>0:
        N=n%10
        rev=rev*10+N
        n//=10

    if original==rev:
        palindrome=True

    return palindrome


n = int(input("Enter a number: "))

if check_prime(n) and check_palindrome(n):
    print("The number is both prime and palindrome")
else:
    print("The number is not both prime and palindrome")


#6. Write a program to find the largest and smallest number that can be formed using the digits of n
n=int(input("Enter a number"))
arr=[]
accending=[]
decending=[]
while n>0:
    N=n%10
    arr.append(N)
    n//=10
print(arr)
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
largest=0
for digit in arr:
     largest=largest*10+digit

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

smallest=0
for digit in arr:
     smallest=smallest*10+digit
print("Largest number:", largest)
print("Smallest number:", smallest)

#7. Write a program to convert a decimal number into its binary equivalent.

n=int(input("Enter a decimal number"))
binary=0
place=1
while n>0:
    N=n%2
    binary=binary+N*place
    place*=10
    n//=2
print(binary)

#8. Write a program to convert a decimal number into its binary equivalent.

n=int(input("Enter a binary number"))
power=0
decimal=0
while n>0:
    N=n%10
    decimal=decimal+ N*(2**power)
    power+=1
    n//=10
print(decimal)

#9. Write a program to display a menu that lets the user repeatedly choose any of the above tasks until they choose to exit.

def check_prime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    return is_prime


def check_palindrome(n):
    palindrome=False
    original=n
    rev=0
    while n>0:
        N=n%10
        rev=rev*10+N
        n//=10

    if original==rev:
        palindrome=True

    return palindrome


def find_sum(n):
   while n>=10:
      total=0
      while n>0:
         digit=n%10
         total+=digit
         n//=10
      n=total

   return n


def decimal_to_binary(n):
    binary=0
    place=1
    while n>0:
        N=n%2
        binary=binary+N*place
        place*=10
        n//=2
    return binary


def binary_to_decimal(n):

    power=0
    decimal=0
    while n>0:
        N=n%10
        decimal=decimal+ N*(2**power)
        power+=1
        n//=10
    return decimal


while True:
    print("\n----- MENU -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Find Sum of Digits")
    print("4. Decimal to Binary")
    print("5. Binary to Decimal")
    print("6. Exit")

    choice=int(input('Enter your choice:'))

    if choice==1:
        n=int(input("enter a number"))
        if check_prime(n):
            print("The given number is prime number")
        else:
            print("The given number is not prime number")
    elif choice==2:
        n=int(input("Enter a number:"))
        if check_palindrome(n):
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice==3:
        n=int(input('Enter a number'))
        print(find_sum(n))

    elif choice==4:
        n=int(input("Enter a decimal number:"))
        print("binary equivalent is ", decimal_to_binary(n))
    elif choice==5:
        n=int(input("Enter a binary number:"))
        print("Decimal equivalent is ", binary_to_decimal(n))
    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")

    







