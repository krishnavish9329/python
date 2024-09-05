def pettern(p):
    if p==0:
        return 0
    print("*"*p)
    p=p-1
    pettern(p)


a=int(input())
pettern(a)