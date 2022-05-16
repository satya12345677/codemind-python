n=int(input())
l=list(map(int,input().split()))
o=int(input())
for i in l:
    if o==i:
        print("True")
        break
else:
    print("False")