# Python Banking program
# 1. Show Balance
# 2. Deposit
# 3. Withdraw

def show_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("That not a valid amount. Please enter a positive number.")
        return 0 # return something to stop the function
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount
balance = 0
is_running = True

while is_running:
    print("Welcome to banking program!")
    print("1. show balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you! Have a nice day!👋")


# use Enclose scope 

def show_balance(balance):
    print("************************************")
    print(f"Your current balance is ${balance:.2f}")
    print("************************************")

def deposit():
    print("************************************")
    amount = float(input("Enter the amount to deposit: "))
    print("************************************")

    if amount < 0:
        print("************************************")
        print("That not a valid amount. Please enter a positive number.")
        print("************************************")
        return 0 # return something to stop the function
    else:
        return amount

def withdraw(balance):
    print("************************************")
    amount = float(input("Enter amount to withdraw: "))
    print("************************************")

    if amount > balance:
        print("************************************")
        print("Insufficient funds.")
        print("************************************")
        return 0
    elif amount < 0:
        print("************************************")
        print("Amount must be greater than zero.")
        print("************************************")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
       print("************************************")
       print("*    Welcome to banking program!*   ")
       print("************************************")
       print("1. show balance")
       print("2. deposit")
       print("3. withdraw")
       print("4. exit")
       print("************************************")

       choice = input("Enter your choice (1-4): ")

       if choice == "1":
           show_balance(balance)
       elif choice == "2":
           balance += deposit()
       elif choice == "3":
           balance -= withdraw(balance)
       elif choice == "4":
           is_running = False
       else:
           print("************************************")
           print("Invalid choice. Please try again.")
           print("************************************")
    print("************************************")
    print("Thank you! Have a nice day!👋")
    print("************************************")

if __name__ == "__main__":
    main()

