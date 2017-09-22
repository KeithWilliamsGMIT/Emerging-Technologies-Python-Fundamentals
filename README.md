# Python Fundamentals Problem Sheet

This repository contains the solutions to the first problem sheet on python fundamentals, given as part of my fourth year [emerging technologies](https://emerging-technologies.github.io/) module in college. Note that the solutions to these problems were written in Python 3.5.

## Getting Started

Clone the repository and navigate to the root of the repository.
```
git clone https://github.com/KeithWilliamsGMIT/Emerging-Technologies-Python-Fundamentals.git
cd Emerging-Technologies-Python-Fundamentals
```

## 1. Hello, World!
*Problem:* Write a program that prints “Hello, world!” to the screen.

*Solution:*
```
python3 01-hello-world.py
```

## 2. Current time
*Problem:* Write a program that prints the current time and date to the console.

*Solution:*
```
python3 02-current-time.py
```

## 3. FizzBuzz
*Problem:* Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

*Solution:*
```
python 03-fizzbuzz.py
```

## 4. Factorial digit sum
*Problem:* Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

*Solution:*
```
python 04-factorial-digit-sum.py <number>
```

The number to calculate the factorial digit sum of should be passed in as an arguement. For example, the factorial digit sum of 100 is **648**.

## 5. Guessing game
*Problem:* Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

*Solution:*
```
python 05-guessing-game.py
```

When the game starts the user will be prompted to enter a guess. This guess should be a positive integer between 1 and 100 inlusive. If any other value is entered a message should inform the user of an incorrect input. After entering a valid guess the user will be informed whether it was too low, too high or correct. If correct the number of tries and a non-repeating list of guess is outputted. Otherwise, the user will be prompted for another guess. If the same guess is entered more than once a message will be outputted to inform the user. This guess is not included in the total number of tries.

## 6. Largest and smallest in list
*Problem:* Write a function that returns the largest and smallest elements in a list.

*Solution:*
```
python 06-largest-and-smallest.py <comma-separated-list-of-integer>
```

A comma separated list of integers should be passed in as the first command line argument. For example, by passing in 9,3,4,5,2,10 the expected result is that the smallest number is **2** and the largest number is **10**. If an invalid argument is given an "Invalid argument!" message will be displayed.

## 7. Palindrome test
*Problem:* Write a function that tests whether a string is a palindrome.

*Solution:*
```
python 07-palindrome.py "<phrase>"
```

The word to check for a palindrome should be passed in as the first command line argument. If it is a palindrome "True" will be outputted, for example, "kayak". Otherwise, "False" will be outputted, for example "car". Note that the phase can be **case insensitive** and can contain spaces. If no phrase is given a "No argument!" message will be shown.

## 8. Merge list and sort
*Problem:* Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

*Solution:*
```
python 08-merge-sorted-lists.py <sorted-list-1> <sorted-list-2>
```

Two comma separated list of integers should be passed in as the first and second command line arguments. For example, if the sorted lists 1,4,6 and 2,3,5,6 are passed in the expected result is [1,2,3,4,5,6,6]. Notice that duplicate entries are possible. If an invalid argument is given an "(n) Invalid argument!" message will be displayed where n is the index of the argument that caused the error. An error message would also occur if two lists weren't given as command line arguments.

## 9. Newton’s method for square roots
*Problem:* Implement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:

```
z_next = z - ((z*z - x) / (2 * z))
```

To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

*Solution:*
```
python 09-newton-square-root.py <number>
```

The number to approximate the square root for should be passed in as the first argument. This value should be a positive float greater than 0. For example, if 25 is passed in, the expected output should be 5 as follows.

```
newton_square_root(25.000000) = 5.000000
match.sqrt(25.000000) = 5.000000
```

The first value is the approximation of the square root using Newton's method. The second value is the result of using the sqrt() from the math library. This is only to show the accuracy of the approximation. If an invalid float is passed in an "Invalid number! Must be a positive number greater than zero!" message is outputted. If the argument is a string a "(1) Invalid argument!" message is outputted. If no argument is given a "No argument!" message is outputted.