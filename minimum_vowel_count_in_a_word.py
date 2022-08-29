s=input()
l=s.split()
b="AEIOUaeiou"
a=[]
for i in range(len(l)):
    c=0
    for j in l[i]:
        if j in b:
            c=c+1
    a.append(c)
print(min(a))