# Money App

## Components
The components are the steps of the money pipeline. These operations on these steps are the core logic of the system and should not be modified without a system design review.

### Income
Income refers to any source of money coming to us. The most obvious instance of income is our salaries.

### Bills
Bills are the payments performed in cycles. These include mortgage, utility bills and similar.

### Expenses
Expenses are any ad-hoc payments for goods or services. These include food, cleaning and shopping.

### Savings
This is the share of money left after using our income to pay for bills and expenses that is saved.

### Investments
This is the share of money left after savings that is put back in the market to generate a return.

## Input Data
- Savings accumulated
- Income from salaries or investments
- Interest generated from savings
- Bills for the past month
- Expenses for the past month
- Investments in the past month
- Personal spending from each of us

## Parameters
Parameters are the parts of the system we can modify to make it work for our financial situation and expectations. These include:
- Saving pots and shares for each of them
- How bills and expenses are split between us
- The savings accounts we use and what pots go each one holds