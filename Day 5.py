Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Q1. 1)	Write a program to create a list of n integer values and do the following
#Creating list of n integer values
s=7
t=[]
for i in range(s):
    x=int(input())
    t.append(x)

for i in t:
    print(i)

#Add an item in to the list (using function)
print("X=",t)
u=[20,30,40,50,60]
t+=u
print("New list",t)

#Delete (using function)
del t[3]
print(t)

#Store the largest number from the list to a variable
L_num = [100,200,300,400,500]
max_num=max(L_num)
print("Maximum number is: ",max_num)

#Store the Smallest number from the list to a variable
S_num=[94,47,36,77,12,3,55]
min_num=min(S_num)
print("Minimum number is: ",min_num)

#--------------------------------------------------------------------------------------------------
#Q2. Create a tuple and print the reverse of the created tuple

my_tuple =(10,50,60,20,40,90)
s=sorted(my_tuple)
print("Before reverse",my_tuple)
print("After reverse",sorted(my_tuple,reverse=True))

#--------------------------------------------------------------------------------------------------
#Q3. Create a tuple and convert it into list 

my_tuple = (10,50,60,20,40,90)
my_list = list(my_tuple)
print("After converting into list",my_list)