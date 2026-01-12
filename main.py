# from accounts import deposit, withdraw, transfer
from account import Account
from simulation import run_concurrent_simulation
from transactions import validate_accounts, transactions

accounts = {
    "Alice": Account("Alice", 1000),
    "Bob": Account("Bob", 500),
    "Charlie": Account("Charlie", 2000)}

