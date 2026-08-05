# default taken the accounts details for testing purpose
accounts={
     "yamuna":{
          "account_number":'1234',
          "balance":5000
     },
    "shiva":{
        "account_number":'4567',
        "balance":2000
    }
}

# random module is used to generate the random account number for the customer
import random
print('***********          Welometo HDFC Bank            **********')
print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer Money\n6. Show All Accounts\n7. Exit")

while True:
    # Taking the user input for the options
    try:
        options = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if  options==1:
        customer_name=input("Enter your name to create an account: ").lower().strip()
        # validation for the customer name
        if customer_name == " ":
            print("Customer name should not be empty, try again")
            continue
        if not customer_name.isalpha():
            print("customer name must contain alpha charesters, no digits and special characters..")
            continue
        # checking the customer name is already exist or not
        if customer_name in accounts:
            print(f"{customer_name} your account is already exits, enter your account number will verfiy")
            account_number= input("Enter your account no: ").strip()
            # checking the account number is already exist or not
            if accounts[customer_name]["account_number"] == account_number:
                print(f"{customer_name} your account is exist in our bank, kindly create account with other details..")
        else:
            # generating the random account number for the new customer
            account_number=''
            for i in range(5):
                # generating the random number between 0 to 9 and adding to the account number
                account_number+= str(random.randint(0,9))
                exist=False
                for name,data in accounts.items():
                    # checking the account number is already exist or not because account number should be unique for each customer
                    if  account_number == data['account_number']:
                        print(f"account number already exist....")
                        exist=True
                        break
                if exist:
                    account_number=''
                    continue
            print(f"{customer_name} your account created succesfully")
                
            # store the account details in dict
            accounts[customer_name]={
                "account_number":account_number,
                "balance":1000
            }            
        
        print(accounts)
    elif options==2:
        found=False
        print("Enter below details to deposit the amount")
        # taking the account number from the user to deposit the amount
        account_number= input("Enter your account number: ").strip()
        for name,data in accounts.items():
            # checking the account number is correct or not
            if account_number == data['account_number']:
                found=True
                customer_name= input("Enter your name:  ").lower().strip()
                while True:
                    amount= float(input("Enter the amount: "))
                    # checking the amount is valid or not
                    if amount>0:
                        data["balance"]+=amount
                        msg= f"{customer_name} is deposited {amount} rupees succefully"
                        print(msg)
                        break
        if not found:
            print("Incorrect account number Try again..")
            break
        print(accounts) 

    elif options==3:
        print("Enter below details to withdraw the amount")
        # taking the account number from the user to withdraw the amount
        account_number= input("Enter your account number: ").strip()
        # iterating the accounts dict to check the account number is correct or not
        for name,data in accounts.items():
            if account_number == data['account_number']:
                customer_name= input("Enter your name:  ")
                while True:
                    amount= float(input("Enter the amount: "))
                    #   checking the amount is valid or not and also checking the balance is sufficient or not
                    if amount>0:
                        # checking the balance is sufficient or not
                        if amount<data['balance']:
                            data["balance"]-=amount
                            msg= f"{customer_name} is withdraw the {amount} rupees succefully"
                            print(msg)
                            break
                        else:
                            print("In suffiecient balance")
                            break
                    else:
                        print("enter the valid amount")
            else:
                print("Incorrect account number Try again..")
                break
        print(accounts) 
    elif options==4:
       found=False
        # checking the balance of the customer using the account number
       account_number= input("Enter your account number to check balance: ").strip()
       for name,data in accounts.items():
           if account_number == data['account_number']:
               print(f"Current Balance is: {data['balance']} Rupees")
               found=True
               break
       if not found:
            print("Incorrect account number Try again..")
            break

    elif options==5:
        print("Enter the below details to transfer the amount ")
        # taking the sender name and account number to transfer the amount
        sender_name= input("Enter your name: ").lower().strip()
        if sender_name in accounts:
            account_number= input("Enter your account number to: ").strip()
            # checking the account number is correct or not for the sender name
            if account_number == accounts[sender_name]['account_number']:
                # taking the receiver name and account number to transfer the amount
                recevier= input("Enter recevier name to send an amount: ").lower().strip()
                if recevier in accounts:
                    recevier_account_number= input("enter recevier account number: ").strip()
                    if  recevier_account_number == accounts[recevier]['account_number']:
                        amount= float(input("Enter the amount: "))
                        # checking the amount is valid or not and also checking the balance is sufficient or not
                        if amount> 0:
                            if amount<= accounts[sender_name]['balance']:
                                accounts[sender_name]['balance']-=amount
                                accounts[recevier]['balance']+=amount
                                print(f"{sender_name} transferred {amount} to {recevier}")
                    else:
                        print(f"{recevier} account number is incorrect")
                        break
                else:
                    print(f"{recevier} account is not exist")
                    break
            else:
                print("enter the correct account number")
                break

        else:
            print(f"{sender_name} is not exist in our bank")
            break

    elif options==6:
        # displaying all the account details of the customers
        print("***                  All Account details                      ***")
        print("="*100)
        for name,data in accounts.items():
            print(f"Customer Name: {name}, Account_number: {data['account_number']}, Balance: {data['balance']}")
        print("="*100)

    elif options==7:
        # exiting the program
        print("Thanks for visiting HDFC Bank")
        break
    else:
        print("Pick the correct options")

'''
Show total money stored in the bank.
Display richest customer.
'''
total=0
richest_customer=''
largest_amount=0
# iterating the accounts dict to calculate the total amount in the bank and also finding the richest customer
for name,data in accounts.items():
    total+= data['balance']
    if data['balance'] > largest_amount:
        largest_amount= data['balance']
        richest_customer=name

print(f"The total amount in the bank is {total} Rupees")
print(f"The Richest Person Who saved highest monet in our bank is {richest_customer}")
