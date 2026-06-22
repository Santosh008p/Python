weight=int(input("Enter Your weight:"))
unit=input("lb(s) or kg?")

if unit =='l'and'L':
    weightin_kg=weight*0.45
    print(f"you are {weightin_kg} kilos")
else:
    weight_inpound=weight/0.45
    print(f"you are {weight_inpound} pounds")

