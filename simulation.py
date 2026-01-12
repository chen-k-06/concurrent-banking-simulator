import threading
from accounts import deposit, withdraw, transfer
from transactions import log_transaction

def perform_operations(account_dict: dict, operations: list):
    """Run a list of operations (deposit, withdraw, transfer)"""
    for operation in operations: 
        if operation["type"] == "deposit":
            result = deposit(account_dict[operation["user"]], operation["amount"])
            log_transaction(f"Deposit ${operation['amount']} to {operation['user']}", result)

        elif operation["type"] == "withdraw":
            result = withdraw(account_dict[operation["user"]], operation["amount"])
            log_transaction(f"Withdraw ${operation['amount']} from {operation['user']}", result)

        elif operation["type"] == "transfer":
            result = transfer(account_dict[operation["from"]], account_dict[operation["to"]], operation["amount"])
            log_transaction(f"Transfer ${operation['amount']} to {operation['to']} from {operation['from']}", result)

        else: 
            print("Invalid transaction type.")
            return

def run_concurrent_simulation(account_dict: dict, operations_lists: list):
    threads = []
    for ops in operations_lists:
        t = threading.Thread(target=perform_operations, args=(account_dict, ops))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
