
t,s,b=map(int,input().split())
capacity=2*s*t*b*512
res=int(capacity/1024)
print(str(res)+"KB")
