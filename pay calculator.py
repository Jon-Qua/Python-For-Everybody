# Collecting hours with error checking
hours = input('How many hours did you work this week? ')
try:
    hours = float(hours)
except:
    print("You did not enter a number.")
    quit()
if hours < 1:
    print("You did not enter a positive number of hours.")
    quit()

# Collecting pay rate with error checking
rate = input('What is your hourly pay rate? ')
try:
    rate = float(rate)
except:
    print("You did not enter a number.")
    quit()
if rate < 1:
    print("You did not enter a positive hourly pay rate.")
    quit()

# Display pay rate -- 1.5x hourly rate for hours above 40
if hours < 41:
    pay = hours * rate
    pay = round(pay, 2)
    print('You earned £', pay)
else:
    pay = 40 * rate
    pay = pay + ((hours - 40) * (rate * 1.5))
    pay = round(pay, 2)
    print('You earned £', pay)
