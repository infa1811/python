  
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bank_Account:\n",
    "    def __init__(self):\n",
    "        self.balance=0\n",
    "        print(\"Hello!!! Welcome to the Deposit & ATM Machine\")\n",
    "    def display(self):\n",
    "        print(\"\\n Net Available Balance=\",self.balance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Deposit(Bank_Account):  \n",
    "    def deposit(self):\n",
    "        amount=float(input(\"Enter amount to be Deposited: \"))\n",
    "        self.balance += amount\n",
    "        print(\"\\n Amount Deposited:\",amount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Withdraw(Bank_Account): \n",
    "    def withdraw(self):\n",
    "        amount = float(input(\"Enter amount to be Withdrawn: \"))\n",
    "        if self.balance>=amount:\n",
    "            self.balance-=amount\n",
    "            print(\"\\n You Withdrew:\", amount)\n",
    "        else:\n",
    "            print(\"\\n Insufficient balance  \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello!!! Welcome to the Deposit & ATM Machine\n"
     ]
    }
   ],
   "source": [
    "s = Bank_Account()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello!!! Welcome to the Deposit & Withdrawal Machine\n",
      "Enter amount to be Deposited: 25\n",
      "\n",
      " Amount Deposited: 25.0\n"
     ]
    }
   ],
   "source": [
    "p=Deposit()\n",
    "p.deposit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello!!! Welcome to the Deposit & Withdrawal Machine\n",
      "Enter amount to be Withdrawn: 16\n",
      "\n",
      " Insufficient balance  \n",
      "\n",
      " Net Available Balance= 0\n"
     ]
    }
   ],
   "source": [
    "q=Withdraw()\n",
    "q.withdraw()\n",
    "s.display()\n"
   ]
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

In [5]:
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & ATM Machine")
    def display(self):
        print("\n Net Available Balance=",self.balance)
In [2]:
class Deposit(Bank_Account):  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
In [3]:
class Withdraw(Bank_Account): 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
In [6]:
s = Bank_Account()
Hello!!! Welcome to the Deposit & ATM Machine
In [7]:
p=Deposit()
p.deposit()
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 25

 Amount Deposited: 25.0
In [8]:
q=Withdraw()
q.withdraw()
s.display()
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Withdrawn: 16

 Insufficient balance  

 Net Available Balance= 0
