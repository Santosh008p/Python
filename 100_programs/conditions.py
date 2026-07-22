#1. Write a program to read a number and check whether it is even or odd.
num=int(input())
if num%2==0:
    print("It is an even number")
else:
    print("It is an odd number")


#2. Write a program to read a number and check whether it is positive, negative or zero.
num1=int(input())
if num1>0:
    print("It is a positive number")
elif num1<0:
    print("It is a negative number")
else:
    print("The given number is zero")

#3. Write a program to read three numbers and find the largest among them.
a,b,c=map(int, input().split())
if a>=b and a>=c:
    print(f'{a} is the largest number')
elif b>=a and b>=c:
    print(f'{b} is the largest number')
else:
    print(f'{c} is the largest number')

#short method
maximum=max(a,b,c)
print(maximum)

#4. Write a program to read three numbers and find the smallest among them.
if a <= b and a <= c:
    print(f'{a} is the smallest number')
elif b <= a and b <= c:
    print(f'{b} is the smallest number')
else:
    print(f'{c} is the smallest number')

print(min(a,b,c))

#5. Write a program to read a year and check whether it is a leap year or not.
print("Enter any Year")
year =int(input())
if year%400==0:
    print("Its a leap Year")
elif year%100 !=0 and year%4==0:
    print("Its a Leap Year")
else:
    print("Its not a leap year")



#6. Write a program to read a character and check whether it is a vowel or a consonant.
vowels="AEIOUaeiou"
print("Enter a character:")
ch=input()
if len(ch)>1:
    print("Please enter only one character")
else:
    if ch in vowels:
        print("Its a vowel character")
    else:
        print("Its a consonant character")

#7. Write a program to read a character and check whether it is an alphabet, digit or special symbol.
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
print("Enter a character")
char=input()
if len(char)>1:
    print("Please enter only one character")
elif char in characters:
    print("The given inout is character")
elif char in digits:
    print("The given input is digit")
else:
    print("The given character is symbol")

# shortcut method
if char.isalpha():
    print("character")
elif char.isdigit():
    print("digit")
else:
    print("Symbol")

#8. Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

print("Enter your marks:")
mark=int(input())
if mark>=90:
    print("congratulations!, You got an A")
elif 80<=mark<90:
    print("COngratulations !, you got a B")
elif 70<=mark<80:
    print("Congratulations! , You got C")
elif 60<=mark<70:
    print("congratulations! you got D")
else:
    print("kyun nahi horahi padhai, you got F")

#9. Write a program to read a number and check whether it is divisible by both 3 and 5.
print("Enter a number:")
n=int(input())
if n%3==0 and n%5==0:
    print("the given number is divisible by both 3 and 5")
else:
   print("The given number is NOT divisible by both 3 and 5")

#10. Write a program to read the age of a person and check whether they are eligible to vote.
print("Enter Your age:")
age=int(input())
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")