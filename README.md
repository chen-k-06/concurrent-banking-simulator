# Concurrent Banking Simulator

A Python simulation of a multi-user banking system that supports **concurrent deposits, withdrawals, and transfers** with thread-safe operations and invariant validation.

## Features

- Thread-safe `Account` class with **locks** to prevent race conditions.
- Functions for `deposit`, `withdraw`, and `transfer` operations.
- Deadlock prevention during concurrent transfers via consistent lock ordering.
- Global **transaction log** with timestamps for auditing.
- Post-simulation validation of account balances and total system funds.

## Example 
```python
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
```
### Output

All accounts valid. Total system balance: 3575.

Transaction Log:
2026-01-12 07:53:50: Deposit $100 to Alice: SUCCESS
2026-01-12 07:53:50: Transfer $50 to Bob from Alice: SUCCESS
2026-01-12 07:53:50: Withdraw $25 from Bob: SUCCESS
2026-01-12 07:53:50: Transfer $200 to Alice from Charlie: SUCCESS

