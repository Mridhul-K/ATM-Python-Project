import random
import sys
dic = {}

def forget(j):
    
    print("Here is your question for resetting the password: ", dic[j][2])
    ans = input("your anwser:")
    
    if ans == dic[j][3]:
        h = input("create new password:")
        dic[j][1] = h
        return "changed"
    
    else:
        print("invalid")
        return "not changed"

def register():
    
    print("Welcome to the bank")
    a = input("You wanna 'login'/'register':").strip().lower()
    
    if a == "register":
        j = input("Enter your name:")
        rn=random.randint(100,999)
        un=j+str(rn)
        while True:
            
            if un in dic.keys():
                rn=random.randint(100,999)
                un=j+str(rn)
                continue
            
            else:
                print("Your username is:",un)
                break
                
        b= input("Enter your password:")
        d = input("For future purpose if you forget your password, write a security question that only you know the answer:")
        e = input("Answer of the question:")
        c=0
        dic[un] = [j,b,d,e,c]
        print("Your registration is complete.")
        return un
    
    elif a == "login":
        while True:
            j = input("Enter your username: ")
        
            if j not in dic.keys():
                a=input("user doesnt exit,if you wish to try again type 'log' or if you wish to register type 're' ").strip().lower()
                if a == 're':
                    return'redo'
                elif a=='log':
                    continue
                else:
                    print("Invalid input, defaulting to login")
            else:
                break

        while True:
            b = input("Enter your password/forgot password:")
            if b == dic[j][1]:
                print("Successfully logged in")
                print("Welcome",dic[j][0] )
                return un
        
            elif b == "forgot password":
                while True:
                    x=forget(j)
                    if x == "changed":
                        print("Password has been changed")
                        return"success"
        
            else:
                print("Invalid password,login again")
    else:
        print("Invalid input, Try again")
        return"redo"
                
def deposit(user):
    try:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount > 0:
            dic[user][-1] += amount
            print(f"Deposit successful! New balance: ₹{dic[user][-1]}")
            return"success"
        else:
            print("Deposit amount must be greater than 0.")
            return"redo"
    except ValueError:
        print(" Invalid input. Enter a numeric value.")
        return"redo"


def withdraw(user):
    try:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return"redo"
        elif amount > dic[user][-1]:
            print("Insufficient balance.")
            return"redo"
        else:
            dic[user][-1] -= amount
            print(f"Withdrawal successful! Remaining balance: ₹{dic[user][-1]}")
            return"success"
    except ValueError:
        print("Invalid input. Enter a numeric value.")
        return"redo"


def check_balance(user):
    print(f"Your current balance is: ₹{dic[user][-1]}")

def delete_account(user):
    print("Are you sure you want to delete your account?")
    confirm = input("Deleting your account is permanent. Are you sure? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        password = input("Please enter your password to confirm: ").strip()
        if password == dic[user][1]:
            del dic[user]
            print(f"Your account, {user}, has been permanently deleted.")
            print("Thanks for being with us. Take care!")
            return"success"
        else:
            print("Passwords don't match. Account not deleted.")
            return"redo"
    else:
        print("Account deletion cancelled.")
        return False

while True:
    while True:
        lg=register()
        if lg=="redo"  :
            continue
        else:
            break
    h=["1 - Deposit","2 - Withdraw","3 - Check Balance","4 - Delete Account","5 - Sign Out"]
    for i in h:
        print(i)
    while True:
        print("6 - Help")
        try:
            ac=int(input("Enter action number:"))
            if ac == 1:
                deposit(lg)
            elif ac == 2:
                withdraw(lg)
            elif ac == 3:
                check_balance(lg)
            elif ac == 4:
                delete_account(lg)
                break
            elif ac == 5:
                break
            elif ac == 6:
                for i in h:
                    print(i)
            else:
                print("Invalid Action Number, Try again")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    while True:
        nac=input("Type 'Exit' to end program or Type 'Re' to re-login:").strip().lower()
        if nac == 'exit' or nac == 're':
            break
        else:
            print("Invalid input try again")
    if nac=='exit':
        break

