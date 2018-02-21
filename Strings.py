
         ----------------"Strings in Python"--------
 
>>> 'spam eggs'  #single quotes
'spam eggs'
>>> 'doesn\'t'  #use \' to escape the single quote ...
"doesn't"
>>> "doesn't"   #... or use double quotes instead
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> 
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> 
>>> 
>>> #   using print()function
>>> 
>>> 
>>> print('"Isn\'t," she said.')
"Isn't," she said.
>>> 
>>> p = 'First line.\nSecond line.'    # \n means newline
>>> p    # without print(), \n is included in the output
'First line.\nSecond line.'
>>> 
>>> print(p)   # with print(), \n produces a new line
First line.
Second line.
>>> 
>>> 
>>> print('C:\some\name')  # here \n means newline
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
>>> 
>>> 
>>> 
>>> print("""\
Usage: thingy [OPTIONS]
-h
-H hostname
""")
Usage: thingy [OPTIONS]
-h
-H hostname

>>> print("""\
Usage: thingy [OPTIONS]
      -h                  Display this usage message
      -H                  Hostname to connect to
""")
Usage: thingy [OPTIONS]
      -h                  Display this usage message
      -H                  Hostname to connect to

>>> # 3 times 'un', followed by 'ium'
>>> 
>>> 3 * 'un' + 'ium'
'unununium'
>>> 
>>> 
>>> 'Py' 'thon'
'Python'
>>> 
>>> prefix = 'Py'
>>> prefix 'thon'   # can't concatenate a variable and string literal
SyntaxError: invalid syntax
>>> ...
Ellipsis
>>> ('un' * 3) 'ium'
SyntaxError: invalid syntax
>>> 
>>> 
>>> prefix + 'thon'
'Python'
>>> 
>>> 
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]   #character in position 5
'n'
>>> 
>>> 
>>> 
>>> word[-1]   #last character
'n'
>>> word[-2]   # second-last character
'o'
>>> word[-6]
'P'
>>> 
>>> 
>>> 
>>> word[0:2]  # characters from postion 0(included) to 2
'Py'
>>> word[2:5]   # characters from postions 2(included) to 5
'tho'
>>> 
>>> 
>>> 
>>> word[:2] + word[2:]
'Python'
>>> 
>>> word[:4] + word[4:]
'Python'
>>> 
>>> 
>>> word[:2]   # characters from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # chatractes from position 4 (included) to the end
'on'
>>> word[-2:]   # charcters from the second-last (included) to the end
'on'
>>> 
>>> 
>>> 
>>> 
>>> word[42]    # the word only has 6 characters
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    word[42]    # the word only has 6 characters
IndexError: string index out of range
>>> 
>>> 
>>> 
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    word[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    word[2:] = 'py'
TypeError: 'str' object does not support item assignment
>>> 
>>> 'J' + word[1:]
'Jython'
>>> 
>>> 
>>> 
>>> word[:2] + 'py'
'Pypy'
>>> 
>>> 
>>> 
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
>>> 
