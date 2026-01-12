from threading import Lock

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount: float):
        with self.lock:
            self.balance += amount
            return True    
        
    def withdraw(self, amount: float):
        with self.lock: 
            if self.balance >= amount:
                self.balance -= amount 
                return True
            return False