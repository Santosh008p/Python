#1. Write a program to display all the natural numbers from 1 to n. (n is user input)
n = int(input())
for i in range(1,n):
    print(i)

#2. Write a program to display all natural numbers from 1 to n in reverse order.
for i in range(n,1,-1):
    print(i)

#3. Write a program to display all even numbers from 1 to n.
for i in range( 1,n):
    if i%2==0:
        print(i)
#4. Write a program to display all odd numbers from 1 to n.
for i in range(1,n):
    if i%2!=0:
        print(i)

#5. Write a program to find the sum of all natural numbers from 1 to n.
sum=0
for i in range(1,n):
    sum+=i
print("Sum of natural number is ", sum)

#6. Write a program to find the sum of all even numbers from 1 to n.
num=int(input())
total=0
for i in range(1,num):
    if i%2==0:
        total+=i
        
print("The sum of all even number upto n is ", total)

#7. program to find the sum of all odd numbers from 1 to n.

for i in range(1,num):
    if i%2!=0:
        total+=i
print("The sum of all odd number upto n is", total)
#8. Write a program to find the product of all natural numbers from 1 to n (factorial of n).
number=int(input())
product= 1
for i in range(1,number+1):
    product*= i
print(product)

#9. Write a program to display the multiplication table of a number n.
for i in range(1,11):
    print(f'{n}*{i} ={n*i}')

#10. Write a program to display all multiples of a number m up to n terms.
print("Enter value for m")
m=int(input())
for i in range(1,n+1):
    print(m*i, end=" ")
#11. Write a program to count how many numbers from 1 to n are divisible by 3.
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print(f'count is {count}')

#12. Write a program to display all numbers from 1 to n that are divisible by 3 or 5.
for i  in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)