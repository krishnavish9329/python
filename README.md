# welcom to Python course 

# Index
1) Introduction of Python
2) Veriables And Datatype
3) String 
4) condtion Statements
5) List & Tubles
6) Dictionary & set
7) Loops
8) Function & recursion
9) Filo i/0
10) OOPs


# Introduction of Python

<b>What is python?</b> <br>
Python is a programming language that's used for a variety of purposes,  <br>
including:  <br>
<b>Web development</b>: Python is used to build websites and web applications  <br>
<b>Software development</b>: Python is used to create software  <br>
<b>Data science</b>: Python is used for data analysis and machine learning  <br>
<b>Automation</b>: Python can be used to automate tasks   <br>
<i>Python is a general-purpose language that's easy to learn and can run on many different platforms. Here are some other things to know about Python:</i>  <br>
Dynamic and interpreted: Python is a dynamic, interpreted language that doesn't require type declarations in source code.  <br>
<b>Name</b>: Python is named after the British comedy group Monty Python.  <br>
<b>Developer</b>: Guido van Rossum developed Python and originally released it in 1991.  <br>
<b>Popularity</b>: Python is one of the most popular programming languages today <br>
<hr>

why the name puthon?





what feature taken from which languages?



appliction of python programming?



feature of puthon programming


limitation of python?




chapter1

modules,comments & pip commamnd?



# Veriables And Datatype
## chapter 1

First of all we undertand <i><b>print("Hello World")</b></i>     you can run program at chapter1/firth_program.py <br>
This function outputs the supplied message or a value to the console.
<br>
<br>

<b>Python Character Set</b>
<b>Letters</b> A to Z, a to z <br>
<b>Digits</b>  0 to 9<br>
<b>Special Symbols</b> -/*-+<br>
<b>Whitespaces</b> Blank Space, Tab, carriage return, newLine, formfeed<br>
<b>Other character</b> Python can process all ASCLL and Unicode characters as pert of data pr literals<br>

<b>Veriable</b>
A Veriable is a name give to a memory location in a Program<br>
<b>
name = "username"
age = 32
price = 23.33
</b>
<hr>


<b>type()</b>
Python type() is a built-in function that returns the type of the objects/data elements stored in any data type or returns a new type object depending on the arguments passed to the function.<br>
<hr>

<b>identifiers</b>
An identifier is a name given to a variable, function, class, module, or other object in a program.<br>
<b>keyword</b>
keyword is a word that serves a specific function in Python. OR REserved Words Also knows as Keyword<br>
<hr>

<b>Datatype</b><br>
<i>Primary datatype</i>
Integers<br>
String<br>
Float<br>
Boolean<br>
None<br>
<hr>

<b>Solve one Problem <i>Sum of 2 number</i> </b> <a herf="chapter 1/firsth_program.py">link</a>

<b>Type Of Tokens</b><br>
Punctuators<br>
Punctuators are symbols to organize sentence structure in programming<br>
(),{},[],@,#,-=,+=,*=,/=,==,=,+,-,*,/ etc<br>
<hr>

# String 
## chapter 2
<i>Strings are used for representing textual data. A string is a sequence of characters enclosed in either single quotes ('') or double quotes (“”). The Python language provides various built-in methods and functionalities to work with strings efficiently.</i><br>

name1="ab"<br>
name='sb'<br>
name3='''all peragaph'''<br>

<b><i>Expression Execution</i></b><br>
A,B =2,3<br>
txt="@"<br>
print(2*txt*3)<br>

<b>Output</b><br>
@@@@@@<br>

A,B ="2",3<br>
Txt="@"<br>
print((A+Txt)*B)<br>
<b>Output</b><br>
2@2@2@<br>
<hr>

<b>Comment</b><br>
there are 2 type of Comment<br>
<i># single line comment</i><br>
<i>"""single line comment""" </i><br>
<hr>

<b>input IN python</b><br>

<i>input() statement is used to accet value (using Keyboard) form user</i><br>
input always take String input so we must convert int for int value<br>

<i>name= input("name: ")</i><br>
<i>age= int(input("age: "))</i><br>

<hr>

# condtion Statements

## chapter 6

if-elif-else(SYNTAX)<br>
if else and elif statement are thr multway decision taken by our program dur yo certaint condtions in out cord<br>

if(condition):<br>
    Statement1<br>
elif(condition):<br>
    Statement2<br>
else:<br>
    StatementN<br>  

and<br>
<b>single Line if / Ternary Operator</b><br>
<i> var = val1 if condition else  val2 </i>

Example<br>
food =input("food : ")<br>
eat = "yes" if food == "cake" else "no"<br>
print(eat)<br>

<i> str1 =if condition else str2 </i>
food = input("food: ")<br>
print("sweet")if food=="cake" or food == "jalebi" else print("not sweet")<br>

<b>Clever if / Ternary Operator</b><br>

<i>var = (false_val, true_val)[ condition]</i><br>

example<br>

age= int (intput("age:"))<br>
vate=("yes","no")[ age>= 18]<br>
print(vate)<br>
<br>
sal = float(intput("salary: "))<br>
tax =sal*(0.1, 0.2)[sal<= 50000]<br>
prnt(tax)
<br>
<hr>
<b>Type Of Operatores</b><br>
<i>An Opertor is a symbol that performs  acertain operation between operands</i><br>

<b>Arithmetic Operators <b> (+, -, *, /, %, **) ** is power Operators<br>
<b>Relational / Comparison Operators <b> (==, !=, >, <, >=, <=)<br>
<b>Assignment Operators <b>(=, +=,-=, *=,/=, %=, **/)<br>
<b>Logical Operators <b>(not, and, or)<br>
<hr>
<b>Type Conversion</b>
Python defines type conversion functions to directly convert one data type to another which is useful in day-to-day and competitive programming. <br>
There are two types of Type Conversion in Python:<br>

