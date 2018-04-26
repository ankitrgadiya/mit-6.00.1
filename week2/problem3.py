def calcBalance(balance, yearRate):
    """
    Input: balance Total balance, yearRate Annual Interest Rate
    Output: Fixed monthly payment to clear all the debt in 1 year
    """
    def checkBalance(balance, fixMonthly):
        """
        Input: balance Total balance, fixMonthly fixed monthly payment
        Output: Checks if fixMonthly clears of all the debt and returns -1, 0
                or 1 accordingly
        """
        month = 12
        while month > 0:
            balance -= fixMonthly
            balance += (yearRate / 12.0) * balance
            month -= 1
        balance = round(balance)
        if balance == 0:
            return 0
        elif balance > 0:
            return 1
        else:
            return -1

    lower = balance / 12.0
    upper = (balance * ((1 + (yearRate / 12.0)) ** 12)) / 12.0
    fixed = (lower + upper) / 2.0
    while True:
        remain = checkBalance(balance, fixed)
        if remain == 0:
            return round(fixed, 2)
        elif remain > 0:
            lower = fixed
            fixed = (lower + upper) / 2.0
        else:
            upper = fixed
            fixed = (lower + upper) / 2.0


print(calcBalance(999999, 0.18))
