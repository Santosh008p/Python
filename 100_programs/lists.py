#1. Write a program to read n elements into an array and print them.
n=int(input("Enter number of elements"))
list=[]
for i in range(n):
    list.append(int(input()))
# print(list)

#2.Write a program to find the sum and average of all elements in an array.
sum=0
count=0
for i in list:
    sum+=i
    count+=1
print("Sum of the all the elements in the array is ", sum)
average=sum/count
print("average of the elements in the array is ", average)

#3. Write a program to find the largest and smallest element in an array.
arr=[2,5,6,3,7,1]
largest=arr[0]
smallest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("largest:",largest)
for i  in arr:
    if i <smallest:
        smallest=i
print(smallest)

#4. Write a program to count the number of even and odd elements in an array.
arr=[1,2,6,7,4,3]
even_count=0
odd_count=0
for i in arr:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f'even Count:{even_count} and odd count:{odd_count}')

# 5. Write a program to search for an element in an array (linear search).
arr=[1,2,3,4,5,6]
search=input("Input element that need to be searched:")
found=False
for i in arr:
    if i==search:
         found=True
         break
if found:
    print("Element found")
else:
    print("Not found")

#6. Write a program to reverse the elements of an array.
arr=[1,2,3,4,5]
reversed=[]
while len(arr)!=0:
    reversed.append(arr.pop())
print(reversed)

#7. Write a program to find the second largest element in an array.
arr=[5,3,6,57,7]
largest=arr[0]
second_largest=None

for i in arr:
    if i > largest:
        second_largest=largest
        largest=i
    elif i!=largest and(second_largest is None or i>second_largest):
        second_largest=i
print(f'largest element in the array is:{largest} and second largest element in the array is:{second_largest}')

#8. Write a program to count the frequency of each element in an array.
arr=[2,4,5,2,66,5]
counted=[]
for i in arr:
    if i in counted:
        continue

    count=0
    for j in arr:
        if i==j:
            count+=1
    print(f'{i} appears {count} times')
    counted.append(i)

#9. Write a program to remove duplicate elements from an array.
arr=[2,5,7,4,3,3,4,2,1]
uniques=[]
for i in arr:
    if i not in uniques:
        uniques.append(i)
print(uniques)

#10. Write a program to sort an array in ascending order (bubble sort).
arr=[1,3,2,6,4,9,7]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    
print(arr)

#11. Write a program to merge two arrays into one.
arr1=[1,2,3]
arr2=[4,5,6]

for i  in arr2:
    arr1.append(i)


print(arr1)
#12. Write a program to find the sum of all even-indexed and odd-indexed elements separately.
arr=[1,2,3,4,5,6,7,8,9,10]
even_sum=0
odd_sum=0

for i in range(len(arr)):
    if i%2==0:
        even_sum+=arr[i]
    else:
        odd_sum+=arr[i]
print(even_sum)
print(odd_sum)