n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if not(i>=a and i<=b):
       k.append(i)
if len(k)!=0:
    print(min(k))
else:
    print(-1)