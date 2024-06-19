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
        return self.__name

    def set_account_name(self, name):
            if isinstance(name, str):
                self.__name = name
            else:
                raise TypeError('Name must be a string')

    def get_account_ID(self):
        return self.__ID

    def set_account_ID(self, ID):
            if isinstance(ID, (int, float)):
                self.__ID = ID
            else:
                raise TypeError('ID must be a number')
    
    def get_account_balance(self):
        return "Balance: ${:.2f}".format(self.__balance) 
    
    def set_account_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Balance must be a non-negative number")
        
if __name__ == '__main__':
    try:
        account1 = Account('John', 123456789, 1000.00)
        print("success", account1.get_account_name(), account1.get_account_ID(), account1.get_account_balance())
    except TypeError as e:
        print("error", e)


