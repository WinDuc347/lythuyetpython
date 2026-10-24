def xuat_hien(a,b):
  count=0
  for x in a:
    if b==x:
      count=count+1
  return count
xuat_hien("afbwaibfigeriafgbeig","af")# Python Thinking – Session 2 Summary

Session 2 has 13 exercises, all about **variables, operators and conditional statements (`if / elif / else`)**.

## 1. Variables and basic arithmetic
| Exercise | What it does |
|---|---|
| [Exercise 2.1](Session%202/Exercise%202.1.py) | Assigns `name = "Omar"` and `age = 17`, then prints them. The second line prints `age + 1`, which shows that an expression is evaluated inside `print`. |
| [Exercise 2.2](Session%202/Exercise%202.2.py) | Computes `2 * radius * pi`. The variable is called `area`, but this formula gives the **circumference**. The area would be `pi * radius ** 2`. |

## 2. Simple `if / else`
| Exercise | What it does |
|---|---|
| [Exercise 2.3](Session%202/Exercise%202.3.py) | Elevator: prints `"DING!"` on floor 55 and `"..."` on any other floor. |
| [Exercise 2.4](Session%202/Exercise%202.4.py) | If a name is shorter than 4 characters, it is doubled (`"Bob"` becomes `"BobBob"`). Uses `len()` and `+=` on strings. |
| [Exercise 2.5](Session%202/Exercise%202.5.py) | Checks for a negative radius before printing the result. |

## 3. Nested `if`
- [Exercise 2.6](Session%202/Exercise%202.6.py): two checks, one inside the other. First `pi` must be precise enough (≥ 3.14), then the radius must not be negative.

## 4. The `%` operator and boolean variables
- [Exercise 2.7.1](Session%202/Exercise%202.7.1.py): checks even/odd directly with `number % 2 == 0`.
- [Exercise 2.7.2](Session%202/Exercise%202.7.2.py): stores the result of the comparison in a boolean variable (`number_was_even`) and uses that in the `if`, which makes the code easier to read.

## 5. Fixing broken code: `elif`, `and`, separate `if`s
- [Exercise 2.8.1](Session%202/Exercise%202.8.1.py): sorts an age into minor, adult or error, using `and` and `elif`. With `age = 0` the program prints `"error - age < 0"`, so an age of 0 counts as an error even though the message says "< 0".
- [Exercise 2.8.2](Session%202/Exercise%202.8.2.py): the point of this one is to use **two separate `if`s** instead of `elif`. That way 6 prints both "even" and "divisible by 3".

## 6. `elif` chains and user input
- [Exercise 2.9](Session%202/Exercise%202.9.py): a more advanced elevator that reads the floor with `int(input())`:
  - below 0 or above the top floor: error
  - floor 0 or the top floor: `"DING!"`
  - a multiple of 10: prints the floor number
  - any other floor: `"..."`
  - Part 9.2 replaces the hardcoded 60 with a variable, `max_floor = 1000`, so the limit only has to be changed in one place.

## 7. Drawing block structures and predicting output
[Exercise 2.10](Session%202/Exercise%202.10.py) is a deeply nested `if` block. With `a=-4, b=7, c=6`, the program runs like this:

1. `a > 0` is false, so it takes the `else` branch and sets `a = 0`.
2. `c = 6 > 0`, so `d = "c is positive"`. Because `c < 10` it appends `" , but smaller than 10"`, then `" and even"`, then `" and divisible by 3"`.
3. `a == 0` is true, so `c = 100` and `a = -0 = 0`. Finally `b = 200`.

**Output:**
```
a: 0 b 200 c: 100 d: c is positive , but smaller than 10 and even and divisible by 3
```

If `a > 0`, `d` is never assigned, and the `print` line raises a `NameError`.

## In short
Session 2 covers variables, the operators `+ * % ==`, the logical operators `and/or`, `if / elif / else` (including nested `if`s), when to use `elif` versus separate `if`s, reading input with `input()` and `int()`, and predicting what a program will print by tracing it.
