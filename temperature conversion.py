selection = input('1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n')
try:
    selection = int(selection)
except:
    print("You've not entered a number")
    quit()

if selection == 1:
    inp = input('Enter Celsius temp: ')
    try:
        celsius = float(inp)
        fahrenheit = float(celsius * 1.8) + 32
        fahrenheit = round(fahrenheit, 1)
        print('Fahrenheit temp: ', fahrenheit)
    except:
        print('Please enter a number')
elif selection == 2:
    inp = input('Enter Fahrenheit temp: ')
    try:
        fahrenheit = float(inp)
        celsius = float((fahrenheit - 32) / 1.8)
        celsius = round(celsius, 1)
        print('Celsius temp: ', celsius)
    except:
        print('Please enter a number')
else:
    print('Please choose either 1 or 2')
