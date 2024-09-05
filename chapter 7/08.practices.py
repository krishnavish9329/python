# wap multiplication tabal in revars order
a= int(input("enter the no. "))
l=[]
for i in range(1,11):
    print(f"{a}X{i}={a*i}")
    l.append(a*i)
l.reverse()
print(l)