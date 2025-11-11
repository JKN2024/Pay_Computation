# compute grade
def computegrade(Grade):
    
    if 0.0 <=Grade>=1.0 :
        print('Enter a score between 0.0 and 1.0')
    elif Grade >= 0.9:
        print('Congratulations your grade is A')
    elif Grade >= 0.8 :
        print('Congratulations your Grade is B')
    elif Grade >= 0.7 :
        print('Your Grade is C')
    elif Grade >= 0.6:
        print('Your Grade is D')
    elif Grade >= 0.5 :
        print('Your Grade is F')
    else :
        print('Please enter a numerical Value')
score=float(input('Enter Grade: '))
Grade = computegrade(score)
print('Grade: ', Grade)
computegrade