Python Implicit Type Conversion<br>
Python Explicit Type Conversion<br>

<b>Implicit Type Conversion</b><br>
<i>In Implicit type conversion of data types in Python, the Python interpreter automatically converts one data type to another without any user involvement.</b><br>
a=2<br>
b=4.25<br>
sum=a+b<br>
print(sum)<br>


<b>Explicit Type Conversion in Python</b>
<i>>In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement. With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type.  </i><br>

int(a, base): This function converts any data type to an integer. ‘Base’ specifies the base in which the string is if the data type is a string.<br>
float(): This function is used to convert any data type to a floating-point number. <br>

a="2"<br>
b=4<br>
sum=int(a)+b<br>
print(sum)<br>

a="Krishna"<br>
b=4<br>
sum=int(a)+b<br>
print(sum)<br>
<i>it give error</i><br>

<hr>
<b>String Method</b><br>
<string>concatenation</string><br>
"hello" + "world!" ----> "helloworld!"<br>
<string>length(len()) of string</string><br>
len(str) ----> length of String in number<br>
str="i am learning python"<br>
print(str[0])---> i<br>
<string>str.endwith(str) </string><br>
return true if string ends with substr<br>
<string>str.capitalize() </string><br>
capitalize 1st char<br>
<string>str.replace(old,new) </string><br>
replace all occurrences of old with new<br>
<string>str.find(word) </string><br>
return 1st index of 1st occurrence<br>
<string>str.count(str) </string><br>
count the occurrence of substr in string<br>
<hr>

# List & Tubles

## chapter 4

<b>List</b>:- A built-in data type that stores set of value<br>
list can store element of differenet type(int.float,string,etc)<br>


list2=[26,10.9,3,26102003]<br>
print(list2)<br>
print(type(list2))<br>
list2.sort()<br>
list2.reverse()<br>
list2.append(299)<br>
list2.insert(3,5)<br>
list2.pop()<br>
list2.remove(26)<br>


list2=[26,10.9,3,26102003]<br>
print(list2)<br>
print(type(list2))<br>
list2.sort()<br>
list2.reverse()<br>
list2.append(299)<br>
list2.insert(3,5)<br>
list2.pop()<br>
list2.remove(26)<br>
print(list2)<br>
list=[85,94,76,63,48]<br>
<i>list can work as string</i><br>
print(list[::-1])-->[48, 63, 76, 94, 85]<br>
print(list[-5::2])-->[85, 76, 48]<br>


