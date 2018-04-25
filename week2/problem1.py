def calcBalance(balance, month, monRate, yearRate):
    """
    Input: balance to start with, month number of months, monRate Monthly
           Payment Rate, yearRate Annual Interest Rate
    Output: Remaining balance after "month" months rounded to 2 decimal places
    """
    while month > 0:
        balance += (yearRate / 12.0) * balance
        balance -= monRate * balance
        month -= 1

    return round(balance, 2)

print(calcBalance(484, 12, 0.04, 0.2))
