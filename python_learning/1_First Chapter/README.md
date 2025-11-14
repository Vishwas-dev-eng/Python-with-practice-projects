# 🧩 First Chapter – Python Basics (If-Else and Fun with PyJokes)

Welcome to **Chapter 1 of Python Learning Notes** 🎉  
In this chapter, we’ll start our Python journey with the **basics of syntax, printing messages, and simple conditional logic** — all while having some fun with jokes 😄

---

## 🧠 What You’ll Learn Here
- How to **write your first Python program**
- The use of the **`print()`** function
- Basics of **`if` and `else`** conditions
- Installing and using a **Python library (`pyjokes`)**
- Running your first “fun” program 😄

---

## 💻 Example Program: "Python Joke Teller"

Here’s a fun and simple program to copy and run:

```python
# fun_jokes.py
# A simple program to print a random programming joke 😆

import pyjokes

print("Welcome to the Python Joke Teller 🤖")
print("-----------------------------------")

# Get a random joke
joke = pyjokes.get_joke()

# Display it
print("Here's a Python joke for you:")
print(joke)

# Small bonus: check your reaction
mood = input("\nDid you laugh? (yes/no): ")

if mood.lower() == "yes":
    print("😂 Glad you liked it!")
else:
    print("😅 I'll try to be funnier next time!")
