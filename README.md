# Cashflow Manager

**Making a Cashflow Manager using Python**

A simple app that assists you in storing and managing your cash flow activities.

## Features

- **Record Transactions**: Easily add debit and credit transactions.
- **View Transaction History**: Display a list of all recorded transactions.
- **Check Total Balance**: See the current total balance of your transactions.

## Package Used

- **datetime**: To generate and handle date and time.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/christoaaron/cashflow-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cashflow-manager
   ```
3. Install the required packages:
   ```bash
   pip install datetime
   ```

## Usage

1. Run the script:
   ```bash
   python cashflow_manager.py
   ```
2. Follow the on-screen instructions to add transactions, view the transaction history, or check the total balance.

## Code Overview

### `add_transaction()`

Handles adding a new transaction (either debit or credit), updates the total balance, and records the transaction details with a timestamp.

### `show_transactions()`

Displays a list of all recorded transactions with their type, amount, and timestamp.

### `show_total_transactions()`

Shows the current total balance of all transactions.

### `main()`

Provides a menu for interacting with the app, allowing users to add transactions, view transaction history, check total balance, or exit the app.

## Example

```text
Cashflow Manager App
1. Add Transaction
2. Show Transactions
3. Show Total Transactions
4. Exit
Choose an option: 1
Enter transaction type (debit/credit): credit
Enter transaction amount: 1000
Transaction credit of 1000.0 added successfully.
```

```text
Cashflow Manager App
1. Add Transaction
2. Show Transactions
3. Show Total Transactions
4. Exit
Choose an option: 2
Transactions List:
Type: credit, Amount: 1000.0, Time: 2024-07-15 10:12:14.446366
```

```text
Cashflow Manager App
1. Add Transaction
2. Show Transactions
3. Show Total Transactions
4. Exit
Choose an option: 3
Total Transactions: 1000.0
```
