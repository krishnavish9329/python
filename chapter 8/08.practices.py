def table(num,s):
    if s==11:
        return 0
    print(f"{num}X{s}={num*s}")
    s=s+1
    table(num,s)

x=int(input())
table(x,1)