<b><i>list method</i></b><br>
list =[2,1,3]<br>
<b>list.append(4)</b>:- adds one at the end [2,1,3,4]<br>
<b>list.sort()</b>:- sort in ascening order [1,2,3,4]<br>
<b>list.sort(reverse= True)</b>:- sort in deascening order [4,3,1,2]<br>
<b>list.reverse()</b>:- reverse list [4,3,1,2]<br>
<b>list.insert(idx,el)</b>:- insert element at index<br>
<br>
<b>list.remove(1)</b>:- remove first occurrence of element [2, 3]<br>
<b>list.pop(idx)</b>:- remove element at idx<br>

## Tuples in python

<b>Tuples</b>:- A Tuples is an Immutable data type in python<br>
A built-in datatype that lets us create immutable sequence of value<br>

tuplenumber=(26,10,20,3,20)<br>
print(type(tuplenumber))<br>
print(tuplenumber)<br>
<b>List method</b><br>
print(tuplenumber.count(20))<br>
print(tuplenumber.index(10))<br>

<i>single element tuple</i>
tup=(1,)<br>
print(type(tup))<br>

<hr>

# Dictionary & set

<b>Dictionary</b>:- Dictionary is a collection of key-value pairs<br>
they are unordered, mutable(changeable) & don't allow duplicate keys<br>

a = {<br>
"kkv" : "i'm krishna vishwakarma" ,<br>
"san" : "my name sangam vishwakarma",<br>
22:[2,3,0,8],<br>
"hey":[90.3,44,77]<br>
}<br>

print(a) --->{'kkv': "i'm krishna vishwakarma", 'san': 'my name sangam vishwakarma', 22: [2, 3, 0, 8], 'hey': [90.3, 44, 77]}<br>
print(type(a))---> < class 'dict'><br>
print(a['kkv']) --> i'm krishna vishwakarma<br>

print(a.items())-->dict_items([('kkv', "i'm krishna vishwakarma"), ('san', 'my name sangam vishwakarma'), (22, [2, 3, 0, 8]), ('hey', [90.3, 44, 77])])<br>

for a,b in a.items():<br>
    print(a,"=:",b)--->kkv =: i'm krishna vishwakarma   <br>
                        san =: my name sangam vishwakarma<br>
                        22 =: [2, 3, 0, 8]<br>
                        hey =: [90.3, 44, 77]<br>

print(a.keys())-->dict_keys(['kkv', 'san', 22, 'hey'])<br>
for p in a.keys():<br>
    print(p)-->kkv<br>
                san<br>
                22<br>
                hey<br>
<hr>
<b>Dictionary method</b><br>
<b>myDick.keys()</b> returns all keys<br>
<b>myDick.values()</b> return all values<br>
<b>myDick.items()</b> return all key value oairs as tuples <br>
<b>myDick.get()</b> return the key according to value<br>
<b>myDick.update(newDict)</b> insert the specified item to the dictionary<br>

a.update({"sng":"krishna",9:90,'ke':"EE"})<br>

# set
<b>Set</b> :- set is the collection of the unordered items.<br>
Each element in the set must be unique & immutable.<br>

sets={22,1,2,3,1}<br>
print(sets)<br>
print(type(sets))<br>
print(len(sets))<br>

<i>empty Set</i>
collection={}--> this is empty Dictionary not set<br>
collection=set()--> this is empty set<br>

<b>set method</b> 
<b>set.add(e)</b> add an element<br>
<b>set.remove(el)</b> remove the eleme an<br>
<b>set.clear()</b> empties the set<br>
<b>set.pop()</b> remove a random value<br>
<b>set.union({})</b> return a new set will all item from both set<br>
<b>set.intersection({})</b> return a new set whitch contain only item int both set<br>

sets.remove(3)<br>
print(sets.pop())<br>
print(sets)<br>
print(sets.pop())<br>
print(sets)<br>
print(sets.pop())<br>
print(sets)<br>
sets.clear()<br>

