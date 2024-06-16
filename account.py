""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    def __init__(self, name, ID, balance):
        self.set_account_name(name)
        self.set_account_ID(ID)
        self.set_account_balance(balance)

    def get_account_name(self):
        return self.name

    def set_account_name(self, name):
        if isinstance(self, Account):
            self.name = name
        else:
            raise TypeError('account must be an Account object')

    def get_account_ID(self):
        return self.ID

    def set_account_ID(self, ID):
        if isinstance(self, Account):
            if isinstance(ID, (int, float)):
                self.ID = ID
            else:
                raise TypeError('ID must be a number')
        else:
            raise TypeError('account must be an Account object')
    
    def get_account_balance(self):
        return "Balance: ${:.2f}".format(self.balance) 
    
    def set_account_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.balance = balance
        else:
            raise ValueError("Balance must be a non-negative number")
        
if __name__ == '__main__':
    try:
        account1 = Account('John', 123456789, 1000.00)
        print("success", account1.get_account_name(account1), account1.get_account_ID(account1), account1.get_account_balance(account1))
    except TypeError as e:
        print("error", e)


