n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
   d=str(abs(i))
   p=len(d)
   k.append(p)
   
print(*k)