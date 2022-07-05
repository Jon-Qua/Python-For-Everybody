score = input('Enter score: ')
try:
    score = float(score)
except:
    print('Bad score')
    quit()
if 0.9 <= score <= 1.0:
    grade = 'A'
elif 0.8 <= score < 0.9:
    grade = 'B'
elif 0.7 <= score < 0.8:
    grade = 'C'
elif 0.6 <= score < 0.7:
    grade = 'D'
elif score < 0.6:
    grade = 'F'
else:
    print('Bad score')
    quit()
print('Your grade is: ', grade)
