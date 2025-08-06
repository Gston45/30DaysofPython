'''
┌──(err0r404㉿Err0r404)-[~]
└─$ python                      
Python 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello word'
  File "<python-input-0>", line 1
    print 'hello word'
    ^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello word')
hello word
>>> print(age)
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    numbers[5]
    ~~~~~~~^^^
IndexError: list index out of range
>>> numbers[3]
4
>>> import maths
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>> users = {'name': 'Asab', 'age' :250, 'country': 'Finland'}
>>> users['country']
'Finland'
>>> users['county']
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    users['county']
    ~~~~~^^^^^^^^^^
KeyError: 'county'
>>> 4 + '3'
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    4 + '3'
    ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>> from math import power
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2, 3)
8.0
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'
>>> 1/0
Traceback (most recent call last):
  File "<python-input-22>", line 1, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
>>> 

'''