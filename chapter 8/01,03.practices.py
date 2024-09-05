def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

x=int(input("enter the number "))
y=int(input("enter the number "))
z=int(input("enter the number "))
i=greatest(x,y,z)
print(i)

# 03 practices
print(i,end="   ")
print(43,end="   ")
