import time
import datetime

# Create a data structure to store user information in a dictionary.
users = {
    "Ahmet": {"password": 1234, "balance": 123, "withdrawals": [], "deposits": [], "transfers": []},
    "Zeynep": {"password": 4321, "balance": 123, "withdrawals": [], "deposits": [], "transfers": []}
}

current_user = None  # Stores the currently logged-in user.
registration_counter = 0  # Keeps track of the number of user registrations.

# Function to register a new user.
def register():
    global current_user, registration_counter

    if registration_counter >= 1:
        print("Sorry, you've reached the registration limit.\nPlease try again later.")
        return

    username = input("Please enter the username you want to register: ")

    if username in users:
        print("This username is already in use.")
        register()
    else:
        password = int(input("Please enter a password: "))

        # Create a new user and initialize their account with a balance of 0.
        users[username] = {"password": password, "balance": 0, "deposits": [], "withdrawals": [], "transfers": []}
        print("You have successfully registered. Please log in again.")
        registration_counter += 1

# Function to handle user login.
def login():
    global current_user
    x = datetime.datetime.now()
    print(x.strftime("""###########################################################
############   Welcome to Our Bank (v.0.1)  ############
############            ISTANBUL               ############                \n############       %x %X           ############
###########################################################"""))

    while True:
        menu = input("Please select the operation you want to perform:\n1. Log In\n2. Register\n3. Log Out")
        if menu == "2":
            register()
        elif menu == "3":
            print("Have a nice day...")
            x = datetime.datetime.now()
            print(x.strftime(" ----------------------- \n /     ISTANBUL    \ \n| %x %X |\n \                 / \n ----------------------- "))
            exit()
        elif menu == "1":
            username = input("Please enter your username: ")

            if username in users:
                password = int(input("Please enter the password: "))

                if users[username]["password"] == password:
                    print("You have successfully logged in.")
                    current_user = username
                    time.sleep(1)
                    main_menu()
                    break
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Username is incorrect. Please try again.")
        else:
            print("You made an invalid selection. Please try again.")

# Function to handle money transfer between users.
def money_transfer():
    global current_user
    x = datetime.datetime.now()
    recipient = input("Please enter the username of the recipient for money transfer: ")

    if recipient in users:
        amount = int(input("Please enter the amount you want to send: "))

        if users[current_user]["balance"] >= amount:
            users[current_user]["balance"] -= amount
            sender_info = "{} On this date, {} TL was sent from your account to the user named {}.".format(
                str(x), amount, recipient)
            users[current_user]["transfers"].append(sender_info)

            recipient_info = "{} On this date, {} TL was received from the user named {}.".format(
                str(x), amount, current_user)
            users[recipient]["transfers"].append(recipient_info)

            print(f"You have sent {amount} TL to {recipient}.")
            print(f"Your New Balance: {users[current_user]['balance']} TL")
        else:
            print("Insufficient balance. Money transfer cannot be completed.")
    else:
        print("Recipient username is incorrect.")

# Function to display the main menu for logged-in users.
def main_menu():
    x = datetime.datetime.now()
    while True:
        operations = input("""\nWelcome to Our Bank (v.1.2) Main Menu
Please select the operation you want to perform:
1. Withdraw Money
2. Deposit Money
3. Money Transfer
4. My Account Information
5. Log Out\n""")

        if operations == "1":
            amount = int(input("Please enter the amount you want to withdraw: "))

            if users[current_user]["balance"] >= amount:
                users[current_user]["balance"] -= amount
                withdrawal_info = "{} On this date, {} TL was withdrawn from your account.".format(
                    str(x), amount)
                users[current_user]["withdrawals"].append(withdrawal_info)

                print("The transaction was successful!")
                print(f"Withdrawn Amount: {amount} \n Your Current Balance: {users[current_user]['balance']} TL")
                print("Redirecting to the Main Menu. Please wait...")
                continue
            elif users[current_user]["balance"] <= amount:
                print("You do not have enough balance to withdraw.")
                print("Redirecting to the Main Menu. Please wait...")
                continue
            elif amount <= 0:
                print("You entered an invalid amount.")
                continue

        elif operations == "2":
            amount = int(input("Please enter the amount you want to deposit: "))
            users[current_user]['balance'] += amount
            deposit_info = "{} On this date, {} TL was deposited into your account.".format(str(x), amount)
            users[current_user]["deposits"].append(deposit_info)

            print(f"{amount} TL has been deposited into your account.")
            print(f"Your Current Balance: {users[current_user]['balance']} TL")
            print("Redirecting to the Main Menu. Please wait...")
            continue
        elif operations == "3":
            money_transfer()
        elif operations == "4":
            x = datetime.datetime.now()
            print(x.strftime("—— Our Bank ——\n%x %X\n——————————————————\nCurrent Balance: {} TL\n".format(
                users[current_user]["balance"])))

            print(f"Username: {current_user}")
            print(f"Password: {users[current_user]['password']} \n")

            print("Deposit Transactions:")
            for deposit_info in users[current_user]["deposits"]:
                print(deposit_info, "\n")

            print("Withdrawal Transactions:")
            for withdrawal_info in users[current_user]["withdrawals"]:
                print(withdrawal_info, "\n")

            print("Money Transfer Transactions:")
            for transfer_info in users[current_user]["transfers"]:
                print(transfer_info)

        elif operations == "5":
            print("Logging out from the account.")
            login()  # Redirects the user back to the login screen.

# Initiates the login process.
login()
