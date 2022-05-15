n=int(input())
l=list(map(int,input().split()))
d=sum(l)/len(l)
print("{:,.2f}".format(d))