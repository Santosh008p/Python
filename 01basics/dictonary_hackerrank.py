from collections import defaultdict

n, m = map(int, input().split())

A = defaultdict(list)

# Store words from group A with positions
for i in range(1, n + 1):
    word = input()
    A[word].append(i)

# Process group B
for _ in range(m):
    word = input()
    
    if word in A:
        print(' '.join(map(str, A[word])))
    else:
        print(-1)

#2.
from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total = 0

for _ in range(n):
    data = input().split()
    s = Student(*data)
    total += int(s.MARKS)

print(f"{total/n:.2f}")

#3
from collections import OrderedDict
N=int(input())
d=OrderedDict()
for _ in range(N):
    *name,price=input().split()
    item_name=" ".join(name)
    price=int(price)
    
    if item_name in d:
        d[item_name]+=price
    else:
        d[item_name]=price
for item,total in d.items():
    print(item, total)

#4
from collections import OrderedDict

n=int(input())
d=OrderedDict()

for _ in range(n):
    word=input()
    
    if word in d:
        d[word]+=1
    else:
        d[word]=1
        
print(len(d))
print(*d.values())

#5
from collections import deque
n= int(input())
d=deque()
for _ in range(n):
    command=input().split()
    
    if  command[0]=="append":
        d.append(command[1])
    elif command[0]=="pop":
        d.pop()
    elif command[0]=="popleft":
        d.popleft()
    elif command[0]=="appendleft":
        d.appendleft(command[1])
print(*d)


#6
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    
    last = float('inf')  
    
    while d:
        if d[0] >= d[-1]:
            pick = d.popleft()
        else:
            pick = d.pop()
        
        if pick <= last:
            last = pick
        else:
            print("No")
            break
    else:
        print("Yes")

#7
import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()

counts = Counter(s)

sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

for char, count in sorted_chars[:3]:
    print(char, count)

    