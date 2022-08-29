s=input()
l=input()
a=list(s)
for i in range(len(a)):
    if a[i] in l:
        print("True")
        print(i)
        break
else:
    print("False")