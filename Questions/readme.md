# Problem set Descriptions

### Swap
Write an algorithm that takes 2 integers as input and saves them into two variables, then swaps those variables (exchanges their values) __without using any extra variable__.

### Fibonacci sequence
Write an algorithm that outputs Fibonacci numbers less than 106.
(Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, …)
```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### Divisors
Write an algorithm that takes a number as input and outputs all of its divisors.

### _n Square_
Write an algorithm that takes a number as input and outputs all of its divisors.
```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### Date Gap
Write an algorithm that takes a number as input and outputs all of its divisors.

```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### Minimum Coins
Assume we have unlimited numbers of 50, 20, 10, 5, 2 and 1 dollar’s coins. Write a python program that takes a price as input and calculates the minimum number of coins required to pay that price.
```
Input:
>>> 178
Output:
7
(Note: 3 $50 coins, 1 $20 coin, 1 $5 coin, 1 $2 coin and 1 $1 coin.)
Input:
>>> 36
Output:
4
(Note: 1 $20 coin, 1 $10 coin, 1 $5 coin and 1 $1 coin.)
```

### Palindrome
Write a python program that gets a non-negative number as input and prints “Yes” if the number is palindrome, otherwise it prints “No”.

```
Input:
>>> 12321
Output:
Yes
Input:
>>> 258
Output:
No
```

### Binary 2 Decimal
Write a python program that takes two number as input, a base and a number in that base, and prints the number’s value in decimal.
(Note: The number is positive and the base is a number between 2 and 9.)

```
Input:
Enter number:
>>> 10111
Enter base:
>>> 2
Output:
23
Input:
Enter number:
>>> 166
Enter base:
>>> 7
Output:
97
```

### GCD & LCM
The greatest common divisor (GCD) of two integers is the largest positive integer that divides the numbers without a remainder.
The least common multiple (LCM) of two integers is the smallest positive integer that is divisible by both numbers.
Write a python program that takes two nonzero integers as input and calculates their GCD and LCM and prints them.

```
Input:
>>> 8
>>> 12
Output:
GCD: 4
LCM: 24
```

### Sum Less than 10
Write a python program that takes a number as input and calculates the sum of its digits and continues calculating and printing its sum of digits until it reaches a number lower than 10.
(Note that the input number can be negative. You can simply ignore its sign.)

```
Input:
>>> 5896
Output:
28 # Note: 5 + 8 + 9 + 6 = 28
10 # Note: 1 + 0 = 1
1 # Note: 1 < 10
```

### Nice numbers
###### Part I
A number is considered nice if number of its odd divisor is even.
Write function that takes a number as argument and returns True if the argument is nice and returns false otherwise.

```
Input:
>>> 6
Output:
True #Note: 1, 2, 3, 6
Input:
>>> 9
Output:
False #Note: 1, 3, 9
```
###### Part II
Write a function that takes numbers from input until the user enters a nice number and returns the nice number.
```
Input:
>>> 8
>>> 9
>>> 12
Output:
12
Input:
>>> 7
Output:
7
```

### Function Writing
For a positive integer n let's define a function f:
f(n) = n|(- 1 + 2 - 3 + .. + (( - 1)^n)n)| (f(3) = 3|(-1 + 2 -3)| = 6)
Write a function that takes a number as its argument and returns f(n).

```
Input:
>>> 3
Output:
6
```

### Digit Counter
Write a function that takes a number as its argument and returns the number of 1s in its digits.
```
Input:
>>> 1587321656131
Output:
4
```

### Nice + Digit
Write a program that use above functions and takes numbers from user until the user enters a nice number and prints number of 1s in f(n) digits.

```
Input:
>>> 1
>>> 8
>>> 4
>>> 6
Output:
1 #Note: f(6) = 18
Input:
>>> 1
>>> 2
>>> 12
Output:
0 #Note: f(12) = 72
```

### Guess the number
Write a python program that guess the number user has selected. At first, the program gets a positive integer n from user. User selects a number k (1 <= k <= n) in his mind. The program guesses a number g and prints g. Then user should enter 1, 0 or -1. 1 means k is greater than g, -1 means k is lower than g and 0 means k is equal to "g". The program continues guessing until k is equal to g (that means finding the number) and prints the number.

```
Example:
Enter n: 15
8 1
12
-1
10
-1
The number is 9
Example
Enter n: 100
50
0
The number is 50
```
### Printer
###### Part  I : Forward Backward
Define a function that takes a number n as parameter and prints “1 2 3 … n … 3 2 1”.
```
Input:
>>> 4
Output:
1 2 3 4 3 2 1
```

###### Part  II : Space Printer
Define a function that takes a number n as parameter and prints “ “ n times. (“ “ is space character).

###### Part  III : Diamond
Define a function that takes a number n as parameter and uses the above functions to draw a numeric rhombus like the example below.

```
Input:
>>> 4
Output:
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
    1 2 3 2 1
      1 2 1
        1
```

### An Experiment
An experiment is defined as follows:
Drop a ball from an initial height and calculate the total distance traveled by the ball after a certain number of bounces. The bounciness of the ball determines how high it bounces when dropped from a particular height. For example, a ball with bounciness of 0.5, will bounce 5 feet high after being dropped from a height of 10 feet. Define a function that takes three inputs: the initial height, the bounciness of the ball and number of bounces. The return value of the function should be the total distance traveled by the ball.


```
Input:
10, 0.5, 2
Output:
22.5 #Note: 10 + 5 + 5 + 2.5
Input:
20, 0.2, 3
Output:
29.76 #Note: 20 + 4 + 4 + 0.8 + 0.8 + 0.16
```
