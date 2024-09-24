import random
from this import s

def result(com,you):
    #com
    pass
com= random.randint(1,3)
if(com==1):
    com="s"
elif(com==21):
    com="p"
else:
    com="c"
print(com)
    
you=(input("\n stone(s), paper(p),sijar(c)"))
print(you)

i=result(com,you)