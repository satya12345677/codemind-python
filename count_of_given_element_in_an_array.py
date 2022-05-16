n=int(input())
l=list(map(int,input().split()))
d=int(input())
if d in l:
    print(l.count(d))
else:
    print(0)