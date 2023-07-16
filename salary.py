# Calculate the yearly salary with adjusted holidays and vacations
salary = int(input("Enter the salary amount per Hour: "))
hoursPerWeek = 40
daysPerWeek = 5
holidaysPerYear = 10
vacationsPerYear = 15

unadjustedSalary = salary*hoursPerWeek*52

adjustedSalary = unadjustedSalary - (salary*(hoursPerWeek//daysPerWeek)*(holidaysPerYear+vacationsPerYear))

print("Holidays & vacation days adjusted salary per year: ",adjustedSalary,"dollars")