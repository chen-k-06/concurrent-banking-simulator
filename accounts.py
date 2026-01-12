from account import Account

def transfer(sender: Account, receiver: Account, amount: float):
    # acquire locks in consistent order to prevent deadlocks 
    first, second = (sender, receiver) if sender.owner > receiver.owner else (receiver, sender)

    with first.lock:
        with second.lock: 
            if sender.amount >= amount: 
                sender.amount -= amount
                receiver.amount += amount
                return True
            return False 

