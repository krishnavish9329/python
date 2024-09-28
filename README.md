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
