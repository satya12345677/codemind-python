s=input()
l=list(s)
b=["a","e","i","o","u","A","E","I","O","U"]
c=0
for i in l:
    if i in b:
        c=c+1
print(c)