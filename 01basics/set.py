# HackerRank set Question solutions
#1.
N=int(input())
stamps=set()
for country in range(N):
    country=input()
    stamps.add(country)
print(len(stamps))


#2.
n = int(input())
s = set(map(int, input().split()))
N=int(input())

for _ in range(N):
    command=input().split()

    if command[0]=="pop":
        s.pop()
    elif command[0]=="remove":
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.remove(int(command[1]))
print(sum(s))

#3.
n=int(input())
English=set(map(int,input().split()))
b=int(input())
French=set(map(int,input().split()))
print(len(English.union(French)))

#4.
n=int(input())
English=set(map(int,input().split()))
b=int(input())
French=set(map(int,input().split()))
print(len(English.intersection(French)))

#5.
n=int(input())
English=set(map(int,input().split()))
b=int(input())
French=set(map(int,input().split()))
print(len(English.difference(French)))

#6.
n=int(input())
English=set(map(int,input().split()))
b=int(input())
French=set(map(int,input().split()))
print(len(English.symmetric_difference(French))) #return all the elements in both sets except those who are in both sets

#7.set mutations
nA=int(input())
A=set(map(int,input().split()))
N=int(input())

for _ in range(N):
    command=input().split()
    B=set(map(int,input().split()))
    
    if command[0]=="intersection_update":
        A.intersection_update(B)
    elif command[0]=="update":
        A.update(B)
    elif command[0]=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command[0]=="difference_update":
        A.difference_update(B)
    
print(sum(A))

#8.
K = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

captain_room = (K * sum(unique_rooms) - sum(rooms)) // (K - 1)

print(captain_room)

#9
A=set(map(int,input().split()))
n=int(input())
is_strict=True
for _ in range(n):
    other_set=set(map(int,input().split()))
    if  not (A> other_set):
        is_strict=False
print(is_strict)

#10
nT=int(input())
for _ in range(nT):
    
    nA=int(input())
    A=set(map(int,input().split()))
    nB=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
