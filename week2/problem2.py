def calcBalance(balance, yearRate):
    """
    Input: balance Total balance, yearRate Annual Interest Rate
    Output: Lowest fixed monthly payment to clear all the debt in 1 year
    """
    def checkBalance(balance, fixMonthly):
        """
        Input: balance Total balance, fixMonthly fixed monthly payment
        Output: Checks if fixMonthly clears of all the debt and returns boolean
        """
        month = 12
        while month > 0:
            balance -= fixMonthly
            balance += (yearRate / 12.0) * balance
            month -= 1
        if balance <= 0:
            return True
        else:
            return False

    fixed = 10
    while True:
        if checkBalance(balance, fixed):
            return fixed
        else:
            fixed += 10


print(calcBalance(3926, 0.2))
