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