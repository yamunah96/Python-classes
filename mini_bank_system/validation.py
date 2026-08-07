from exceptions import InvalidAmountError,InsufficientBalanceError,InvalidAccountNumber
from logger import get_logger

logger = get_logger()
def validate_amount(amount):
    '''checks the valid amount entered by customer'''
    logger.error(f"Invalid Amount Entered : {amount}")
    if amount<=0:
        raise InvalidAmountError("Amount should be greater than zero")

def validate_balance(balance,amount):
    '''checks the amount should lesser than balance'''
    logger.error(f"Insufficient Balance | Available : {balance} | Requested : {amount}")
    if amount >= balance:
        raise InsufficientBalanceError("Insufficient Balance")
    
def validate_account_number(account_no):
    if not account_no.isdigit():
        logger.error(f"Account number should be digit")
        raise InvalidAccountNumber("Account number should be digit")
    if account_no=='':
        logger.error(f"Wrong account number") 
        raise InvalidAccountNumber("Enter correct account number")
