Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#Assignment operator-it always gives updated values
a=5
b=9
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
14
a-=3
a
11
a*=4
a
44
a/=3
a
14.666666666666666
a**=4
a
46272.79012345678
a%=4
a
0.7901234567834763
b+=3
a
0.7901234567834763
b
12
b-=6
b
6
b*=6
b
36
b**=4
b
1679616
b%=6
b
0
b//=5
b
0
#comparision operator
a=6
b=7
a<b
True
a>b
False
b>a
True
a<=b
True
b>=a
True
a=5
b=5
a==b
True
#logical operator
a=10
b=20
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>=a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=3
type(a) is int
True
type(a) is not int
False
type(a) is not float
True
type(a) is float
False
a=5.6
type(a) is float
True
type
<class 'type'>
9
type(a) is not float
False
type(a) is complex
False
type(a) is not complex
True
type(a) is string
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    type(a) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(a) is str
False
type(a) is not str
True
type(a) is bool
False
type(a) is not bool
True
#membership operator
a=2,3,4,5,6,7,8,9,10
2 in a
True
20 not in a
True
30 not in a
True
99 in a
False
#bitwise operator
a=3
b=6
a&b
2
bin(3)
'0b11'
bin(6)
'0b110'
>>> a=2
>>> b=4
>>> a|b
6
>>> a=5
>>> b=7
>>> a|b
7
>>> a=5
>>> -(a+1)
-6
>>> ~a
-6
>>> a=-8
>>> -(a+1)
7
>>> ~a
7
>>> a=3
>>> b=5
>>> a^b
6
>>> a=8
>>> b=10
>>> a^b
2
>>> a=4
>>> a<<2
16
>>> bin(4)
'0b100'
>>> a=8
>>> a<<3
64
>>> a>>6
0
>>> a=9
>>> a>>3
1
