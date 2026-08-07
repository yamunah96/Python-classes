from customers import create_customer
from transactions import deposit_amount,withdraw_amount,check_balance,transfer_money,generate_transaction_report,view_log

from logger import get_logger
logger = get_logger()
def Bank_system():
    while True:
        # Taking the user input for the options
        try:
            options = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter numbers only")
            continue
        if  options==1:
            create_customer()
        elif options ==2:
            deposit_amount()
        elif options ==3:
            withdraw_amount()
        elif options==4:
            account_number= input("Enter your account number to check balance: ").strip()
            check_balance(account_number)
        elif options==5:
            transfer_money()
        elif options==6:
            generate_transaction_report()
        elif options==7:
            view_log()
        elif options==8:
            # exiting the program
            logger.info("Exit from the menu")
            print("Thanks for visiting HDFC Bank")
            break
        else:
            logger.error("Wrong menu option picked")
            print("Pick the correct options")

if __name__ == "__main__":
    print("="*100)
    print('                                        Welometo HDFC Bank                    ')
    print("="*100)
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer Money\n6. Generate Transcation Report\n7. View log\n8. Exiit")
    Bank_system()