# Monthly Budget Planner
A simple desktop GUI application built in Python that helps users track their monthly income and expenses, calculate their remaining budget, and get feedback on their finances.

## Features
Input fields for:
* Monthly Income
* Housing
* Utilities
* Food
* Transportation
* Entertainment
* Other expenses
* Savings Goal
* Emergency Fund

**Calculate Budget Button**

Totals all expenses and shows your remaining balance

**Reset Button**

Clears all fields back to 0.0

 **Instant Popup Messages showing:**

* Total Expenses
* Remaining Balance
* If the user is over budget, on budget, and under budget


## Requirements

* Python 3
* `breezypythongui` module (This provides the `Easy Frame` GUI base class and field/button widgets used in this project)

## Setup/Installation

1. Make sure Python 3 is installed on your machine. Check with **python --version**

2. Install the `breezypythongui` package:
    **pip install breezypythongui**

3. Download or clone this project folder.

## Screenshots

### Main Interface
The main window where users enter their income and expenses.

![Main Interface](Screenshots\main-interface.png)

### Total Expenses Calculation

After clicking **"Calculate Budget"**, a pop up displays the total of all entered expenses.

![Total Expenses](Screenshots\total-expenses.png)

### Remaining Balance
A second popup shows the remaining balance after expenses are subtracted from income.

![Remaining Balance](Screenshots\remaining-balance.png)

### Budget Status Message
A final popup lets the user know whether they are over budget, on budget, or under budget.

![Under Budget](Screenshots\popup-message.png)

## Challenges
* My code wasn't properly indented which initially prevented it from executing.
    
* Accidentally capitalizing `self`
    
* Using two `if` statements instead of `elif`
    
* Finding the right background colors.