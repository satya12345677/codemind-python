s=input()
l=list(s)
a="aeiou"
b="AEIOU"
m=0
u=0
for i in a:
    if i in s:
        m+=1
    else:
        m=0
        break
for i in b:
    if i in s:
        u+=1
    else:
        u=0
if m!=0 or u!=0:
    print("True")
else:
    print("False")