class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")


class Bank:
    def __init__(self, connection):
        self.connection = connection
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, account_holder)
            self.accounts[account_number] = new_account
            print("Account created successfully.")
            # Add account to database
            cursor = self.connection.cursor()
            query = "INSERT INTO accounts (account_number, account_holder, balance) VALUES (%s, %s, %s)"
            cursor.execute(query, (account_number, account_holder, new_account.balance))
            self.connection.commit()
            cursor.close()
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def update_customer(self, account_number, new_account_holder):
        account = self.get_account(account_number)
        if account:
            account.account_holder = new_account_holder
            print("Customer information updated successfully.")
            # Update account holder in database
            cursor = self.connection.cursor()
            query = "UPDATE accounts SET account_holder = %s WHERE account_number = %s"
            cursor.execute(query, (new_account_holder, account_number))
            self.connection.commit()
            cursor.close()
        else:
            print("Account does not exist.")

    def view_all_customers(self):
        self.accounts = {self.account_number}
        print("List of Customers:")
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Account Holder: {account.account_holder}, Balance: {account.balance}")
            cursor = self.connection.cursor()
            query = "SELECT * FROM accounts"
            cursor.execute(query)
            self.connection.commit()
            cursor.close()   
            

    def delete_all_customers(self):
        self.accounts = {}
        print("All customers deleted successfully.")
        # Delete all accounts from database
        cursor = self.connection.cursor()
        query = "DELETE FROM accounts"
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
