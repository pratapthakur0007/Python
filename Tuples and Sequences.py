Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list(range(50))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> 
>>> 'a' in 'Pratap Singh'
True
>>> course = {'MCA','BCA'}
>>> 'MCA' in course
True
>>> 'BBA' in course
False
>>> 
>>> #  del statement
>>> 
>>> a = [-1, 1, 66.25, 33, 555, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 33, 555, 1234.5]
>>> 
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> 
>>> del a[:]
>>> a
[]
>>> 
>>> 
>>> # Tuples and Sequences
>>> 
>>> t = 123, 4352, 'Hello!', "Pratap"
>>> t
(123, 4352, 'Hello!', 'Pratap')
>>> 
>>> # Tuples may be nested
>>> 
>>> t[0]
123
>>> 
>>> t
(123, 4352, 'Hello!', 'Pratap')
>>> 
>>> # Tuples my be nested
>>> 
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((123, 4352, 'Hello!', 'Pratap'), (1, 2, 3, 4, 5))
>>> 
>>> # Tuples are immutable:
>>> t[0]
123
>>> t[0] = 7777
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t[0] = 7777
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v = ([1, 2, 3], [3, 2, 1])
>>> 
>>> empty = ()
>>> singleton = 'Hello',    # <-- note trailing comma
>>> len(empty)
0
>>> 
>>> len(singleton)
1
>>> singleton
('Hello',)
>>> 
>>> 
>>> 
>>> x, y, z = t
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x, y, z = t
ValueError: too many values to unpack (expected 3)
>>> 
