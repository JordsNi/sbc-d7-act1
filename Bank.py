from random import randint
all_user = {}
def account():
    for i in range(1):
            bal = int(input("\nCreate Account\nEnter your starting amount: "))
            user_id = str(randint(00000,99999)).zfill(5)
            all_user[user_id] = bal
            print(f"\nThis is your account:\nUser ID: {user_id}\nBalance: {bal}")

def balance():
    check = (input("\nPlease enter your user ID: "))
    if check in all_user:
            print("Your Balance is", all_user[check],"\n")
    else:
            print("User ID not in bank!")
        
def withdraw():
    check = (input("\nPlease enter your user ID: "))
    if check in all_user:
        amt = int(input("Amount to be withdrawn: "))
        total = all_user[check] - amt
        all_user.update({check:total})
        print(f"{amt} successfully withdrawn, Total balance: {total}")
    else:
         print("ID not in bank!")

def deposit():
    check = (input("\nPlease enter your user ID: "))
    if check in all_user:
        amt = int(input("Amount to be deposited: "))
        total = all_user[check] + amt
        all_user.update({check:total})
        print(f"{amt} successfully deposited, Total balance: {total}")
    else:
         print("ID not in bank!")

def delete():
    check = (input("\nPlease enter your user ID: "))
    if check in all_user:
        remove = all_user.pop(check)
        print("Successfully removed")
    else:
        print("ID not in bank!")

while True:
    print(all_user)
    bank = input("\nBanko\nCreate Account(A)\nCheck Balance(B)\nWithdraw(C)\nDeposit(D)\nDelete Account(E)\nChoose your next action: ").upper()
    if bank == "A":
        account()
    if bank == "B":
        balance()
    if bank == "C":
        withdraw()
    if bank == "D":
        deposit()
    if bank == "E":
        delete()
    else:
         ...