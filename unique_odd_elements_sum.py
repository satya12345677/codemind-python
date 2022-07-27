n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in l:
    if i%2!=0:
        if i not in k:
            k.append(i)
print(sum(k))