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

## Web Requests, HTML Parsing, and Pagination
- **In my own words:** A scraper fetches a page, parses its HTML, and extracts related information from each matching container. It can follow the page's relative Next link until no next page is available.
- **Why it matters:** Parsing structured HTML and following pagination lets a program collect related information across multiple pages.
- **Time / space complexity (if applicable):** For p pages with q quote records per page, processing time is O(pq); storing only the current page uses O(q) space.
- **Source:** Quotes to Scrape practice project
- **Self-quiz result:** I fetched all 10 pages, extracted 100 quote-author pairs, checked HTTP responses, and stopped when the Next link was absent.

## Dynamic Arrays and List Complexity
- **In my own words:** Reading a list item by index is O(1). Searching takes O(n) in the worst case, and inserting at the beginning takes O(n) because later items shift. Appending is O(1) amortized.
- **Why it matters:** Operation costs help predict how a program will scale as its data grows.
- **Time / space complexity (if applicable):** Index access O(1), search O(n), front insertion O(n), and append O(1) amortized.
- **Source:** Phase 2 data structures and algorithms practice
- **Self-quiz result:** I identified why front insertion requires shifting, why append is usually constant time, and why doubling the list size roughly doubles search work.

## Linked Lists
- **In my own words:** Finding a node can take O(n) because nodes may need to be visited one at a time. Inserting at the head or after a node I already have takes O(1), while appending by traversing takes O(n) unless a tail reference is maintained. Removing a middle node means linking its previous node to its next node.
- **Why it matters:** Linked lists make some insertions and removals efficient when the needed node references are available, but finding a position still requires traversal.
- **Time / space complexity (if applicable):** Searching or indexing is O(n); insertion after a known node and removal with a known predecessor are O(1); append by traversal is O(n), or O(1) with a maintained tail reference.
- **Source:** Phase 2 data structures and algorithms practice
- **Self-quiz result:** I distinguished the O(n) cost of finding a node from O(1) pointer updates, implemented head insertion, identified `None` as the end-of-list marker, created and linked Node instances, traversed with a separate current-node reference so the head remains available, appended a node to empty and non-empty lists, implemented `contains` for found, missing, and empty-list cases, and implemented and tested `remove` for head, middle, and missing targets in empty and non-empty lists.

## Classes and Instances
- **In my own words:** A class defines the structure and behavior for objects. Each instance has its own attributes; `__init__` sets them when the instance is created.
- **Why it matters:** Classes let a data structure keep its state, such as a linked list's head, together with the operations that use it.
- **Time / space complexity (if applicable):** Not applicable.
- **Source:** Python linked-list practice
- **Self-quiz result:** I created a `LinkedList` instance whose `head` initializes to `None`, implemented `append` for empty and non-empty lists, and implemented `display` by traversing with a separate cursor.

## Stacks
- **In my own words:** A stack follows last in, first out (LIFO). The most recently pushed item is the next one popped.
- **Why it matters:** Stacks model workflows where the newest item must be handled first, such as undo history or function calls.
- **Time / space complexity (if applicable):** With a Python list used as the stack, pushing and popping at the end are O(1) amortized.
- **Source:** Python stack practice
- **Self-quiz result:** I pushed X, then Y, and verified that pop returns Y while X remains. I also handled pop on an empty stack by returning `None`.

## Queues
- **In my own words:** A queue follows first in, first out (FIFO). The first item added is the first item removed.
- **Why it matters:** Queues are useful when work should be handled in arrival order, such as a line of tasks waiting to be processed.
- **Time / space complexity (if applicable):** With a Python list, enqueue using `append()` is O(1) amortized. Dequeue using `pop(0)` is O(n) because the remaining items shift. An empty-queue check is O(1).
- **Source:** Python queue practice
- **Self-quiz result:** I implemented `enqueue` and `dequeue`, verified that A, B, and C leave the queue in that order, and handled dequeue on an empty queue by returning `None`.

## Hash Maps
- **In my own words:** A hash map stores key-value pairs. It hashes a key to choose a bucket; if multiple keys land in the same bucket, it checks the stored keys to find the right pair.
- **Why it matters:** Hash maps support key-based lookup and can track counts such as repeated colors or votes.
- **Time / space complexity (if applicable):** With a good key distribution, lookup and insertion are O(1) on average. With chaining, an operation can take O(n) in the worst case if many keys land in one bucket. This practice implementation uses a fixed number of buckets and does not resize.
- **Source:** Python hash map practice
- **Self-quiz result:** Implemented `put` and `get` with bucket lists, handled collisions and updates, returned `None` for a missing key, and used the map to count repeated colors. Needed hints while building the loop and frequency-counting logic; independent implementation has not yet been demonstrated.

## Binary Search Trees
- **In my own words:** Each node has up to two children. Smaller values go left and larger values go right. In-order traversal visits left, current, then right, producing ascending values.
- **Why it matters:** A binary search tree uses its ordering rule to guide insertion and search toward the part of the tree where a value belongs.
- **Time / space complexity (if applicable):** Insert and search take O(h), where h is the tree height: O(log n) when balanced and O(n) when skewed. In-order traversal takes O(n) time and O(h) call-stack space.
- **Source:** Python binary search tree practice
- **Self-quiz result:** With guided help, practiced insertion, `contains`, and in-order traversal; verified traversal of 8, 3, 10, and 6 returns 3, 6, 8, 10. Explained that smaller values appear in the left subtree. Independent implementation and transfer practice remain to be checked.
