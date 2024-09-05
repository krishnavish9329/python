# write a program to read the text from a given file "poem.txt" & find the wherther it content the word "twunkle"
f=open("poem.txt","r")
data=f.read()
if 'tunkle'in data:
    print( "twunkle is find ")
else:
    print ("twunkle isn't find")
f.close()