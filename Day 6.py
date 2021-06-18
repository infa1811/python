Q1. Write a Python script to merge two Python dictionaries

#Creating 2 dictionaries
dict1={'s':1,'h':2,'e':3,'f':4}
dict2={'b':5,'c':6,'d':7,'a':8}

res = {**dict1,**dict2}
print("After merge: ",res)

#-------------------------------------------------------------------------------------------------

#Q2. Write a Python program to remove a key from a dictionary

dict1.pop('e')
print(dict1)

#-------------------------------------------------------------------------------------------------

#Q3. Write a Python program to map two lists into a dictionary 

D1=['Radhe','Raghav','Rama','Rutam']
D2=[10,11,12,13,14]

res = {}
for key in D1:
    for value in D2:
        res[key]=value
        D2.remove(value)
        break
print("Dictionary=",str(res))

#---------------------------------------------------------------------------------------------------

#Q4. Write a Python program to find the length of a set

print("Length: ",len(D1))

#----------------------------------------------------------------------------------------------------

#Q5 Write a Python program to remove the intersection of a 2nd set from the 1st sets

d1={10,11,12,13,14,15}
d2={14,15,20,30,40,50}
print(d1.intersection(d2)) 
