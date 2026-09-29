Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=9.8
type(b)
<class 'float'>
c=[9.8]
type(c)
<class 'list'>
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
print(a)
['python', 'java', 'c', 'c++', ['ml', 'ai']]
a=["ds","ai"]
a.extend(["c","c++"])
a
['ds', 'ai', 'c', 'c++']
#insert()
b=["python","java","c"])
SyntaxError: unmatched ')'
b.insert(1,"ds")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b.insert(1,"ds")
AttributeError: 'float' object has no attribute 'insert'
b=["python","java","c"]
b.insert(1,"ds")
b
['python', 'ds', 'java', 'c']
#index
a=["hyd","vij","vzg"]
a.index("vzg")
2
a.copy()
['hyd', 'vij', 'vzg']
b=a=a=["hyd","vij","vzg"]
b
['hyd', 'vij', 'vzg']
c=a.copy()
c
['hyd', 'vij', 'vzg']
#sort
a=["mango","apple","grapes","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[7,5,9,3,0,1,20,30,25]
b.sort()
b
[0, 1, 3, 5, 7, 9, 20, 25, 30]
a=["grapes","Mango","Apple","berry","Banana"]
a.sort()
a
['Apple', 'Banana', 'Mango', 'berry', 'grapes']
b=["Kiwi","apple","Banana","berry","dragon","Grapes"]
b.sort()
b
['Banana', 'Grapes', 'Kiwi', 'apple', 'berry', 'dragon']
#reverse()
a=["black","white","red","blue"]
a.reverse()
a
['blue', 'red', 'white', 'black']
b=[4,7,8,2,6,8]
b.reverse()
b
[8, 6, 2, 8, 7, 4]
#pop()
a=["java","ds","ai"]
a.pop()
'ai'
a
['java', 'ds']
a.pop("java")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.pop("java")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0)
'java'
a
['ds']
a.remove("ds")
a
[]
b=["chair","table"]
b.clear()
b
[]
c=[]
c.append("pooja")
c
['pooja']
a=["hi","hello"]
len(a)
2
b="hello"
len(b)
5
c=["hello"]
len(c)
1
a.count("hi")
1
#tuple()
a=(4,6.7,"pooja",8+9j,True,False)
type(b)
<class 'str'>
type(a)
<class 'tuple'>
a.count(8+9j)
1
a.index(True)
4
len(a)
6
a.count()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)
#sets{}--
a={3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 3, (8+9j), 6.7, 'python'}
type(a)
<class 'set'>
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.issubset(b)
False
b.issubset(a)
False
a={2,3,4,5,6,7,8}
b={5,6,7,8}
b.issubset(a)
True
a.issubset(b)
False
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
a={4,5,6,8,2,9,0,5,4,10}
print(a)
{0, 2, 4, 5, 6, 8, 9, 10}
#union
a={10,11,12,13,14,15}
b={14,15,16,17,18,19}
a.union(b)
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
a
{10, 11, 12, 13, 14, 15}
a={4,5,6,7,8,9}
b={8,9,10,11,12,13}
a.intersection(b)
{8, 9}
a={3,4,5,6,7}
b={6,7,8,9,10}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9, 10}
a
{3, 4, 5, 6, 7, 8, 9, 10}
b
{6, 7, 8, 9, 10}
b.update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10}
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.difference(b)
{8, 5, 6, 7}
b.difference(a)
{12, 13, 14}
#symmetric_difference
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 9, 10}
#difference_update
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference_update(b)
a
{4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10, 11}
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.intersection_update(b)
a
{9, 10, 11}
b.intersection_update(a)
b
{9, 10, 11}
#symetric_difference_update
a={10,20,30,40,50}
b={30,40,50,60,70}
a.symmetric_difference_update(b)
a
{20, 70, 10, 60}
b.symmetric_difference_update(a)
b
{50, 20, 40, 10, 30}
#pop and remove()
a={2,3,4,5,6,7}
a.pop()
2
a
{3, 4, 5, 6, 7}
a.remove(5)
aa.pop(7)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    aa.pop(7)
NameError: name 'aa' is not defined. Did you mean: 'a'?
>>> a.remove(5)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    a.remove(5)
KeyError: 5
>>> a
{3, 4, 6, 7}
>>> a.discard(3)
>>> a
{4, 6, 7}
>>> a={5,6,7,8,9,10}
>>> a.copy()
{5, 6, 7, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(60)
>>> b
{60}
>>> #isdisjointa={4,5,6,7,8}
>>> a={4,5,6,7,8}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
>>> #length()
>>> a={4,5,6,7,8,9}
>>> len(a)
6
>>> a.count(8)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    a.count(8)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