print(sets.union({4,5,6,4}))<br>
print(sets.intersection({22,2,1,9,0,9}))<br>


# Loops
## chapter 7
sometime we want to repeat a set of statements in our program for instace Print 1 to 1000<br>
loops make it easy for a programmer to tell the computer which set of instruction to repeat and How!<br>

<i>Type of loops</i><br>
<i>while</i><br>
<i>for</i><br>

<b>while</b>:- <br>
Syntax of while loop:-<br>
<i>while <b>condition</b>: </i><br>
    #body of the loop<br>


i=0<br>
#using while loop <br>
while i<10:<br>
    print ("hello  " + str(i))<br>
    i=i+1<br>


i=0<br>
using while loop <br>
while i<50:<br>
    print (i)<br>
    i=i+1<br>

fruits=['banana','orange','mangoes','greps','papaya']<br>
i=0<br>
while(i<len(fruits)):<br>
    print(fruits[i])<br>
    i=i+1<br>

i=50<br>
using while loop (reverxe) <br>
while i>0:<br>
    print (i)<br>
    i=i-1<br>

<b>for</b>:- <br>
A for loop is used to iterate throught a sequence the list tuple or string[iterables]<br>

the syntax of a for loop looks like this:-<br>

l=[1,7,8]<br>
for i in l:<br>
    print(i)<br>
    <br>

fruits=['banana','orange','mangoes','greps','papaya']<br>
for i in fruits:<br>
    print(i)<br>

for i in range(7):<br>
    print(i)<br>
print(range(1,9))<br>

<b>Range function</b>:- <br><i>
the range function in python is used to generate a sequence of number.  we can also specify the state, stop and Stap_size as follows.<br></i>
range[star,stop,steps_size]<br>

<b>for with else</b>:- <br>
<i>An optional else can be ued a for loop if the code is to be executed when the loop exhausts<br>
</i>

for i in range(10):<br>
    print(i)<br>
else:<br>
    print("yes")<br>
<br>
<br>
for i in range(9):<br>
    print(i)<br>
    if(i==3):<br>
        break<br>
else:<br>
    print("hello")<br>
    <br>
for i in range(8):<br>
    if(i==5):<br>
        continue<br>
    print(str(i))<br>
    <br>
i=9<br>
if i >0:<br>
    pass<br>
print ("helo")<br>
while i>0:<br>
    pass<br>
print(<br>
    "he;llp"<br>
)<br>


<b>Breack & continue % pass</b><br>
<i>
break:- used to terminate the loop when encountered<br>
continue :- terminates execution in the current iteration & continues executoin of the loop with the next iteratoin.<br>
pass :- pass is a null statement in pythan it instructs to "do nothing"<br></i>


for i in range(9):<br>
    print(i)<br>
    if(i==3):<br>
        break<br>

for i in range(8):<br>
    if(i==5):<br>
        continue<br>
    print(str(i))<br>

# Function & recursion
## chapter 8


<b>Function :- </b> a function is a group of statement performing a specific task.<br>
when a program is gets bigger in size and its complexity grous, it get difficult for a programmer to keep track on which piece of code is doing what!.<br>

a Functon can be recused by the programmer in a given program any number of.<br>

<b>Syntax :-</b><br>
def fun1():<br>
    #function body<br>

<br>
def fun1(param1,param2):<br>
    #function body<br>
<br>
function_name(arg1,arg2) #function call<br>

<b>Function call</b><br>

Wherever we want to call a function we put the name og the function followed y parenthesis as follwe<br>

function_name(arg1,arg2) #function call<br>

<b>Function definition</b><br>

the part containing  the exact set of instructions which are executed during the function call<br>

<hr>

def greet(name):<br>
    print("Good Day "+ name)<br>
<br>
greet("keishan")<br>
<hr>
def sum1(mark1):<br>
    sum=(((mark1[0]+mark1[1]+mark1[2]+mark1[3])/400)*100)<br>
    return(sum)<br>
