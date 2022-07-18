n=int(input())
l=list(map(int,input().split()))
oc=0
for i in range(n-2):
    if (l[i]%2==0 and l[i+2]%2!=0) or (l[i]%2!=0 and l[i+2]%2==0):
            oc+=1
print(oc)