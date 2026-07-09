names=['john','bob', 'mosh','sarah','mary']
print(names[2:4])

names[0]='santosh'
print(names)

numbers=[2,4,6,8,10]
largest=numbers[0]
for item in numbers:
    if item >largest:
        largest=item
print(f'largest item in your list is {item}')

###2D Lists###
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

##list methods##
nums=[1,2,3,4,5]
nums.append(6) # add a value in the end of list
print(nums)

nums.insert(2,5) #used to insert value at any position in list
print(nums)

nums.remove(5) # remove first instance
print(nums)

#nums.clear() # clear list
#print(nums)

nums.pop() #remove last item from list
print(nums)

print(nums.index(2))
print(nums.count(2))

nums.reverse()
print(nums)
nums.sort()
print(nums)

##removing the duplicates##
all_num=[2,2,1,1,3,4,5]
uniques=[]
for numbers in all_num:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)