import os
oldname="this.txt"
newname="rempve.txt"

with open(oldname)as t:
    f=t.read()

t=open(newname,'w')
t.write(f)

os.remove(oldname)
