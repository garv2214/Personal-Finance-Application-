import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data.json")

#function to load transaction data from JSON file
def load_data():
    if DATA_DIR.exists():
        return []
    with open(DATA_DIR, "r") as f:
        return json.load(f)
    

#function to save transaction data to JSON file
def save_data(transactions):
    with open(DATA_DIR, "w") as f:
        json.dump(transactions, f, indent=4)


#function to validate transaction data before saving it
def validate_transaction(transaction):
    required_fields = ["type", "date", "amount", "category"]
    for field in required_fields:
        if field not in transaction:
            raise ValueError(f"Missing required field: {field}")

    #testig the type field to be either income or expense
    if transaction["type"] not in ("income", "expense"):
        raise ValueError("Type must be 'income' or 'expense'")

    #testing the amount field to be a positive number
    if not isinstance(transaction["amount"], (int, float)):
        raise ValueError("Amount must be a number")

    if transaction["amount"] <= 0:
        raise ValueError("Amount must be positive")

    #testing the date field to be in YYYY-MM-DD format
    try:
        datetime.strptime(transaction["date"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

    return True


#function to add a new transaction 
def add_transaction(t_type, amount, category=None, date=None, note=""):
    
    transactions = load_data()

    #block to create a new transaction dictionary
    transaction = {
        "type": t_type,
        "amount": float(amount),
        "category": category if category else "Uncategorized",
        "date": date if date else datetime.today().strftime("%Y-%m-%d"),
        "note": note
    }

    #saving the transaction after validation
    validate_transaction(transaction)  # strict check
    transactions.append(transaction)
    save_data(transactions)
    print("Transaction added successfully.")
    return transaction
    

def get_all_transactions():
    
    transactions = load_data()

    # Run validation on each transaction to ensure integrity
    valid_transactions = []
    for t in transactions:
        try:
            validate_transaction(t)

            # Ensure amount is float (in case JSON stored it differently)
            t["amount"] = float(t["amount"])
            valid_transactions.append(t)
        except ValueError as e:
            print(f"Skipping invalid transaction: {e}")
    return valid_transactions

