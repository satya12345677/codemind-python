n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(0,n-2):
    if l[k+2]==l[i]+l[i+1]:
        k+=1
    else:
        k=0
        break
if k==0:
    print("no")
else:
    print("yes")