from threading import Lock

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.lock = Lock()

def deposit(user:Account, amount: float):
    with user.lock:
        user.balance += amount
        return True    
        
def withdraw(user:Account, amount: float):
    with user.lock: 
        if user.balance >= amount:
            user.balance -= amount 
            return True
        return False
    
def transfer(sender: Account, receiver: Account, amount: float):
    # acquire locks in consistent order to prevent deadlocks 
    first, second = (sender, receiver) if sender.owner > receiver.owner else (receiver, sender)

    with first.lock:
        with second.lock: 
            if sender.balance >= amount: 
                sender.balance -= amount
                receiver.balance += amount
                return True
            return False 

