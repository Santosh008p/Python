for item in "Santosh":
    print (item)

for item in ['santosh', 'rohit', 'ravi']:
    print (item)
 
 # range 
for item in range(10):  
    print (item)
for item in range(5,10):
    print(item)
for item in range(5,10,2):
    print(item)

prices=[100,200,300]
sum=0
for item in prices:
    sum=sum+item
print(sum)

###Nested Loops###
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers=[5,2,5,2,2]
for x_count in numbers:
   # print('x'*item)
    output=''
    for count in range(x_count):
         output+='x'
    print(output)

numbers1=[1,1,1,1,5]
for x_count in numbers1:
   # print('x'*item)
    output=''
    for count in range(x_count):
         output+='x'
    print(output)
        
