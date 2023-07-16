def financial_calculator(principal, interest_rate, years):
 

  future_value = principal * (1 + interest_rate) ** years
  return future_value

def main():
  principal = 100000
  interest_rate = 0.1
  years = 1

  future_value = financial_calculator(principal, interest_rate, years)
  print("The future value of the investment is Rs", round(future_value))

if __name__ == "__main__":
  main()