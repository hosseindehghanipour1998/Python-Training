# Problem set Descriptions

### 1 - Swap (Algorithm)
Write an algorithm that takes 2 integers as input and saves them into two variables, then swaps those variables (exchanges their values) __without using any extra variable__.

### 2 - Fibonacci sequence (Algorithm)
Write an algorithm that outputs Fibonacci numbers less than 106.
(Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, …)
```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### 3 - Divisors (Algorithm)
Write an algorithm that takes a number as input and outputs all of its divisors.

### 4 - _n Square_
Write an algorithm that takes a number as input and outputs all of its divisors.
```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### 5 - Date Gap
Write an algorithm that takes a number as input and outputs all of its divisors.

```
Input:
>>> 24
Output:
1 2 3 4 6 8 12 24
```

### 6 - Minimum Coins
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

### 7 - Palindrome
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

### 8 - Binary 2 Decimal
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

### 9 - GCD & LCM
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

### 10 - Sum Less than 10
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

### 11 - Nice numbers
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

### 12 - Function Writing
For a positive integer n let's define a function f:
f(n) = n|(- 1 + 2 - 3 + .. + (( - 1)^n)n)| (f(3) = 3|(-1 + 2 -3)| = 6)
Write a function that takes a number as its argument and returns f(n).

```
Input:
>>> 3
Output:
6
```

### 13 - Digit Counter
Write a function that takes a number as its argument and returns the number of 1s in its digits.
```
Input:
>>> 1587321656131
Output:
4
```

### 14 - Nice + Digit
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

### 15 - Guess the number
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
### 16 - Printer
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

### 17 - An Experiment
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

### 18 - Work With strings
Note: Write function of each question in a separate file and use import if you need to use that in other questions. __And do not use any functions of python string library__.
###### Part I : Contains
Define a function that takes two strings as parameters and returns the beginning index of the first occurrence of str2 in str1, or -1 if str2 is not in str1.

```
Function Parameters:
“hello world”
“world”
Return value:
6
Function Parameter:
“hello world”
“word”
Return value:
-1
```
###### Part II : Index Of
Define a function that takes a string as parameter and returns last index of its first word (words are separated by space).
```
Function Parameters:
“hello world”
Return value:
4
Function Parameter:
“my function”
Return value:
1
```

###### Part III : Reverse
Define a function (using the function in q2) that takes a string as its parameter,
reverses its words’ order and returns the result.
Note: Don’t forget to import the function and do not write it in this file again.
```
Function Parameters:
“hello I am testing this function!!!!”
Return value:
“function!!!! This testing am I hello”
Function Parameters:
“python”
Return value:
“python”
```

###### Part IV : Replace
Define a function that swaps first and last character of a string.
```
Function Parameters:
“hello”
Return value:
“oellh”
Function Parameters:
“ny functiom”
Return value:
“my function
```
###### Part V : Occurrence
Define a function (using functions in q1 and q2) that takes two strings and deletes all occurrences of second string in first one and returns the result.
Note: Do not forget to import functions from q1 and q2.
```
Function Parameters:
“word1 word2 word1 again word1 and word2”
“word1”
Return value:
“ word2 again and word2”
Function Parameters:
“my function”
“hello”
Return value:
“my function”
```

###### Part VI : Insert
Define a function that takes two strings and an integer as index and inserts second string in given index of the first one, adds to the end if index greater or equal to first string’s length. (you are not allowed to use string slicing: str[i:j])
```
Function Parameters:
“word1 word2”
“hello”
3
Return value:
“worhellod1 word2”
Function Parameters:
“hello my”
“friend”
8
Return value:
“hello myfriend”
```

### 19 - Work with Lists

###### Part I : String Counter
Define a function that takes a list of strings and count the number of strings in that list which the string length is 2 or more and the first and last character of that string are same.

```
Function Parameters:
[“abc”, “xyz”, “aba”, “1221”]
Return value:
2
```
###### Part II : Element Frequency
Define a function that takes a list as parameter and outputs the frequency of the elements in that list.

```
Function Parameters:
[1, 2, “python”, 2, 3, “hello”, “python”, 2]
output:
1: 1
2: 3
“python”: 2
3: 1
“hello”: 1
```

###### Part III : Element Contain
Define a function that takes two lists as parameters and returns True if they have at least one common member. (You are allowed to use ___in___ keyword).

```
Function Parameters:
[1, 2, 3]
[3, 4, 5]
Return value:
True
Function Parameters:
[1, [1,2], [1, 2, 3]]
[2, 3]
Return value:
False
```

###### Part IV : 3D Array
Define a function that takes m, n, p as parameters and returns an m*n*p 3D array which each element of that is ___*___.

```
Function Parameters:
2 3 2
Return value:
[
[[‘*’, ‘*’], [‘*’, ‘*’], [‘*’, ‘*’]],
[[‘*’, ‘*’], [‘*’, ‘*’], [‘*’, ‘*’]]
]
```

###### Part VI : Splitter
Define a function that takes two strings as parameters, splits the first string using
second one as delimiter, adds the tokens to a list and returns that list. Note: You are not allowed to use any functions or methods of python.

