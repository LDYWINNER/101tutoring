

def calculateEarnings():
    initialMoney = float(input('How much money are you investing? '))
    interestRate = float(input('What is the yearly interest rate (%)? '))
    year1 = initialMoney * (1 + interestRate / 100)
    year10 = initialMoney * (1 + interestRate / 100) ** 10
    year20 = initialMoney * (1 + interestRate / 100) ** 20
    year30 = initialMoney * (1 + interestRate / 100) ** 30
    print('After 1 year: ', '{:.2f}'.format(year1))
    print('After 10 years: ', '{:.2f}'.format(year10))
    print('After 20 years: ', '{:.2f}'.format(year20))
    print('After 30 years: ', '{:.2f}'.format(year30))

calculateEarnings()