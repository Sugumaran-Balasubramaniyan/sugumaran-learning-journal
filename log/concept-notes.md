# Concept Notes

Use this template for each concept. Do not copy the textbook — write it in your own words.

## Functions and Loops
- **In my own words:** A function is a reusable block of code. When I call a function, Python runs the code inside it. A loop repeats a block of code over and over so I do not have to duplicate the same instructions many times.
- **Why it matters:** Functions make code easier to read and reuse, while loops help process lists and repeated tasks efficiently.
- **Time / space complexity (if applicable):** For a simple loop over n items, the time complexity is O(n).
- **Source:** Python fundamentals practice / CS50-style learning
- **Self-quiz result:** I can explain the difference between a function definition, a function call, and a loop, and I understand that loops repeat work while functions package reusable logic.

## Conditionals and Boolean Logic
- **In my own words:** A conditional lets Python choose which block of code to run based on whether a comparison is true or false. `if` checks the first condition, `elif` checks another possibility, and `else` handles everything that remains.
- **Why it matters:** Conditionals let programs make decisions and respond differently to different inputs.
- **Time / space complexity (if applicable):** A fixed chain of conditional checks is O(1) time and O(1) space.
- **Source:** Python fundamentals practice / CS50-style learning
- **Self-quiz result:** I can use `if`, `elif`, and `else` to classify a number as positive, negative, or zero.

## Collections and Error Handling
- **In my own words:** Lists store ordered, changeable values; tuples store ordered values that should not change; sets store unique values; and dictionaries store key-value pairs. `try` and `except` handle expected errors such as invalid numeric input.
- **Why it matters:** Collections organize data, while error handling keeps programs usable when input is unexpected.
- **Time / space complexity (if applicable):** Accessing a list or tuple by index is O(1); looping through a collection is O(n).
- **Source:** Python fundamentals practice / CS50-style learning
- **Self-quiz result:** I can create, access, modify, and iterate through basic Python collections, and catch `ValueError` from invalid integer input.

## Input, Loops, and Small Programs
- **In my own words:** `input()` reads text, so numeric input must be converted with `int()` or `float()`. A `while` loop repeats until its condition becomes false, and `continue` skips the rest of the current iteration.
- **Why it matters:** These tools let a program interact with users and repeat work until a task is complete.
- **Time / space complexity (if applicable):** A guessing game with one guess per iteration uses O(g) time for g guesses and O(1) additional space.
- **Source:** Python fundamentals practice / CS50-style learning
- **Self-quiz result:** I built a number-guessing game that validates input, gives high/low hints, and stops when the correct number is guessed.

## Functions in a Small Program
- **In my own words:** Functions can give distinct jobs, such as adding or viewing tasks, a clear place in a program. I can pass the task list to a function so the functions work with the same data.
- **Why it matters:** Breaking a program into functions makes each action easier to understand, test, and update.
- **Time / space complexity (if applicable):** Depends on the work inside each function; iterating through n tasks is O(n) time.
- **Source:** To-do CLI practice
- **Self-quiz result:** I refactored the to-do menu actions into functions that receive the task list; I am practicing reusing one save function instead of repeating file-writing code.
