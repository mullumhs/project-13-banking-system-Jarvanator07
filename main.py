""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
from bank import Bank

def main():
    accounts = []
    bank = Bank()
    
    while True:
        print("1. Add account")
        print("2. Remove account")
        print("3. Update account")
        print("4. Display accounts")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            account_number = int(input("Enter account number: "))
            name = input("Enter name: ")
            balance = float(input("Enter balance: "))
            account = Account(account_number, name, balance)
            bank.add_account(account)
            
        elif choice == 2:
            account_number = int(input("Enter account number to remove: "))
            bank.remove_account(account_number)
                
        elif choice == 3:
            account_number = int(input("Enter account number to update: "))
            name = input("Enter new name: ")
            balance = float(input("Enter new balance: "))
            bank.update_account(account_number, name, balance)
                
        elif choice == 4:
            bank.display_accounts()
                
        elif choice == 5:
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
