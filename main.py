from accounts import Account
from simulation import run_concurrent_simulation
from transactions import validate_accounts, transactions

accounts = {
    "Alice": Account("Alice", 1000),
    "Bob": Account("Bob", 500),
    "Charlie": Account("Charlie", 2000),
}

# Each list is executed by one thread
ops1 = [
    {"type": "deposit", "user": "Alice", "amount": 100},
    {"type": "transfer", "from": "Alice", "to": "Bob", "amount": 50},
]

ops2 = [
    {"type": "withdraw", "user": "Bob", "amount": 25},
    {"type": "transfer", "from": "Charlie", "to": "Alice", "amount": 200},
]

run_concurrent_simulation(accounts, [ops1, ops2])
validate_accounts(accounts)
print("\nTransaction Log:")
for entry in transactions:
    print(entry)