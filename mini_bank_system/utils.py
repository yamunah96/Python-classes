from data import customer_data
import random

def account_exist(account_number:str)->bool:
    '''checkng the account is exist on data  using accout number'''
    return account_number in customer_data

def generate_account_number():
    '''Using random module bank creates an unique 5 digit account number to new customer '''
    while True:
        account_number = ""
        for _ in range(5):
            account_number += str(random.randint(1,9))
        if account_number not in customer_data:
            return account_number   
