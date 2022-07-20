n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if l[i]%2==0:
        s=s+1
    else:
        s=0
        break
if s==0:
    print("False")
else:
    print("True")