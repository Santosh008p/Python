try:
    age=int(input("Age: "))
    print(age)
    income=20000
    risk=income/age
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print("Age can not be zero")

#
T = int(input())

for _ in range(T):
    a, b = input().split()
    
    try:
        print(int(a) // int(b))
        
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
        
    except ValueError as e:
        print("Error Code:", e)

#
import re
S = int(input())

for _ in range(S):
    s = input()
    repeats = ["++", "**", "*+", "+*", "??", "?+", "+?"]
    try:
        for i in repeats:
            if i in s:
                raise Exception
        re.compile(s)  
    except Exception as e:
        print("False")
    else:
        print("True")
        