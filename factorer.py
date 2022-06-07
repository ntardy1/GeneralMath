
# A program designed to test for the Primality of
# an input number

# Importing libraries
import math

# Funcion for testing the primality of an input number
def testPrimality(number):
    testNumber = number
    possibleFactorsList = []
    factorsList = []

    # For loop used to append all possible factors of the number (1-number)
    # to a list named such
    for factor in range(1, testNumber + 1):
        possibleFactorsList.append(factor)

    # For loop used to check every number of the possibleFactorsList
    for possibleFactor in range(1, testNumber + 1):

        # If the number is greater than 10,000 then the user will
        # see a progress bar during execution
        if testNumber >= 10000:
            # Creating an array of evenly spaced values (0.1-0.9)
            percentagesList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            # For loop to check possibleFactor for compatibility
            # with each value in the percentagesList
            for percentage in percentagesList:
                if possibleFactor == math.floor(percentage*testNumber):
                    percent = (possibleFactor/testNumber)*100
                    print(f"{percent} %")
        if math.remainder(testNumber, possibleFactor) == 0:
            factorsList.append(possibleFactor)
    return factorsList

# Getting user input for number to test
number = int(input("Test number: "))

# Running function to test for primality of input number
factorsList = testPrimality(number)

# Displaying final output based on results of program
if len(factorsList) == 2:
    print(f"Primality: True \nFactors: {factorsList}")
else:
    print(f"Primality: False \nFactors: {factorsList}")
