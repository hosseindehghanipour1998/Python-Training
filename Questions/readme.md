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
