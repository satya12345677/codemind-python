n,k=map(int,input().split())
l=list(map(int,input().split()))
h=[]
s=0
for i in l:
   d=str(abs(i))
   p=len(d)
   h.append(p)
   if p==k:
        s=s+1
print(s)