#recursion 
# n!=1*2*3*...*n

def fectorial(num):
    if num==0:
        return 1
    else:
        return (num*fectorial(num-1))
    
num =int(input())
i=fectorial(num)
print(i)