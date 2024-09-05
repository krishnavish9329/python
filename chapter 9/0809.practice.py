#with open("this.txt") as t:
#    contant=t.read()
#
#with open("copy.txt",'w') as t:
#    t.write(contant)

#09 problem

with open("this.txt") as t:
    contant=t.read()

with open("copy.txt") as t:
    contant2=t.read()

if(contant==contant2):
    print("identical")
else:
    print("not identival")
