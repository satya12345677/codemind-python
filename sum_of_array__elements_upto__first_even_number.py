n=int(input())
l=list(map(int,input().split()))
k=[]
s=0
for i in l:
    if i%2!=0:
        s=s+i
    if i%2==0:
        break
print(s)