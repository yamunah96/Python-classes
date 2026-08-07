class InsufficientBalanceError(Exception):
    """Raised when the account has insufficient balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when the amount is invalid."""
    pass

class InvalidAccountNumber(Exception):
    """Raised when the account number is not digit and empty"""
    pass