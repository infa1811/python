In [1]:
import re
In [2]:
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
In [3]:
print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("1233@@#$$%$"))
True
False
In [5]:
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
In [6]:
print(end_num('abcdef12233'))
print(end_num('abcdef634556'))
print(end_num('abc'))
True
True
False
In [7]:
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 9, 11, and 222 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))
Number of length 1 to 3
1
9
11
222
In [8]:
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
In [9]:
print(text_match("Best Enlist."))
print(text_match("Python_Exercises_13"))
Not matched!
Found a match!
