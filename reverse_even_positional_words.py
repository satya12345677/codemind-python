s=input()
l=s.split()
a=[]
for i in range(len(l)):
    if i%2==0:
        a.append(l[i][::-1])
    else:
        a.append(l[i])
    
print(" ".join(a))