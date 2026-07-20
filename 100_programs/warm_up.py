import math
#1. Write a program to print "Hello, World!" on the screen.
print("Hello, World!")

#2. Write a program to read two numbers and print their sum.
print("Enter Two Numbers:")
a,b =map(int, input().split())
sum=a+b
print("sum is:", sum)

#3. Write a program to read two numbers and print their sum, difference, product and quotient.
difference= a-b
product=a*b
quotient=a/b
print("difference is:", difference)
print("Product is:", product)
print("Quotient is:", quotient)

#4. Write a program to read the radius of a circle and print its area and circumference.
print("Enter the radius of the circle:")
r=int(input())
area=math.pi*pow(r,2)
circumference=2*math.pi*r
print("Are of the given circle is :", area)
print("circumference of the given circle is:", circumference)


#5. Write a program to read the length and breadth of a rectangle and print its area and perimeter.
print("Enter the length and breadth of the rectanlge")
l,breadth=map(int, input().split())
Area=l*breadth
perimeter=2*(l+breadth)
print("Area and perimeter of the given rectangle is:", Area, perimeter)

#6. Write a program to swap two numbers using a third variable.
c=a
a=b
b=c
print(a,b)

#7. Write a program to swap two numbers without using a third variable.
print("Enter two numbers: ")
num1,num2=map(int, input().split())
num1, num2= num2, num1



print(num1,num2)

#8 Write a program to read a temperature in Celsius and convert it to Fahrenheit
print("Enter the temperature in celcius")
c=int(input())
F=(c*1.8)+ 32
print(f'Temperature in Farenheit is {F}F')

#9 Write a program to read the marks of 5 subjects and print the total and average.
print("Enter the Marks obtained by the students")
sub1, sub2, sub3, sub4, sub5=map(int, input().split())
avg=(sub1+ sub2 + sub3 + sub4 + sub5 )/5
print("Average marks of student is:",avg)

#10. Write a program to read seconds and convert them into hours, minutes and seconds.
print("Enter seconds")
seconds=int(input())
hours=seconds//3600
remaining=seconds%3600
minutes=remaining//60
seconds_left=remaining%60
print(f"{hours} hours, {minutes} minutes, {seconds_left} seconds")
