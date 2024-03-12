from db_connection import connect
from BankerSide import Bank
from CustomerSide import Customer

def main():
    # Connect to the MySQL database
    connection = connect()
    if not connection:
        print("Exiting...")
        return

    bank = Bank(connection)

    while True:
        print("\n===== Banking Application =====")
        print("1. Banker Operations")
        print("2. Customer Operations")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            banker_operations(bank)

        elif choice == '2':
            customer_operations(bank)

        elif choice == '3':
            print("Thank you for using the Banking Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when exiting
    connection.close()


def banker_operations(bank):
    print("\n===== Banker Operations =====")
    print("1. Create Account")
    print("2. Update Customer")
    print("3. View All Customers")  # Option to view all customers
    print("4. Delete All Customers")
    print("5. Back to Main Menu")

    banker_choice = input("Enter your choice: ")

    if banker_choice == '1':
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder's name: ")
        bank.create_account(account_number, account_holder)

    elif banker_choice == '2':
        account_number = input("Enter account number: ")
        new_account_holder = input("Enter new account holder's name: ")
        bank.update_customer(account_number, new_account_holder)

    elif banker_choice == '3':
        bank.view_all_customers()  # Call the view_all_customers method

    elif banker_choice == '4':
        bank.delete_all_customers()

    elif banker_choice == '5':
        return

    else:
        print("Invalid choice. Please try again.")
        banker_operations(bank)



def customer_operations(bank):
    account_number = input("Enter account number: ")
    customer = Customer(account_number, bank)

    print("\n===== Customer Operations =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Back to Main Menu")

    customer_choice = input("Enter your choice: ")

    if customer_choice == '1':
        amount = float(input("Enter amount to deposit: "))
        customer.deposit(amount)

    elif customer_choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        customer.withdraw(amount)

    elif customer_choice == '3':
        customer.check_balance()

    elif customer_choice == '4':
        return

    else:
        print("Invalid choice. Please try again.")
        customer_operations(bank)


if __name__ == "__main__":
    main()
