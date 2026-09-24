Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b=7.8
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e='''code'''
type(e)
<class 'str'>
f=4+9j
type(f)
<class 'complex'>
g=2j+8
type(g)
<class 'complex'>
i=7j
k=9i
SyntaxError: invalid decimal literal
m="j"
type(m)
<class 'str'>
x=True
type(x)
<class 'bool'>
y=False
type(y)
<class 'bool'>
z=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    z=true
NameError: name 'true' is not defined. Did you mean: 'True'?
z="true"
type(z)
<class 'str'>
#data type conversions
int(8)
8
int(6.7)
6
int("hi")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(8+9j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(8+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(7)
7.0
float(8.9)
8.9
float("hello")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(6+8j)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(6+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(int)
"<class 'int'>"
str(float)
"<class 'float'>"
str(7)
'7'
str(5.6)
'5.6'
str(6+4j)
'(6+4j)'
str(True)
'True'
>>> str(False)
'False'
>>> complex(5)
(5+0j)
>>> complex(4.0)
(4+0j)
>>> complex("hi
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> complex("hi")
...         
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
>>> complex(True)
...         
(1+0j)
>>> complex(False)
...         
0j
>>> bool(6)
...         
True
>>> bool(6.8)
...         
True
>>> bool(6+8j)
...         
True
>>> bool(bool)
...         
True
>>> bool(True)
...         
True
>>> bool(False)
...         
False
