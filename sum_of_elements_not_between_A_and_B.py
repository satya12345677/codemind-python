n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
s=0
for i in range(n):
    if not(a<=l[i]<=b):
        c=c+1
        s=s+l[i]
print(s)
