import random
import csv
import datetime


def create_new_account():
    # Date for Account Creation
    date = datetime.datetime.now()
    ac_date = date.strftime("%d-%m-%Y %I:%M %p")

    # Assigning a random AC number to the user
    ac_no = random.randint(10000, 99999)
    name = input("Enter Your Full Name: ").title()
    email = input("Enter Your E-Mail ID: ").lower()
    balance = 0
    bal_after_creation = "Account Created"

    # Assigning INFO to the CSV File
    with open("accounts.csv", "a", newline="") as f:
        accounts = csv.writer(f)
        accounts.writerow([name, ac_no, email, ac_date, balance])
    print(f"Name: {name}")
    print(f"E-Mail ID: ", email)
    print(f"AC No.: {ac_no}")
    print(f"Please Note Down the AC Number for further transactions. Your AC no. is {ac_no}".upper())

    # Creating new Document to store transaction details
    with open("transactions.csv", "a", newline="") as f:
        transactions = csv.writer(f)
        transactions.writerow([ac_no, balance,bal_after_creation, ac_date])


def search_ac_no():
    print("Enter Your Email ID to get your AC Number.".upper())
    email = input("Enter E-Mail Address: ").lower()
    found = False
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        for i in reader:
            if i[2] == email:
                found = True
                print("Name: ", i[0])
                print("AC Number: ", i[1])
                print("Date of Creation :", i[3])
    if not found:
        print("Invalid Email or Email Doesn't exist.")


def deposit():
    ac = input("Enter AC Number: ")
    updated_details = []
    mode = "Credit"
    found = False
    date = datetime.datetime.now()
    transac_date = date.strftime("%d-%m-%Y %I:%M %p")
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == ac:
                found = True
                amount = int(input("Enter Amount: "))
                row[4] = amount + int(row[4])
            updated_details.append(row)

    if not found:
        print("AC Number Not Found")
    else:
        with open("accounts.csv", "w+", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(updated_details)

    with open("transactions.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ac, amount, mode, transac_date])
    print(f"You Deposited Rs. {amount} Successfully")


def view_transactions():
    ac = input("Enter AC Number: ")
    count = 0
    with open("transactions.csv", "r") as f:
        reader = csv.reader(f)
        for account in reader:
            if ac == account[0]:
                count +=1
                print(f"{count}. Amount: {account[1]} | Mode: {account[2]} | Date: {account[3]}")


def withdraw():
    ac = input("Enter AC Number: ")
    updated_details = []
    mode = "Debit"
    found = False
    date = datetime.datetime.now()
    transac_date = date.strftime("%d-%m-%Y %I:%M %p")
    with open("accounts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if ac == row[1]:
                print(f"Balance: {row[4]}")
                print()
                found = True
                amount =input("Enter Amount to Withdraw: ")
                if int(amount) > int(row[4]):
                    print()
                    print("Insufficient Balance".upper())
                else:
                    row[4] = int(row[4]) - int(amount)
            updated_details.append(row)

    if not found:
        print()
        print("Enter Valid AC Number")
    else:
        with open("accounts.csv", 'w+', newline="" ) as f:
            writer = csv.writer(f)
            writer.writerows(updated_details)

    with open("transactions.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ac,amount, mode, transac_date])
    print(f"You Withdrew Rs. {amount} Successfully")

def view_balance():
    ac = input("Enter AC number: ")
    with open("accounts.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == ac:
                print(f"Balance: {row[4]}")

while True:
    print('''*************
Welcome to Bank of Daroga
*************
[1] Create new Bank Account
[2] Search Account Number
[3] Withdraw
[4] Deposit
[5] View Balance
[6] View Previous Transactions
*************
[7] Exit
*************''')
    ch = input("Enter Choice: ")
    if ch == "1":
        create_new_account()
        break

    elif ch == "2":
        search_ac_no()
        print('''*******
[1] Main Menu
[2] Quit
*******''')
        ch1 = input("Enter Option: ")
        if ch1 == "1":
            continue
        else:
            break

    elif ch == "3":
        withdraw()
        break

    elif ch == "4":
        deposit()
        break

    elif ch == "5":
        view_balance()
        print('''*******
[1] Main Menu
[2] Quit
*******''')
        ch1 = input("Enter Option: ")
        if ch1 == "1":
            continue
        else:
            break

    elif ch == "6":
        view_transactions()

        print('''*******
[1] Main Menu
[2] Quit
*******''')
        ch1 = input("Enter Option: ")
        if ch1 == "1":
            continue
        else:
            break

    elif ch == "6":
        break
