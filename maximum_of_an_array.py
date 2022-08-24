n=int(input())
l=list(map(int,input().split()))
c=-1000000
for i in l:
    if c<i:
        c=i
print(c)