s=input()
l=list(s)
b=["a","e","i","o","u"]
a=[]
for i in b:
    if i not in l:
        a.append(i)
d=sorted(a)
if len(a)!=0:
    print(" ".join(a))
else:
    print("0")
