Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing--> used to access elements in string
a="I am in class"
a[8]+a[9]+a[10]+a[11]
'clas'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
#negative indexing
a="vizag is a city of destiny"
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a="simple is better than complex"
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]
'com'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work hard until you succeed"
a[10:15]
'until'
a[5:9]
'hard'
a[0:4]
'work'
a[16:19]
'you'
a[20:27]
'succeed'
b="time is very precious"
b[13:21]
'precious'
b[8:12]
'very'
b[0:4]
'time'
a="I love python"
a[-11:-7]
'love'
a[-6:-1]
'pytho'
a[-6:0]
''
a[-6:]
'python'
b="today is weekend"
b[-16:-11]
'today'
b[-10:-8]
'is'
b[-7:]
'weekend'
#striding
a="data science"
a[::}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a="machine learning"
a[::4]
'miln'
>>> a[::6]
'men'
>>> a[::2]
'mcielann'
>>> a[5:]
'ne learning'
>>> a[:9]
'machine l'
>>> a[::7]
'm n'
>>> a="cloud computing"
>>> a[1:11:2]
'lu op'
>>> a[2:14:4]
'ocu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dcmu'
>>> #negative striding
>>> a="python course"
>>> a[-1:-11:2]
''
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> a[8:4:2]
''
>>> a[4:8:2]
'o '
>>> a[-10:-5:-2]
''
>>> a[-8:-12:-2]
'nh'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
