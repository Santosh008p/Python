#1.
from itertools import combinations
s,k=input().split()
k=int(k)
s=sorted(s)
for i in range(1,k+1):
    for x in combinations(s,i):
        print(''.join(x))

#2.
from itertools import combinations_with_replacement
s,k =input().split()
k=int(k)
s=sorted(s)

for x in combinations_with_replacement(s,k):
    print(''.join(x))
    
#3.
from itertools import groupby

s=input()
for k, g in groupby(s):
    print((len(list(g)),int(k)))

#4
from itertools import groupby
s=input()
for k, g in groupby(s):
    print((len(list(g)),int(k)) ,end=' ')
#5
from itertools import combinations
N=int(input())
letter=input().split()
k=int(input())
indices=list(range(N))
all_combos=list(combinations(indices,k))

count=0
for combo in all_combos:
    if any(letter[i]=='a' for i in combo):
        count+=1

print(count/len(all_combos))
#6
from itertools import product
K,M=map(int,input().split())
lists=[]
for _ in range(K):
    data=list(map(int,input().split()))
    lists.append(data[1:])

max_value=0
for combo in product(*lists):
    value=sum(x*x for x in combo)%M
    max_value=max(max_value,value)
print(max_value)
    