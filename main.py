import datetime

# Stores the transactions
transactions = []
# Stores the total amount of transactions
total_amount = 0

# Add Transaction
def add_transaction():
    global total_amount
    transaction_type = input('Enter transaction type (debit/credit): ').strip().lower()
    amount = float(input('Enter transaction amount: '))
    transaction_time = datetime.datetime.now()

    if transaction_type == 'debit':
        amount = -amount  # Debit reduces the total amount

    if transaction_type == 'credit':
        amount = +amount  # Credit increases the total amount

    transaction = {
        'transaction_type': transaction_type,
        'amount': amount,
        'transaction_time': transaction_time
    }
    transactions.append(transaction)
    total_amount += amount

    print(f"Transaction {transaction_type} of {amount} added successfully.")

# Show Transactions List
def show_transactions():
    print("Transactions List:")
    for transaction in transactions:
        print(f"Type: {transaction['transaction_type']}, Amount: {transaction['amount']}, Time: {transaction['transaction_time']}")

# Show Total Transactions
def show_total_transactions():
    print(f"Total Transactions: {total_amount}")

# Menu
def main():
    while True:
        print("\nCashflow Manager App")
        print("1. Add Transaction")
        print("2. Show Transactions")
        print("3. Show Total Transactions")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_transactions()
        elif choice == '3':
            show_total_transactions()
        elif choice == '4':
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
