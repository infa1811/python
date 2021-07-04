{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'list1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-4be8aa878477>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'list1' is not defined"
     ]
    }
   ],
   "source": [
    "list=10\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-46200ca448e7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'123'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0ms\u001b[0m\u001b[1;33m+=\u001b[0m\u001b[1;36m123\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "s='123'\n",
    "s+=123"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-acb202c31946>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-acb202c31946>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    for i range(1,10):\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "for i range(1,10):  \n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-8863d01b31ee>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-8863d01b31ee>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    in =456\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "in =456"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "56\n",
      "6\n",
      "7\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-1af7c3ce58a8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0ml\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m56\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "l=[1,2,3,4,5,56,6,7]\n",
    "for i in range(len(l)):\n",
    "    print(l[i+1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'modulexyz'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-278d43f9a72a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmodulexyz\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'modulexyz'"
     ]
    }
   ],
   "source": [
    "import modulexyz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-3ad380d27c2d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0md1\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0md1\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m13\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m14\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0md1\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m23\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'd' is not defined"
     ]
    }
   ],
   "source": [
    "d1=d()\n",
    "d1={1:12,11:12,13:14}\n",
    "print(d1[23])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'x' from 'math' (unknown location)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-7c042d96054e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmath\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'x' from 'math' (unknown location)"
     ]
    }
   ],
   "source": [
    "from math import x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'abc'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-2dda1cc00c48>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"abc\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'abc'"
     ]
    }
   ],
   "source": [
    "int(\"abc\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-e574edb36883>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;36m10\u001b[0m\u001b[1;33m/\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "10/0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate():\n",
    "    try:\n",
    "        print('+')\n",
    "        print('-')\n",
    "        print('*')\n",
    "        print('/')\n",
    "        print('%')\n",
    "        print('**')\n",
    "        operation = input(\"Select an operator:n\")\n",
    "        print(\"Enter two numbers\")\n",
    "        number_1 = int(input())\n",
    "        number_2 = int(input())\n",
    "        if operation == '+': \n",
    "            print(number_1 + number_2)\n",
    "        elif operation == '-': \n",
    "            print(number_1 - number_2)\n",
    "        elif operation == '*': \n",
    "            print(number_1 * number_2)\n",
    "        elif operation == '/': \n",
    "            print(number_1 / number_2)\n",
    "        elif operation == '%': \n",
    "            print(number_1 % number_2)\n",
    "        elif operation == '**': \n",
    "            print(number_1 ** number_2)\n",
    "        else:\n",
    "            print('Invalid Input')\n",
    "    except Exception as e:\n",
    "        print(e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+\n",
      "-\n",
      "*\n",
      "/\n",
      "%\n",
      "**\n",
      "Select an operator:n*\n",
      "Enter two numbers\n",
      "15\n",
      "2\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "calculate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name 'b' is not defined\n"
     ]
    }
   ],
   "source": [
    "\n",
    "try:\n",
    "    a = 123\n",
    "    if a==123:\n",
    "        print(b)\n",
    "        raise NameError(\"Name error\")\n",
    "    if a >0:\n",
    "        raise ValueError(\"Value error\")\n",
    "except NameError as ne:\n",
    "        print(ne)\n",
    "except ValueError as ve:\n",
    "    pritn(ve)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age: 70\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    age=int(input('Enter your age: '))\n",
    "except:\n",
    "    print ('You have entered an invalid value.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}


In [1]:
list=10
print(list1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-4be8aa878477> in <module>
      1 list=10
----> 2 print(list1)

NameError: name 'list1' is not defined
In [2]:
s='123'
s+=123
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-46200ca448e7> in <module>
      1 s='123'
----> 2 s+=123

TypeError: can only concatenate str (not "int") to str
In [3]:
for i range(1,10):  
    print(i)
  File "<ipython-input-3-acb202c31946>", line 1
    for i range(1,10):
          ^
SyntaxError: invalid syntax
In [4]:
in =456
  File "<ipython-input-4-8863d01b31ee>", line 1
    in =456
    ^
SyntaxError: invalid syntax
In [5]:
l=[1,2,3,4,5,56,6,7]
for i in range(len(l)):
    print(l[i+1])
2
3
4
5
56
6
7
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-5-1af7c3ce58a8> in <module>
      1 l=[1,2,3,4,5,56,6,7]
      2 for i in range(len(l)):
----> 3     print(l[i+1])

IndexError: list index out of range
In [6]:
import modulexyz
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-6-278d43f9a72a> in <module>
----> 1 import modulexyz

ModuleNotFoundError: No module named 'modulexyz'
In [7]:
d1=d()
d1={1:12,11:12,13:14}
print(d1[23])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-3ad380d27c2d> in <module>
----> 1 d1=d()
      2 d1={1:12,11:12,13:14}
      3 print(d1[23])

NameError: name 'd' is not defined
In [8]:
from math import x
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-8-7c042d96054e> in <module>
----> 1 from math import x

ImportError: cannot import name 'x' from 'math' (unknown location)
In [9]:
int("abc")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-9-2dda1cc00c48> in <module>
----> 1 int("abc")

ValueError: invalid literal for int() with base 10: 'abc'
In [10]:
10/0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-10-e574edb36883> in <module>
----> 1 10/0

ZeroDivisionError: division by zero
In [11]:
def calculate():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:n")
        print("Enter two numbers")
        number_1 = int(input())
        number_2 = int(input())
        if operation == '+': 
            print(number_1 + number_2)
        elif operation == '-': 
            print(number_1 - number_2)
        elif operation == '*': 
            print(number_1 * number_2)
        elif operation == '/': 
            print(number_1 / number_2)
        elif operation == '%': 
            print(number_1 % number_2)
        elif operation == '**': 
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)
In [12]:
calculate()
+
-
*
/
%
**
Select an operator:n*
Enter two numbers
15
2
30
In [13]:
try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)
name 'b' is not defined
In [14]:
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
Enter your age: 70
In [ ]:
