Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"pooja","year":2026,"month":9}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 9}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 9)])
a.values()
dict_values(['pooja', 2026, 9])
#accessing
a={"name":"pooja","city":"vij"}
a["name"]
'pooja'
a.get("name")
'pooja'
a
{'name': 'pooja', 'city': 'vij'}
a["pooja"]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a["pooja"]
KeyError: 'pooja'
a={"city":"via","state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("state")
'ap'
a
{'city': 'via', 'country': 'india'}
a.popitem()
('country', 'india')
a.update({"year":2026})
a
{'city': 'via', 'year': 2026}
a={"course":"python","duration":100}
a.update({"year":2026})
a
{'course': 'python', 'duration': 100, 'year': 2026}
a.update({"month":"sep"},{"date":30})
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.update({"month":"sep"},{"date":30})
TypeError: update expected at most 1 argument, got 2
a.update({"month":"sep","date":30})
a
{'course': 'python', 'duration': 100, 'year': 2026, 'month': 'sep', 'date': 30}
#setdefault
a={"date":30,"time":11}
a.setdefault("hour",11)
11
a
{'date': 30, 'time': 11, 'hour': 11}
a.setdefault(11,"hour")
'hour'
a
{'date': 30, 'time': 11, 'hour': 11, 11: 'hour'}
a={"colour":"white","food":"biryani"}
a.copy()
{'colour': 'white', 'food': 'biryani'}
len(a)
2
a.count("colour")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.count("colour")
AttributeError: 'dict' object has no attribute 'count'
a.index("food")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.index("food")
AttributeError: 'dict' object has no attribute 'index'
a.clear()
a
{}
a={"name":"pravallika","city":"via","name":"pravallika"}
print(a)
{'name': 'pravallika', 'city': 'via'}
a={"name":"pravallika","city":"via","name":"priya"}
a
{'name': 'priya', 'city': 'via'}
a={"name1":"pravallika","city":"via","name2":"pravallika"}
a
{'name1': 'pravallika', 'city': 'via', 'name2': 'pravallika'}
#one key multiple values
a={"idnos":10,20,30}
SyntaxError: ':' expected after dictionary key
a={"idnos":[10,20,30],"names":["ambica","anusha","pooja"]}
print(a)
{'idnos': [10, 20, 30], 'names': ['ambica', 'anusha', 'pooja']}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names'])
a.values()
dict_values([[10, 20, 30], ['ambica', 'anusha', 'pooja']])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['ambica', 'anusha', 'pooja'])])
#tasks
a=[9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,3,7,0]
a1=a[0:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:10]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a2.sort()
a2
[0, 3, 4, 6, 7]
a1.reverse()
a2.reverse()
a1
[9, 8, 5, 2, 1]
a2
[7, 6, 4, 3, 0]
c=a2.reverse+a1.reverse
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    c=a2.reverse+a1.reverse
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'builtin_function_or_method'
a2+a1
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
#task_2
a=["codegnan","python"]
#["CODEGNAN","PYTHON"]
print(a.upper())
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(a.upper())
AttributeError: 'list' object has no attribute 'upper'
b=str(a)
b
"['codegnan', 'python']"
b.upper()
"['CODEGNAN', 'PYTHON']"
#task_3
>>> a=[2,5,7,9,10,15]
>>> #output-[2,5,7,8,9,10,15]
>>> a.insert(3,8)
>>> a
[2, 5, 7, 8, 9, 10, 15]
>>> #task_4
>>> a=(10,20,30,40)
>>> #(10,20,30,40,50)
>>> b=str(a)
>>> b
'(10, 20, 30, 40)'
>>> b.append(50)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b.append(50)
AttributeError: 'str' object has no attribute 'append'
>>> b=list(a)
>>> b
[10, 20, 30, 40]
>>> b.append(50)
>>> bc=tuple(b)
>>> c
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    c
NameError: name 'c' is not defined. Did you mean: 'bc'?
>>> c=tuple(b)
>>> c
(10, 20, 30, 40, 50)
>>> #task_5
>>> a=[2,3,4,5,6]
>>> #[2,3,4,5,6,"c","o","d","e"]
>>> a.extend("code")
>>> a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e']
>>> a.extend(["code"])
>>> a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e', 'code']
>>> #swappimg of two variables
>>> a=10
>>> b=20
>>> #a->20,b->10
