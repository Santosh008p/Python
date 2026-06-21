
#####Formatting Strings#####
first="santosh"
last="parajuli"
message= first + " [" + last + "] is a coder"
message2=f'{first} [{last}] is a coder'
print(message)
print(message2)

###String Methods###
print(len(first))
print(first.upper())
print(first.lower())
print(first.title())

print (first.find('o'))
print(first.find('osh'))
print(first.replace('santosh', 'kada'))

print('santosh' in first)


