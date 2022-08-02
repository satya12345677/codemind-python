n=int(input())
l=list(map(int,input().split()))
h=[]
r=[]
for i in l:
   d=str(abs(i))
   p=len(d)
   h.append(p)
g=max(h)
for j in range(n):
    if h[j]==g and l[j] not in r:
        r.append(l[j])
print(*r)