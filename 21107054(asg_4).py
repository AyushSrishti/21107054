{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "21107054(asg-4).ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMSDc65ISxHy8tR9CN8zKXB",
      "include_colab_link": true
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
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AyushSrishti/21107054/blob/main/21107054(asg_4).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-IpjA6MTl8Vb"
      },
      "outputs": [],
      "source": [
        "# Question 1\n",
        "\n",
        "# User Input\n",
        "marks = float(input('Enter your marks : '))\n",
        "\n",
        "# Condition for grading\n",
        "\n",
        "if marks<25:  \n",
        " print('Your grade is F')\n",
        "elif 25<=marks<45:\n",
        " print('Your grade is E')\n",
        "elif 45<=marks<50:\n",
        " print('Your grade is D')\n",
        "elif 50<=marks<60:\n",
        " print('Your grade is C')\n",
        "elif 60<=marks<=80:\n",
        " print('Your grade on B')\n",
        "elif 80<marks<=100:\n",
        " print('Your grade is A ')\n",
        "else: \n",
        " print('Please enter correct number of marks ')\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 2 \n",
        "\n",
        "# User input\n",
        "year = int(input('Enter the year : '))\n",
        "\n",
        "# Checking condition for leap year\n",
        "if (year%4==0 and year!=0):\n",
        " print(year,'is a leap year')\n",
        "elif (year%4==0 and year%100==0 and year%400==0):\n",
        " print(year,'is a leap year')\n",
        "else:\n",
        "  print(year,'is not a leap year')"
      ],
      "metadata": {
        "id": "A-UtSobxNC5N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 3 \n",
        "\n",
        "n = 10\n",
        "while(n>0):\n",
        "    n = n-1\n",
        "    import random\n",
        "\n",
        "    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
        "    num1 = random.choice(a)\n",
        "    num2 = random.choice(a)\n",
        "    print(num1, \"x\", num2)\n",
        "    answer = int(input(\"Enter the correct answer:\\n\"))\n",
        "    if answer == num1*num2:\n",
        "        print(\"Correct\")\n",
        "    elif answer != num1*num2:\n",
        "        print(\"Wrong!, the correct answer is \", num1*num2)\n",
        "    print(\"Number of tries left:\", n)\n",
        "\n",
        "print(\"Thank you for playing the game.\")\n"
      ],
      "metadata": {
        "id": "SOc35JlkQaTH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Question 4\n",
        "\n",
        "number=1\n",
        "while number<200:\n",
        "    if number%5 == 2 and number%6 == 3 and number%7 == 2:\n",
        "        print(\"The number of candies is : \" + str(number))\n",
        "    number = number + 1\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "eba6GeDdYwbv"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}