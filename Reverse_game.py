n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    s=0
    while i:
        r=i%10
        s=s*10+r
        i=i//10
    k.append(s)
print(*k)