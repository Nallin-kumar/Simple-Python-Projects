#banking Program

def show_balance(balance):
    print("************************")
    print(f"Your balance is ₹{balance:.2f}")
    print("************************")

def deposit():
    print("************************")
    amt=float(input("Enter the amount to be deposited "))
    print("************************")
    if amt<0:
        print("************************")
        print("That's not a valid amount")
        print("************************")
        return 0
    else:
        return amt

def withdraw(balance):
    print("************************")
    amt=float(input("Enter the amount to be withdrawn: "))
    print("************************")
    if amt>balance:
        print("************************")
        print("Insufficient Funds")
        print("************************")
        return 0
    elif amt<0:
        print("************************")
        print("Amount must be greater than 0 ")
        print("************************")
        return 0
    else:
        return amt  

def main():
    balance= 0
    is_running=True

    while is_running:
        print("************************")
        print("Banking Program")
        print("************************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("************************")

        choice=input("Enter your choice(1-4) ")
        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance+=deposit()
        elif choice=="3":
            balance-=withdraw(balance)
        elif choice=="4":
            is_running=False
        else:
            print("Enter a valid Number ")
    
    print("************************")
    print("Thank you ! Have a great day ")
    print("************************")
if __name__=='__main__':
    main()
  
