import random

from data import customer_data

from validation import validate_account_number
from utils import account_exist

from logger import get_logger
logger = get_logger()


def create_customer(balance=1000):
    ''' create new customer, by default balance is 1000, genrate unique account number
        One customer name → One account
        Every account number is unique
    '''
    while True:
        customer_name= input("Enter your name: ").lower().strip()
        if not customer_name:
            logger.error("Customer name not entered.")
            print("Customer name should not be empty, try again")
            continue
        if not customer_name.isalpha():
            logger.error(f"Customer name not contain alpha characaters")
            print("customer name must contain alpha characaters, no digits and special characters..")
            continue
       
        for account,data in customer_data.items():
            if customer_name == data['name']:
                logger.info(f"{customer_name.title()} account is already exists")
                print(f"{customer_name.title()} your account is already exists, enter your account number will verfiy")
                account_number= input("Enter your account no: ").strip()
                validate_account_number(account_number)
                if account_exist(account_number):
                    logger.info(f"{customer_name.title()} Account verified successfully")
                    print("Account verified successfully.")
                    logger.info(f"{customer_name.title()} You already have an account in our bank")
                    print("You already have an account in our bank")
                    return
                else:
                    logger.error(f"Incorrect account number  Account: {account_number}")
                    print("Incorrect account number.")
                    return

        # generating unique account number
        while True:
            account_number=''
            for i in range(5):
                # generating the random number between 0 to 9 and adding to the account number
                account_number+= str(random.randint(0,9))
            for account in customer_data:
                # checking the account number is already exist or not because account number should be unique for each customer
                if  account_number == account:
                    logger.info(f"{customer_name.title()} account number already exist,create a new account number")
                    print(f"account number already exist....")
                    break
            if not account_exist(account_number):
                break
            
        # store the account details in dict
        customer_data[account_number]={
            "name":customer_name,
            "balance":balance
        } 
        logger.info(f"{customer_name.title()} Account created successfully | Account {account_number}")
        print("\nAccount created successfully.")
        print(f"Customer Name : {customer_name.title()}")
        print(f"Account Number: {account_number}")
        print(f"Balance       : ₹{balance}")

        return
       


