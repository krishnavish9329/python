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


<i>1:57</i>