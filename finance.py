def personalFinance(*args):

    Salary = float(input("Please enter the salary"))

    ExtraIncome= float(input("Please enter the any other extra income if you have"))

    Pf = int(input("Please enter the PF"))

    HRA = int(input("Please enter the HRA"))

    Monthly_Food = float(input("Please enter the montly"))

    Education_Investment = int(input("Please enter the total amount monthly to invest in education"))

    Travelfashion = float(input("Please enter the amount for the allocated for travel&fashion"))

    financialinvestmentAmount = (Salary + ExtraIncome) - (Pf + HRA + Monthly_Food + Education_Investment + Monthly_Food + Travelfashion)

    print(f"Congratulations, your financialinvestment for upcoming month is {financialinvestmentAmount} but we advise you save something for in account  and dont forget to do some SIP and mutual funds, remeber mutual funds are subjected to market risk, please read all documents carefully")