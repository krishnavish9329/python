a1=int(input("enter the no. of subject : "))
a2=int(input("enter the no. of subject : "))
a3=int(input("enter the no. of subject : "))
sum=(a1+a2+a3)/3
if(sum>40):
    if(a1>33 and a2>33 and a3>33):
        print("you are pass")
    else:
        print("you are fail due to subject")
else:
    print("you are fail due to persentage")