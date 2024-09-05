#wap to finde prime no. or not
num=int(input("enter the num. :"))
t=False
for i in range(2,num-1):
    if(num%i==0):
        t=True
        break
if t==True:
    print("entered the num. is not prime")        
else:
    print("entered the num. is prime")