from utils import account_exist
from data import customer_data
from validation import validate_amount,validate_balance,validate_account_number

from logger import get_logger
logger = get_logger()

def deposit_amount():
    try:
        account_no= input("Enter the account no: ").strip()
        validate_account_number(account_no)
        if not account_exist(account_no):
            logger.error(f"Deposit Failed | Invalid Account Number : {account_no}")
            print("Account not found")
            return
        amount= float(input("Enter amount: "))
        validate_amount(amount)
        logger.info(f"Deposit Successful | Account : {account_no} | Amount : {amount}")
        customer_data[account_no]['balance']+= amount
        print(f"₹{amount} deposited successfully")
        
    except Exception as e:
        logger.exception(
            f"Deposit Failed | Account : {account_no}"
        )
        print(e)

    
def withdraw_amount():
    try:
        account_no= input("Enter the account no: ").strip()
        validate_account_number(account_no)
        if not account_exist(account_no):
            logger.error(f"Deposit Failed | Invalid Account Number : {account_no}")
            print("Account not found")
            return
        amount= float(input("Enter amount: "))
        validate_amount(amount)

        validate_balance(customer_data[account_no]['balance'],amount)
        logger.info(f"Withdraw Successful | Account : {account_no} | Amount : {amount}")
        customer_data[account_no]['balance']-= amount
        print(f"₹{amount} withdraw successfully")

        try:
            answer= input("You want check balance Yes/No: ").lower().strip()
            if answer == "yes" or answer =="y":
                check_balance(account_no)
        except Exception as e:
            logger.exception(f"Checking balance failed | Account : {account_no}")
            print(e) 
    except Exception as e:
        logger.exception(f"Withdrawal Failed | Account : {account_no}")
        print(e)


def check_balance(account_number):
    validate_account_number(account_number)
    if account_number in customer_data:
        logger.info(f"Balance fetched successfully | Account : {account_number}")
        print(f"Current Balance is: {customer_data[account_number]['balance']} Rupees")
        return
    logger.error(f"Incorrect account number entered | Account : {account_number}")
    print("Incorrect account number Try again..")


def transfer_money():
   try:
        sender_acc_no= input("Enter your account number: ").strip()
        validate_account_number(sender_acc_no)
        receiver_acc_no= input("Enter reciever account number: ").strip()
        validate_account_number(receiver_acc_no)

        if not account_exist(sender_acc_no):
            logger.error(f"Transaction Failed, Incorrect sender account number | Sender Account : {sender_acc_no}")
            print("Transaction Failed, Incorrect sender account number.")
            return
        if not account_exist(receiver_acc_no):
            logger.error(f"Transaction Failed, Incorrect receiver account number |Receiver Account : {receiver_acc_no}")
            print("Transaction Failed,Incorrect receiver account number.")
            return
        if sender_acc_no == receiver_acc_no:
            logger.error(f"Transaction Failed, Sender and receiver account cannot be the same  | Sender Account : {sender_acc_no} |Receiver Account : {receiver_acc_no}")
            print("Transaction Failed,Sender and receiver account cannot be the same.Can't send the amount")
            return
        
        amount = float(input("Enter amount: "))
        validate_amount(amount)
        sender_balance=customer_data[sender_acc_no]['balance']
        validate_balance(sender_balance,amount)
        logger.info(f"Transfer Successful | Sender:{sender_acc_no} | Receiver:{receiver_acc_no} | Amount:₹{amount}")
        customer_data[sender_acc_no]["balance"] -= amount
        customer_data[receiver_acc_no]["balance"] += amount

        print(f"₹{amount} Transfered successfully.")
        
   except ValueError as e:
       logger.exception("Transfer Failed")
       print(e)
            

def generate_transaction_report():
    deposits = 0
    withdrawals = 0
    transfers = 0
    success = 0
    failed = 0

    with open("banklog.txt", "r") as file:
        for line in file:
            if "Deposit Successful" in line:
                deposits += 1
                success += 1
            elif "Withdraw Successful" in line:
                withdrawals += 1
                success += 1
            elif "Transfer Successful" in line:
                transfers += 1
                success += 1
            elif "ERROR" in line:
                failed += 1
    print("=" * 50)
    print("        TRANSACTION REPORT")
    print("=" * 50)

    print(f"Total Deposits       : {deposits}")
    print(f"Total Withdrawals    : {withdrawals}")
    print(f"Total Transfers      : {transfers}")
    print(f"Successful           : {success}")
    print(f"Failed               : {failed}")

    print("=" * 50)

def view_log():
    print("=" * 50)
    print("        Log Data")
    print("=" * 50)
    with open("banklog.txt", "r") as file:
        for line in file:
            print(line)
