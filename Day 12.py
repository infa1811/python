{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "f =open(r\"30_days_30_hour_operations.txt\",\"w+\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "37"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f.write(\"I have completed 10 days successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "f1 =open(r\"30_days_30_hour_operations.txt\",\"a+\") \n",
    "f1.writelines(\"Cherry S\")"
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
      "I have completed 10 days successfullyCherry S\n"
     ]
    }
   ],
   "source": [
    "f1 =open(r\"30_days_30_hour_operations.txt\",\"r\") \n",
    "print(f1.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "f1.close()"
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
f =open(r"30_days_30_hour_operations.txt","w+")
In [2]:
f.write("I have completed 10 days successfully")
Out[2]:
37
In [3]:
f.close()
In [4]:
f1 =open(r"30_days_30_hour_operations.txt","a+") 
f1.writelines("Cherry S")
In [5]:
f1 =open(r"30_days_30_hour_operations.txt","r") 
print(f1.read())
I have completed 10 days successfullyCherry S
In [6]:
f1.close()
