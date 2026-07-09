try:
    age=int(input("Age: "))
    print(age)
    income=20000
    risk=income/age
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print("Age can not be zero")
