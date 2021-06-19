Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Q1.Create a function getting two integer inputs from user. & print the following:
num1= int(input("Enter the first value :"))
num2=int(input("Enter the second value: "))
signs=input("Enter '+' for addition , '-' for Subration ,'*' for multiplication, '/ for division'")

def math_function(num1,num2,sign):
    if sign == '+':
        print("Addition of num1 and num2 is ",str(num1+num2))
    elif sign == '-':
        print("Subraction of num1 and num2 is ",str(num1-num2))
    elif sign == '*':
        print("Multiplication of num1 and num2 is ",str(num1*num2))
    elif sign == '/':
        print("Division of num1 and num2 is ",str(num1/num2))
math_function(num1,num2,signs)
#----------------------------------------------------------------------------------------------------------------------------------------

#Q2. Create a function covid( )& it should accept patient name, and body temperature, by default the body temperature should be 98 degree
def covid(name,temp):
    print("Enter name",name)
    if temp=='':
        print("Temp is:98")
    else:
        print("Temp is :",temp)

name = input("Enter name ")
temp=input("Enter temp")
covid(name,temp)