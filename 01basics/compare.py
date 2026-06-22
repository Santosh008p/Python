name=input("Enter your name: ")
if len(name)<3:
    print("name must be atleast 3 character")
elif len(name)>50:
    print("name can't have more than 50 characters")

else:
    print("name looks good")