<br>
mark3=[98,78,99,44] <br>
parentage=sum1(mark3)<br>
print(parentage)<br>
<br>
mark2=[98,44,55,77] <br>
parentage=sum1(mark2)<br>
print(parentage)<br>

<b>With out function</b><br>
mark1=[98,78,99,44]<br>
parcentage=((sum(mark1)/400)*100)<br>
print(parcentage)<br>


<i>
<b>Function type in python</b><br>
<b>Built-in Functions</b> :- Already present in python like:- len(),print(),type(), range()<br>
<b>User Defined Functions</b> :- Defined by the user<br>
</i>


<hr>
<b>Redursion:-</b><br>
When a function calls itself repeatedly.<br>
factorial(n)=n*factorial(n-1)<br>

recursion <br>
 n!=1*2*3*...*n<br>
<br>
def fectorial(num):<br>
    if num==0:<br>
        return 1<br>
    else:<br>
        return (num*fectorial(num-1))<br>
    <br>
num =int(input())<br>
i=fectorial(num)<br>
print(i)<br>

# Filo i/o  
## chapter 9

File Input/Outpt<br>

<i>Python can be used to perform operations on a file (read & write data)</i><br>

<b>The random Access memory is volatile all its contents are lost once the program termintes in order to persist the data forever, we use File</b>
<br>

<b>Type of all files</b><br>
1 Text Files : .txt, . docx, .log etc<br>
2 binary Files : .mp4,.mov, .png, .jpeg etc.<br>


<b>Open, Read & close File </b><br>
we have to open a file before reading or writing.<br>

<i><b>
f= open("file_name", "mode")<br><br>

file_name = sample.txt, demo.docx<br>

mode = r : read mode,  w: weite mode<br>

data = f.read()<br>
f.close()<br>
</b></i>

<br>

f=open("this.txt","r")  #read the file <br>
hi=f.read() #reade all date of file<br>
print(hi)<br>
print(type(hi))<br>
f.close()<br>

<i><b>
<br>
r : open for reading (default)<br>
x : create a new file and open it for writing <br>
a : open for writing, appending to the end of the file if it exists <br>
b : binary mode <br>
w : open for writing , trucating the file first <br>
t : text mode (default) <br>
" + " : open  disk file for updating(reading and writing) <br>

<u>node: if you open binary file so write wb,rb,ab in open file mode</u><br>
</b></i>

<b> Reading a file </b><br>
data = f.read() # reads entire file<br>
data = f.readline()  # reads one line at a time<br>

<hr>

f=open("this.txt","r")  #read the file using readline <br>
hi=f.readline() <br>
print(hi) <br>
f.close() <br>


<b>write to a file</b></br>


f=open("this.txt","w") #write the file but before the write ,all data is cleare  <br>
f.write("hello krishna") # overwrite the entire data<br>
f.close() <br>

<b>append a file </b><br>

<b><i> file i/o with syntax </i></n> <br>


with open("this.txt","a")as f: <br>
   f.write("\n hello sangam") <br>
   f.write("i am genious") <br>

<br>




# OOPs
## chapter 10

To  map with real worls scenarios,  we started using Object in code<br>
This is called <i>OBJECCT ORIENTED PROGRAMMING</i> <br>

<i>
<b>
Class & Object in python </b></i>

Class is a blueprint for creating object<br>
<i>
#creating class<br>
class Student:<br>
    name="kk"<br>
<br>
#creating object (instance)<br>
<br>
s1=Student()<br>
print(s1.name)<br>
</i>
<br>


<b>Class</b><br>

A class is a user defined blueprint or prototype from which object are created. it represent the set of proparties and methods that are common to all object of one type.<br>

The syntax of a class look like this<br>
class Employee:<br>
    #methods<br>

<b>Object</b><br>
it is a basic unite of Object Oriented programming and represents reat life entities<br>
<br>
An object is an instantiation of a class. when class is defined a template (info) is defined. memory is allocated only after object instantiation.<br>

<b>__info__ function (constrator)</b><br>
All classes have a function called __info__(), which is always executed when the Object is being  intiated<br>

