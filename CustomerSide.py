class Customer:
    def __init__(self, account_number, bank, connection):
        self.account_number = account_number
        self.bank = bank
        self.connection = connection

    def deposit(self, amount):
        account = self.bank.get_account(self.account_number)
        if account:
            account.deposit(amount)
            # Update account balance in database
            cursor = self.connection.cursor()
            query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
            cursor.execute(query, (account.balance, self.account_number))
            self.connection.commit()
            cursor.close()
            print("Deposit successful.")
        else:
            print("Account does not exist.")

    def withdraw(self, amount):
        account = self.bank.get_account(self.account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account does not exist.")

    def check_balance(self):
        account = self.bank.get_account(self.account_number)
        if account:
            account.check_balance()
        else:
            print("Account does not exist.")
