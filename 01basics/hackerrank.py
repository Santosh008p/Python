# # # # # x = int(input())
# # # # # y = int(input())
# # # # # z = int(input())  
# # # # # n = int(input())
# # # # # c=[(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
# # # # # print(c)

# # # # # n = int(input())
# # # # # arr = list(map(int, input().split()))
# # # # # uniques=[]
# # # # # for numbers in arr:
# # # # #     if numbers not in uniques:
# # # # #         uniques.append(numbers)
# # # # # sl=sorted(uniques)
# # # # # print(sl[-2])
# # # # # students=[]
# # # # # for _ in range(int(input())):
# # # # #     name = input()
# # # # #     score = float(input())
# # # # #     students.append([name,score])
# # # # # print(students)

# # # # # n = int(input())
# # # # # integer_list = map(int, input().split())
# # # # # print(int)

# # # # # def swap_case(s):
# # # # #     modified_string=''
# # # # #     for item in s:
# # # # #         if item.islower():
# # # # #            modified_string+= item.upper()
# # # # #         elif item.isupper():
# # # # #            modified_string+= item.lower()
# # # # #         else:
# # # # #            modified_string+= item
# # # # #     print(modified_string)
    

# # # # # swap_case("sAntosh!")

# # # # def count_substring(string, sub_string):
# # # #     count = 0
# # # #     n = len(sub_string)
    
# # # #     for i in range(len(string) - n + 1):
# # # #         if string[i:i+n] == sub_string:
# # # #             count += 1
            
# # # #     return count


# # # # if __name__ == '__main__':
# # # #     string = input().strip()
# # # #     sub_string = input().strip()

# # # #     count = count_substring(string, sub_string)
# # # #     print(count)


# # # c="H"
# # # thickness=9
# # # for i in range(thickness):
# # #     print((i*c).center(thickness-1))

# # # n,m= map(int, input().split())
# # # for i in range(n//2):
# # #     pattern= '.|.'*(2*i +1)
# # #     print(pattern.center(m,'-'))

# # # print("WELCOME".center(m,'-'))

# # # for i in reversed(range(n//2)):
# # #      pattern= '.|.'*(2*i +1)
# # #      print(pattern.center(m,'-'))

# # def print_formatted(number):
# #     # your code goes here
# #     for i  in range(1,n):
# #         decimal = number
# #         octal= oct(number)
# #         hex=hex(number)
# #         binary=bin(number)
# #         print(f'{decimal}  {octal}  {hex}  {binary}')


# #     n = int(input())
# #     print_formatted(n)

# s= input()
# first_name,last_name=s.split()
# print(first_name)
# for i in first_name:
#     if first_name[0].islower():
#         first_name.toupper()

A=list(map(int, input().split()))
B=list(map(int, input().split()))
print(A)

