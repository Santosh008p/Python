#1. Write a program to count the number of digits in a number n.
n=int(input())
n=abs(n)
if n==0:
    count=1
else:
    count =0
    while n!=0:
       n=n//10
       count+=1
print(f'number of digits is {count}')

#2. Write a program to display all the digits of a number n (one per line).
N=int(input())
N=abs(N)
digits=[]
if N==0:
    print(N)
else:
    while N!=0:
        digits.append(N%10)
        N=N//10
digits.reverse()
for d in digits:
    print(d)

#3. Write a program to find the sum of all digits of a number n.
digits=int(input())
if digits==0:
    print('0')
else:
    sum=0
    while digits!=0:
        digit=digits%10
        sum+=digit
        digits//=10
print("sum is ", sum)

#4. Write a program to find the product of all digits of a number n.
Number=int(input())
if Number==0:
    print(0)
else:
    product=1
    while Number!=0:
        Digit=Number%10
        product*=Digit

        Number//=10
print("product is", product)

#5. Write a program to reverse a number n.
orginal_number=int(input())
reverse_number=0
while orginal_number!=0:
    DDigit=orginal_number%10
    reverse_number= reverse_number*10 + DDigit
    orginal_number//=10
print(reverse_number)

#6. Write a program to find the largest digit in a number n.
integer= int(input())
largest_value=0
while integer!=0:
    value=integer%10
    if value>largest_value:
        largest_value=value
    integer//=10
print(f'largest value in the digit is: {largest_value}')


#7.Write a program to find the smallest digit in a number n.
n=int(input())
smallest_value=9
while n!=0:
    digit=n%10
    if digit< smallest_value:
        smallest_value=digit
    n//=10
print("Smallest digit in the number is ", smallest_value)

#8 . Write a program to count the number of even digits and odd digits in a number n.
n= int(input())
even_count=0
odd_count=0
while n!=0:
    digit=n%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1
    n//=10
print(f'even count={even_count} and odd count={odd_count}')

#9. Write a program to check whether a number n is a palindrome (reads the same reversed).
n=int(input())
original=n
rev_n=0
while n!=0:
    digit=n%10
    rev_n= rev_n*10+digit
    n//=10
print(rev_n)
if original==rev_n:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")

#10. Write a program to replace all zeros in a number n with the digit 5.
n=int(input())
if n==0:
    print(5)
else:
    result=0
    place=1
while n!=0:
    digit=n%10
    if digit==0:
        digit=5

    result=result + digit*place
    place*=10
    n//=10
print(result)


#11. Write a program to find the sum of the first and last digit of a number n.
n =int(input())
last_digit= n%10
while n>=10:
    n//=10
first_digit=n
print(first_digit+last_digit)

