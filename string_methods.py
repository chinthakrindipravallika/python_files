Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="python"
a.find("h")
3
a[3]
'h'
a.find("n")
5
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tcollege\nmailid\tbranch"
print(a)
name
mobileno	college
mailid	branch
b="name:pravallika\nmobileno:123456789\tcollege:acharya nagarjuna university\nmailid:pravallikaa@gmail.com\tbranch:msc"
print(b)
name:pravallika
mobileno:123456789	college:acharya nagarjuna university
mailid:pravallikaa@gmail.com	branch:msc
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python c"
b.replace("c","dsa")
'python dsa'
print(a)
wait until you succeed
b=a.replace("wait","work")
print(b)
work until you succeed
#upper()
a="code"
a.upper()
'CODE'
#lower()
b="HELLO"
b.lower()
'hello'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'
#conditions
a="java"
a.isupper()
False
a.islower()
True
b="PYTHON"
b.isupper()
True
c="data science"
c.startswith("d")
True
c.endswith("e")
True
c.alnum()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    c.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
d=7896
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
f="6789"
f.isdigit()
True
e="pravallika123"
e.isalnum()
True
e.isdigit()
False
f="pravallika@123"
f.isalnum()
False
type(f)
<class 'str'>
#strip()

#lstrip(),rstrip()
a="      pravallika     "
a.strip()
'pravallika'
a.lstrip()
'pravallika     '
a.rstrip()
'      pravallika'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="pravallika"
lname="ch"
print(fname+lname)
pravallikach
print(fname+" "+lname)
pravallika ch
print(fname.title()+" "+lname.title())
Pravallika Ch
print((fname+" "+lname).title())
Pravallika Ch
#split()
a="c c++ python java"
a.split()
['c', 'c++', 'python', 'java']
b="i am learning python full stack"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
#join()
a="apple","banana","grapes"
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"l".join(a)
'applelbananalgrapes'
d="apple"
"l",join(a)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    "l",join(a)
NameError: name 'join' is not defined
"l",join(d)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    "l",join(d)
NameError: name 'join' is not defined
"l".join(d)
'alplpllle'
#formatting
a=3
b=6
print(a+b)
9
print("the sum is",a+b)
the sum is 9
city="vijaya"
print("city is",city)
city is vijaya
#format method()
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}",format(a,b))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print("hello {} hello {}",format(a,b))
ValueError: Invalid format specifier 'patlu' for object of type 'str'
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> print("hello {} hello {}".format(a,b)).title()
hello motu hello patlu
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print("hello {} hello {}".format(a,b)).title()
AttributeError: 'NoneType' object has no attribute 'title'
>>> print(("hello {} hello {}".format(a,b)).title())
Hello Motu Hello Patlu
>>> #fstring
>>> a="pravallika"
>>> b="ch"
>>> print(f"hello {a}{b}")
hello pravallikach
>>> print(f"hello {a} {b}")
hello pravallika ch
>>> print(f"hello {a} hello {b}")
hello pravallika hello ch
>>> print((f"hello {a}{b}").title())
Hello Pravallikach
>>> print((f"hello {a} {b}").title())
Hello Pravallika Ch
>>> a=2
>>> b=5
>>> print("product of two numbers",a*b)
product of two numbers 10
>>> print("product of two numbers:{}".format(a*b))
product of two numbers:10
>>> print(f"the product is {c}")
the product is data science
>>> print(f"product of two numbers:{a*b}")
product of two numbers:10
