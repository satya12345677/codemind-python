n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    if l[i]%2==0:
        if i%2==0:
            k+=1
        else:
            k=0
            break
if k==0:
    print("False")
else:
    print("True")