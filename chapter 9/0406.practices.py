##problem no. 4
#with open("this.txt") as t:
#    sim=t.read().lower()
#
#sim=sim.replace("donkey"," ####")
#with open("this.txt",'w') as t:
#    t.write(sim)

#problem no. 6
#find python 
with open("this.txt") as t:
    file=t.read().lower()
if "python" in file:
    print("python is present in file")
else:
    print("python isn't present in file")
