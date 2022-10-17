

# ATM MACHINE
acctBal = 100000
cardPin = 2020
welcomeOption = """Select an option:
1. Withdrawal
2. Transfer
3. Check Balance
4. Airtime Top-Up
5. Change pin
6. Cancel or exit
"""

userPin = int(input("Enter pin >> "))

if userPin == 2020:
    print(welcomeOption)
    userOption = int(input(">> "))
    if userOption == 1:
        withdrawalAmount = int(input("Enter amount >> "))
        if withdrawalAmount <= acctBal:
            acctBal = acctBal - withdrawalAmount
            print(f'Please take your cash! | AvalBal = {acctBal}')
        else:
            print('insufficent balance, please fund your account')
    elif userOption == 2:
        transferAmount = int(input("enter transfer amount >>"))
        if transferAmount <= acctBal:
            acctBal = acctBal - transferAmount
            print(f"After this transaction your balance will be {acctBal}, do you still want to be broke?")
            Bank = input("type the name of the bank >>")
            accountNo = int(input("Enter Account Number >> "))
        else:
            print(f"insufficient fund, your account balance is {acctBal}")
    elif userOption == 3:
        print(f"your account balance is {acctBal}")
    elif userOption == 4:
        rechargeAmount = int(input("Enter recharge amount"))
        if rechargeAmount <= acctBal:
            acctBal = acctBal - rechargeAmount
            Network = """Select the network to recharge:
            1. MTN
            2. Airtel
            3. 9Mobile
            4. GLO
            """
            print(Network)
            networkChoice = int(input("select network"))
            rechargeNumber = int(input("enter phone number"))
            print(f"recharge of {rechargeAmount} was sucessful")
        else:
            print(f'insufficient balance')
    elif userOption == 5:
        pin = int(input("enter card pin"))
        if pin == cardPin:
            newPin = int(input("Enter new Pin"))
            confirmPin = int(input("confirm Pin"))
            if newPin == confirmPin:
                print("pin changed succesfully")
            else:
                print("pin did not match")
        else:
            print("incorrect pin")
    elif userOption == 6:
        choice = input("do you want to perform another transaction?")
        if choice == "yes":
            print(welcomeOption)
        else:
            print("Thank you!!! please take your card")
else:
    print("Incorrect PIN")
