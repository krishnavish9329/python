#from re import template
name=input("Enter you name :")
date=input("enter the data of today :")
print("DERA " + name +"\n you are selected \n" + date)
template ='''
dear <name>,
you are selected ,
<data>
'''
print(template.replace("<name>",name).replace("<data>",date))