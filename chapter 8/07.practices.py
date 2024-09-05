def remove_and_split(string ,word):
    newstr=string.replace(word,"***")
    return newstr.strip()
    
hello="    my name  is krishna  kumar vishwakarma   "
n=remove_and_split(hello,"kumar")
print(n)
print(type(n))