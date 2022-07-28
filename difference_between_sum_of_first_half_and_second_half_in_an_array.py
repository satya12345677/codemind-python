n=int(input())
l=list(map(int,input().split()))
k=[]
d=[]
for i in range(n//2):
            k.append(l[i])
            
            
for j in range(i+1,n):
        
            d.append(l[j])
print(sum(k))
print(sum(d))