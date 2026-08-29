#1. Write a program to display the first n terms of the Fibonacci series.
n = int(input("enter number of terms"))
a=0
b=1
for i in range(n):
    print(a, end=' ')
    c=a+b
    a=b
    b=c

#2. Write a program to find the sum of the first n terms of the Fibonacci series.

n= int(input("enter number of terms"))

a=0
b=1
sum=0
for i in range(n):
    sum+=a
    c=a+b
    
    a=b
    b=c
print(sum)

#3. Write a program to find the sum of the series 1 + 2 + 3 + ... + n.
n =int(input("Enter a number"))

# total =0
# for i in range(1, n+1):
#     total+=i
# print(total)

#OR
def sum(n):
    return (n*(n+1))//2
    

print(sum(5))

#4. Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
n = int(input("enter a number"))
sum=0
for i in range(1, n+1):
    sum+=i*i
print(f'sum of the given series is {sum}')

#5. Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.
n =int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=1/i
print(f'sum of the given series is {sum}')

#6. Write a program to find the value of x raised to the power y without using inbuilt power.
x,y=map(int, input("enter two numbers").split())
answer=1
for _ in range(1,y+1):
    answer*=x
print(answer)

#7. Write a program to print a right-angled triangle pattern of stars of height n.
n=int(input("Enter an number"))

for i in range(1,n+1):
    print('*'*i)

#8. Write a program to print an inverted right-angled triangle pattern of stars of height n.
n=int(input("Enter the value of n"))
for i in range(n,1,-1):
    print('*'*i)

#9. Write a program to print a pyramid pattern of stars of height n.
n =int(input("Enter the height of the pyramid"))
for i in range (1, n+1):
    spaces=' '*(n-i)
    stars=(2*i-1)*'*'
    print(spaces+stars)

#10. Write a program to print a number triangle (row i contains numbers 1 to i).
n=int(input('Enter the height of triangle'))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#11. Write a program to print Pascal's triangle for n rows.
n = int(input("Enter number of rows: "))

for row in range(n):
    # Print spaces for triangular alignment
    print(" " * (n - row), end="")
    
    val = 1
    for col in range(row + 1):
        print(val, end=" ")
        # Efficient calculation of next value using formula: nCr = nCr-1 * (n - r + 1) / r
        val = val * (row - col) // (col + 1)
        
    print()