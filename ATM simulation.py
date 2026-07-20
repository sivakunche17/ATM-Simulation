
#3rd Mini Project
#ATM Simulation

balance=10000
pin=9110

while True:
    print("\n========= ATM ==========")
    print("1. check balance: ")
    print("2. deposit: ")
    print("3. withdraw: ")
    print("4. exit: ")
    print("========================")

    choice = (input("enter your choice (1-4): "))

    if choice == "4":
        print("\nTHANK YOU")
        print("\nvisit again\n")
        break

    _pin = int(input("enter your Pin: "))
    if _pin == pin:
        if choice == "1":
            print("\nBalance:", balance)
        elif choice == "2":
            amount=int(input("enter your amount: "))
            balance=balance+amount
            print("\nDeposit Sucessful")
            print("Current balance:", balance)
        elif choice == "3":
            amount=int(input("enter your amount: "))
            if amount <= balance:
                balance = balance-amount
                print("\nWithdraw Sucessful")
                print("please take your cash")
                print("Current balance:", balance)
            else:
                print("insufficient Balance")
                break
        else:
            print("invalid Entered")
            print("Time out")
            break
    else:
        print("wrong pin")
        break
