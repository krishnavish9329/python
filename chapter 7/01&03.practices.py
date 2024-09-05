# write a program to print multiplication table of a given nu. using for loop
'''a= int(input("enter the no. "))
for i in range(1,11):
    #print(str(a) +"X"+ str(i)+"=" +str(i*a))
    print(f"{a}X{i}={a*i}")'''

#using while loop // problem 3
a=int(input("no.  "))
i=1
while i<10:
    print(f"{a}X{i}={a*i}")
    i=i+1