```
Function Parameters:
“hello,how,are you”
“,”
Return value:
[“hello”, “how”, “are you”]
Function Parameters:
“python is great .”
“ “
Return value:
[“python”, “is”, “great”, “.”]
Function Parameters:
“to be or not to be”
“be“
Return value:
[“to “, “ or not to “]
```

###### Part VII : Deep Copy
Define a function named deepCopy that takes a list as parameter and returns a copy of that list. The list may contain other lists and those lists may contain other lists and so on. You are not allowed to use slicing and other functions and methods of python.

## Bonus part

### 20 - Work With strings I
1. Write a python program that takes a string as input and prints its characters in separate lines.
2. Define a function that takes two string as parameters and compare them. It should return -1 if str1 < str2, 0 if str1 == str2 and 1 if str1 > str2. `Note: You cannot use python compare operators. (<, >, ==)``
3. Define a function for testing your q2 function. It takes two strings as parameters and compare them using python compare operators (<, >, ==). Then compares the result with the result of your compare function. It returns True if your function is working and False otherwise.
4. Define a function that takes a string and a character as parameters and finds the char in the string and returns its index. It returns -1 if the char was not found.
5. Define a function that takes two strings as input and checks weather the second string’s characters are in the first string with the same order.
`Example: “abcdefg”, “bdf” -> true`
6. Define a function that takes a string and a character and returns a string between two of that char.
`Example: “salam”, “a” -> “l” “string”, “r” -> “ing” “hello”, “b” -> “”`
7. Define a function that takes a string as parameter and reverses that.
### 21 - Work With strings II
1. Define a function that takes a string as parameters and converts its uppercase characters to lowercase and visa-versa.
`Example: “hEllO” -> “HeLLo”``
2. A. Define a function that takes a string as parameters and adds the digits of that a string to a list and returns that list.
`Example: “a1bc2d34f” -> [‘1’, ‘2’, ‘3’, ‘4’]``
  1. Define a function that takes a list of character digits and converts that list to a list of integer digits.
`Example: [‘1’, ‘2’, ‘3’, ‘4’] -> [1, 2, 3, 4]``
  2. Use functions of A and B and define a function that takes a string and converts it to integer. (Google “atoi” if you are interested to learn more)
`Example: “256hello1” -> 2561`
3. A. Define a function that takes a list as parameter and gets input from user until the user enters 0 and adds the inputs to that list. (Note that the function doesn’t return anything and the passed list may not be empty.)
  1. Define a function that gets input from user until the user enters 0 and adds the inputs to a list and returns that list.
4. Define a function that takes some students’ name and grade and adds them to a 2D list and returns name of the student with maximum grade.
5. Define a function that takes a list of characters and converts it to a string.

### 22 - Work With Lists
1. Define a recursive function that takes a positive integer as parameter and returns the factorial of that number.
2. Define a recursive function that takes a string as parameter and reverses that string and returns it.
3. Define a recursive function that takes x and n as parameters and returns True if x is a power of n and returns False otherwise.
4. Define a recursive function that takes an integer as parameter and return the number of its digits.
5. Define a recursive function that takes a list of integers as parameter and return the maximum integer in that list.
6. Define a recursive function that takes a list and an integer as parameters and returns True if the integer is in that list and returns False otherwise. Note that the list may contain another list and the function should also search inner lists.
`Example: [[1, 2, 3], [1], 2, [1, 2, [2016, 3]]], 2016 -> True`
***Hint: Use type function.****
7. In this problem, you will be working on a famous mathematical puzzle called The Tower of Hanoi. There are three pegs, and on the first peg is a stack of discs of different sizes, arranged in order of descending size. The object of the game is to move all of the discs
to another peg. However, only one disc can be moved at a time, and ***a disc cannot be placed on top of a smaller disc.***

### 23 - Work With Files
Write a Python module and Implement these functionalities.
  - createFile
  - appendToFile
  - readFromFile
  - deleteFromFile

### 24 - Work With Everything
Write a python program that takes a number and shows a menu of operations on that number. It takes the number of operation and shows the result and continues taking
number of operation until user choose exit.
###### List of operations:
1. Multiple of factors: Calculates multiple of the number’s prime factors.
Ex: 12 = 22 * 3 → 2 * 3 = 6
2. Greatest prime divisor: Finds the greatest prime divisor.
Ex: 12 = 22 * 3 → 3
3. Calculates poly: Gets n and n+1 multipliers and calculates the n-degree poly made
by the multipliers for the number.
Ex: 3 1 2 1 4 → f(x) = x3 + 2x2 + x + 4 → f (12) = 2032
4. Calculate a.n: Gets n and theta (an angle) and calculates the number and n’s inner
product (a.n = a * n * cos(theta)).
Ex: 4 60 → 12 * 4 * cos (60) = 24
5. Change base: Gets n and change the number’s base from 10 to n.
Ex: 2 → (12)10 = (1100)2
6. Change number: changes the number.
7. Exit


As you can see there are 2 python files in this zip.
The first file _"List of operations\_2"_ contains array and built -in functions usage.
The second python file _"List of operations\_1"_ is the same file with the same result but **WITHOUT USING BUILT-IN
FUNCTIONS AND ARRAY.**