<i>
class Student:<br>
     #parameterized constructor<br>
    def __init__(self,fullName):<br>
        print("hello am constructor")<br>
        print(self)<br>
        self.name=fullName<br>
<br>
s1= Student("krishna")<br>
print(s1.name)<br>
</i>

the <b>self</b> perameter is a refernce to the current instance of the class, and is used access the veriables that belogs to the class.<br>

<b>Default constructor</b>
<i>
class Student:<br>
    def __init_subclass__(cls) -> None:<br>
        pass<br>
</i>


<b>Methods</b><br>

Methods are functions that belong to Objects.<br>

<i>
#creating class<br>
class Student:<br>
    name="anonymous"<br>
    #parameterized constructor<br>
    def __init__(self,fullName):<br>
        print("hello am constructor")<br>
        print(self)<br>
        self.name=fullName<br>

#creating object<br>
s1= Student("krishna")<br>
print(s1.name)<br>


<i>

#prectice 1

class student:<br>
    def __init__(self,name,subject1,subject2,subject3):<br>
        self.name = name<br>
        self.subject1 = subject1<br>
        self.subject2 = subject2<br>
        self.subject3 = subject3<br>
        print("ok")<br>
    def avg(self):<br>
        return ((self.subject1+self.subject2+self.subject3)/3)<br>
krishna = student("krishna",96,85,75)<br>
print(krishna.avg())<br>
</i>

<b>Static Methods</b><br>

Methods that don't use the self parameter (work at class level)

<i>
#prectice 1<br>
class student:<br>
    #Static methods<br>
    @staticmethod<br>
    def hello():<br>
        print("hello everone ")<br>
    def __init__(self,name,mark):<br>
        self.name = name<br>
        self.mark = mark<br>
        print("ok")<br>
    def avg(self):<br>
        sum =0<br>
        for i in self.mark:<br>
            sum += i<br>
        return ((sum)/3)<br>
    <br>
krishna = student("krishna",[96,85,75])<br>
<br>
print(krishna.avg())<br>
krishna.hello()<br>
</i>

<br>

Decorator allow us to wrap another functon i order to entend the behavoiur of the wrapped function , without permanently modifying it.

<br>

<b> Abstraction </b><br>
Hinding the implementation details of a class  and showing the essential features to the user. <br>
<hr>
<b> Ecapsulation </b><br>
wrapping data and functions into a single unite (object)<br>
<hr>

## chapter 10 -> programing2.py

<b>del Keyword</b><br>

<i>
del s1.name<br>
del s1 <br>
</i>



<b>private(linke) Attributes & methods </b><br>

Conceptual impplementation in pythan<br>
Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.<br>

<b>
<i>
class Account:<br>
        self.acc_no=acc_no<br>
    def __init__(self, acc_no, acc_pass):<br>
    def reset_pass(self, acc_new_pass):<br>
        self.__acc_pass=acc_pass #private Attribute(__(name of veriable))<br>
        self.__acc_pass=acc_new_pass<br>
        print(self.__acc_pass)<br>
        print("hello  name  enter the details")<br>
    def __hello(self):<br>
<br>
    def welcome(self):<br>
        self.__hello()    <br>
<br>
a1.welcome()<br>
a1=Account(1234,"abc")<br>
a1.reset_pass(123)<br>
print(a1.acc_no)<br>
a1.reset_pass('a')<br>
a1.reset_pass('a')<br>

</i>
</b>
<br>


<b>Inheritance</b><br>

When one class(child/ drived ) derives the properties & methods of another class ( parent / base).<br>

<i>
<b>
class Car:<br>
    ......<br>

class ToyotaCar( Car ):<br>
    ......<br>

<br>


Example<br>



class Car:<br>
    color="black"<br>
    @staticmethod<br>
    def start():<br>
        print("car started")<br>
    @staticmethod<br>
    def stop():<br>
        print("car stopped :")    <br>
class ToyptaCar(Car):<br>
    def __init__(self,name):<br>
        self.name = name<br>
car1 = ToyptaCar("fortuner")<br>
car2 = ToyptaCar("prius")<br>
<br>
print(car1.name)<br>
print(car1.color)<br>
print(car1.start())<br>


