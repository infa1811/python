{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\lily\\anaconda3\\lib\\site-packages (1.1.3)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\lily\\anaconda3\\lib\\site-packages (from pandas) (2.8.1)\n",
      "Requirement already satisfied: numpy>=1.15.4 in c:\\users\\lily\\anaconda3\\lib\\site-packages (from pandas) (1.19.2)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\lily\\anaconda3\\lib\\site-packages (from pandas) (2020.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\lily\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "46"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randint(low =1, high=100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([44, 73, 10, 85, 30])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randint(low =1, high=100,size=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9223372036854775807"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sys\n",
    "sys.maxsize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['C:\\\\Users\\\\LILY',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\python38.zip',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\DLLs',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3',\n",
       " '',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib\\\\site-packages',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib\\\\site-packages\\\\win32',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib\\\\site-packages\\\\win32\\\\lib',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib\\\\site-packages\\\\Pythonwin',\n",
       " 'C:\\\\Users\\\\LILY\\\\anaconda3\\\\lib\\\\site-packages\\\\IPython\\\\extensions',\n",
       " 'C:\\\\Users\\\\LILY\\\\.ipython']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'-f'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.argv[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Skipping django as it is not installed.\n"
     ]
    }
   ],
   "source": [
    "pip uninstall django"
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
