from datetime import datetime
from threading import Lock

transactions = []  # global transaction log
log_lock = Lock()

def log_transaction(operation: str, success: bool):
    with log_lock:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILED"
        transactions.append(f"{timestamp}: {operation}: {status}")

def validate_accounts(accounts: dict):
    """Check no negative balances and print final state"""
    total = 0
    for account in accounts.values(): 
        if account.balance < 0: 
            print("Account %s has negative balance.", account.owner)
            return 
        total += account.balance
    print("All accounts valid. Total system balance: %d\n", total)
    return