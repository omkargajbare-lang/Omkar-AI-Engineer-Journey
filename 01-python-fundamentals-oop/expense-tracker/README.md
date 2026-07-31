Expense Tracker

A command-line expense management application built with Python as part of my AI Engineer learning journey.



Project Objective

The goal of this project was to practice how individual Python concepts work together in a real program.



The application allows users to:

\- Add expenses

\- View expenses

\- Calculate total spending

\- Calculate spending by category

\- Modify an expense

\- Delete an expense

\- Exit the application safely





Features



1\. Add Expense

Users can enter:

\- Expense date

\- Category

\- Amount

\- Description

Each expense receives a unique expense ID automatically.



2\. View All Expenses

Displays all expenses currently stored in the application.



3\. Calculate Total Expense

Calculates the total amount of all recorded expenses.



4\. Calculate Category Total

Users can enter a category and calculate the total spending for that category. Category matching is case-insensitive.



5\. Modify Expense

Users can provide an expense ID and update its amount.



6\. Delete Expense

Users can provide an expense ID to remove an expense.



7\. Exit

Allows the user to safely exit the application.





Input Validation



The application includes validation for user inputs.



Expense Date

The date must follow:

YYYY-MM-DD

Invalid dates are rejected using Python's datetime module.



Expense Category

The category cannot be empty.



Expense Amount

The amount must be a valid number, must be greater than zero, and cannot be negative.



Expense ID

The expense ID must be a valid integer.



Menu Choice

Invalid menu input is handled without crashing the program.



Exception Handling

The application uses try / except blocks to handle invalid user input.



Example:

try:

&#x20;   amount\_input = float(input("Enter expense amount: "))

except ValueError:

&#x20;   print("Invalid amount.")



This prevents the application from terminating when the user enters unexpected input.





Python Concepts Demonstrated

\- Variables and data types

\- Lists

\- Dictionaries

\- Loops

\- if / elif / else

\- Functions

\- Function parameters

\- Return values

\- String methods

\- Dictionary operations

\- List operations

\- try / except

\- ValueError

\- datetime

\- Input validation

\- Modular program design





Program Design



The application separates input validation, business logic, and menu interaction.



User

&#x20;|

&#x20;v

Main Menu

&#x20;|

&#x20;+-- Add Expense

&#x20;|     |

&#x20;|     +-- Validate Date

&#x20;|     +-- Validate Category

&#x20;|     +-- Validate Amount

&#x20;|     +-- Add Expense

&#x20;|

&#x20;+-- View Expenses

&#x20;|

&#x20;+-- Calculate Total

&#x20;|

&#x20;+-- Calculate Category Total

&#x20;|

&#x20;+-- Modify Expense

&#x20;|

&#x20;+-- Delete Expense



This separation keeps the program easier to read, maintain, and extend.





Project Structure



expense-tracker/

|

+-- expense\_tracker.py

+-- README.md





How to Run

If Python is installed locally, run:

python expense\_tracker.py



The application displays:

\------ Welcome to the Expense Tracker! ------

1\. Add Expense

2\. View All Expenses

3\. Calculate Total Expense

4\. Calculate Category Total

5\. Modify Expense

6\. Delete Expense

7\. Exit



Example Expense

An expense is stored as a dictionary:

{

&#x20;   "expense\_id": 1,

&#x20;   "date": "2026-07-31",

&#x20;   "category": "Food",

&#x20;   "amount": 250.00,

&#x20;   "description": "Lunch"

}

Multiple expenses are stored inside a list:

expense\_list = \[

&#x20;   {

&#x20;       "expense\_id": 1,

&#x20;       "date": "2026-07-31",

&#x20;       "category": "Food",

&#x20;       "amount": 250.00,

&#x20;       "description": "Lunch"

&#x20;   }

]





Key Learning Outcomes

Through this project, I learned how to move from individual Python exercises to building a complete application.



Functions

Functions allow individual responsibilities to be separated into reusable blocks.



Return Values

Functions return results to the calling code instead of directly controlling how those results are displayed.



Input Validation

Validation should happen before business logic receives the data.



Exception Handling

try / except prevents expected user-input errors from crashing the application.



Separation of Responsibilities

Keeping validation, business logic, and menu interaction separate makes the program cleaner and easier to maintain.



Possible Future Improvements

The current project intentionally uses an in-memory list for learning purposes.



Possible future improvements include:

\- Persist expenses to a JSON file

\- Add expense search

\- Add monthly expense summaries

\- Add spending reports

\- Add CSV export

\- Add automated tests

\- Introduce a database

\- Convert the application into an OOP-based version



These improvements can be explored in later stages of the learning journey.





Learning Journey



Roadmap: Omkar's AI Engineer Journey

Module: 01 — Python Fundamentals \& OOP

Project: Expense Tracker

Status: Completed



Author

Omkar

This project is part of my structured journey toward becoming an AI Engineer, progressing from Python fundamentals through Machine Learning, NLP, AI, and Generative AI.



