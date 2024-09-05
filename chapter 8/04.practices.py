# using recursion find sum of natural no.

def sum(num):
    if num==0:
        return 0
    return (num+sum(num-1))

x=int(input())
i=sum(x)
print("sum of nature no."+ str(i))
