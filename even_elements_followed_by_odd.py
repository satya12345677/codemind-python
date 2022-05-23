n=int(input())
s=list(map(int,input().split()))
oc=[]
ec=[]
r=[]
for i in range(n):
    if s[i]%2==0:
        ec.append(s[i])
    else:
        oc.append(s[i])
r=ec+oc
for i in r:
    c=i
    print(c,end=' ')