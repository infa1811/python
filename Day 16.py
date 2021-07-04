{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Task 16.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Qr65iGgoGJ_n"
      },
      "source": [
        "Create a lambda function that multiplies argument x with argument y\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yfwm3xdDGOJn",
        "outputId": "fba88897-4d55-4f6f-bc85-375e95b29de8"
      },
      "source": [
        "r = lambda x, y : x * y\n",
        "print(r(14, 4))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "56\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DVWtDNsgGfbm"
      },
      "source": [
        "**Write a Python program to create Fibonacci series to n using Lambda**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FffXdZLXGiXZ",
        "outputId": "fb6b61f1-2ff5-416a-b1c8-94f9ca2ee863"
      },
      "source": [
        "from functools import reduce\n",
        "  \n",
        "fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],\n",
        "                                 range(n-2), [0, 1])\n",
        "  \n",
        "print(fib(11))"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7K5JuF7fG0vb"
      },
      "source": [
        " **Write a Python program that multiply each number of given list with a given** **number**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8VyLOBzJG86i",
        "outputId": "55492028-0ba8-4e8a-93c8-d2af7998cb27"
      },
      "source": [
        "nums = [2, 4, 6, 9 , 11]\n",
        "n = 2\n",
        "print(\"Original list: \", nums)\n",
        "print(\"Given number: \", n)\n",
        "filtered_numbers=list(map(lambda number:number*n,nums))\n",
        "print(\"Result:\")\n",
        "print(' '.join(map(str,filtered_numbers)))"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Original list:  [2, 4, 6, 9, 11]\n",
            "Given number:  2\n",
            "Result:\n",
            "4 8 12 18 22\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pU8BYIJ0HfpM"
      },
      "source": [
        "** Write a Python program to find numbers divisible by 9 from a list of numbers**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sLEGCkmNHOJJ",
        "outputId": "54d75343-d092-4180-ed0c-e1b3c5581d31"
      },
      "source": [
        "list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]\n",
        "print(list1)\n",
        "list2=list(map(lambda j:j%9==0,list1))\n",
        "print(\"Result\")\n",
        "print(' '.join(map(str,list2)))\n",
        "list2=list(filter(lambda j:j%9==0,list1))\n",
        "print(\"Result\")\n",
        "print(' '.join(map(str,list2)))"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]\n",
            "Result\n",
            "False False False False False False True False False False False True True True\n",
            "Result\n",
            "9 27 36 81\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NSR16O4uH20i"
      },
      "source": [
        "**Write a Python program to count the even numbers in a given list of integers**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aFouPf6IH7M2",
        "outputId": "bfd24e6f-ca03-41ee-e1f1-2039a68cb685"
      },
      "source": [
        "list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]\n",
        "print(list1)\n",
        "list2=list(filter(lambda j:j%2==0,list1))\n",
        "print(\"Result :\")\n",
        "print(len(list2))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]\n",
            "Result :\n",
            "7\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}


Create a lambda function that multiplies argument x with argument y

In [1]:
r = lambda x, y : x * y
print(r(14, 4))
56
Write a Python program to create Fibonacci series to n using Lambda

In [2]:
from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])
  
print(fib(11))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Write a Python program that multiply each number of given list with a given number

In [3]:
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))
Original list:  [2, 4, 6, 9, 11]
Given number:  2
Result:
4 8 12 18 22
Write a Python program to find numbers divisible by 9 from a list of numbers

In [4]:
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(map(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
list2=list(filter(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]
Result
False False False False False False True False False False False True True True
Result
9 27 36 81
Write a Python program to count the even numbers in a given list of integers

In [5]:
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(filter(lambda j:j%2==0,list1))
print("Result :")
print(len(list2))
[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]
Result :
7
