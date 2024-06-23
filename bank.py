""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            raise TypeError("Account must be an instance of the Account class")
        
    def remove_account(self, account): 
        if isinstance(account, Account):
            self.accounts.remove(account)
        else:
            raise TypeError("Account must be an instance of the Account class")
        
    def update_account(self, account):
        if isinstance(account, Account):
            for i in range(len(self.accounts)):
                if self.accounts[i].get_account_ID() == account.get_account_ID():
                    self.accounts[i] = account
                    break
                if i == len(self.accounts) - 1:
                    raise ValueError("Account not found")
        else:
            raise TypeError("Account must be an instance of the Account class")

    def display_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts to display")
        else:
            print("Accounts:")