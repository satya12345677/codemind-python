n=int(input())
l=list(map(int,input().split()))
s=[]
k=[]
for i in l:
    r=i%10
    s.append(r)
    d=i//10
    k.append(d)
print(sum(s)+sum(k))