</b>
</i>



<b> Type of interitance </b><br>

single interitance<br>
multi-level interitance<br>
multiple interitance<br>






<b>multi-level interitance</b><br>
<i>
<b>


class Car:<br>
    @staticmethod<br>
    def start():<br>
        print("car started")<br>
    @staticmethod<br>
    def stop():<br>
        print("car stopped :")    <br>
class ToyptaCar(Car):<br>
    def __init__(self,barnd):<br>
        self.band = barnd<br>
    <br>
class Fortuner(ToyptaCar):<br>
    def __init__(self,type):<br>
        self.type=type<br>
<br>
car1 = Fortuner("EV")<br>
<br>
<br>
print(car1.type)<br>
print(car1.start())<br>
</b>
</i>



<b>multiple inheritance</b><br>


<b>
<i>

class A:<br>
    varA ="welcome to class A"<br>
<br>
<br>
class B:<br>
    varB ="welcome to class B"<br>
<br>
class C (A,B):<br>
    varC ="welcome to class C"<br>
<br>
c1=C()<br>
<br>
print(c1.varA)<br>
print(c1.varB)<br>
print(c1.varC)<br>

</i>
</b>


<b>Super method</b><br>


<b><i>


#super mrthod<br>
<br>
class Car:<br>
    def __init__(self,type):<br>
        self.type=type<br>
    @staticmethod<br>
    def start():<br>
        print("car started")<br>
    @staticmethod<br>
    def stop():<br>
        print("car stopped :")    <br>
class ToyptaCar(Car):<br>
    def __init__(self,name,type):<br>
        super().__init__(type)<br>
        super().stop()<br>
        self.name = name<br>
<br>
car1 = ToyptaCar("fortuner","EV")<br>
print(car1.name)<br>
print(car1.type)<br>
print(car1.start())<br>

</i></b>



<b>class method</b><br>

A Class mthod is bound to the class & receive the class as an implicit first argument<br>
Node - static can't access or modify class state & generally for utility.<br>

<i>
class student:<br>
    @classMethod<br>
    def college(cls):<br>
        pass<br>
</i>


<b>Example</b><br>

<i>
<b>
#classMethod<br>

class person:<br>
    name="anonymous"<br>
    # def chnageName(self,name):<br>
    #     # self.name=name<br>
    #     person.name=name #1st method of class method<br>
    #     self.__class__.name=name #2st method of class method<br>
<br>
    @classmethod<br>
    def chnageName(cls,name):<br>
        cls.name=name<br>
<br>
p1=person()<br>
p1.chnageName("krishna")<br>
<br>
print(p1.name)<br>
print(person.name)<br>
</b>
</i>

<b>propety method</b><br>

We use @property decorator on any method in the class to use the method as a property<br>

<i><b>

#propety method<br>
<br>
class student:<br>
    def __init__(self,phy,chem,math):<br>
        self.phy=phy<br>
        self.chem = chem<br>
        self.math=math<br>
    @property<br>
    def percentage(self):<br>
        return str((self.phy+ self.chem +self.math)/3)+"%"<br>
stu1= student(89,97,99)<br>
print(stu1.percentage)<br>
stu1.phy=86<br>
print(stu1.phy)<br>
print(stu1.percentage)<br>
<br>
</b></i>



<b>polymorphism<b> operator overloading<br>

when the same operoter is allowed to have different meaning according to the context.<br>

<b>Operatore & Dunder Function</b>

a+b #addition        a.__add__(b)<br>
a-b #subtraction     a.__sub__(b)<br>
a*b #multiplication  a.__mul__(b)<br>
a/b #division        a.__truediv__(b)<br>
a%b #addition        a.__mod__(b)<br>


<b>
<i>

#polymorphism<br>
<br>
class str:<br>
    def __init__(self,name):<br>
        self.name=name<br>
<br>
    def __add__(self,s2):<br>
        return self.name+" "+s2.name<br>
s1=str("krishna")<br>
s2=str("vishwakarma")<br>
s3=s1+s2<br>
print(s3)<br>

we can make more method <br>
</i>
</b>

