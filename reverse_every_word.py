s=input()
l=s.split()
a=[]
for i in l:
    a.append(i[::-1])
print(" ".join(a))