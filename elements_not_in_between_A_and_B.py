n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(n):
    if not(a<=l[i]<=b):
        c=c+1
        print(l[i],end=' ')
if c==0:
    print(-1)