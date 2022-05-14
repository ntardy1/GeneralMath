'''
A Program to Calculate the Period of the Decimal Representation of the Reciprocal of a Prime Number
The program utilizes the fact that the maximum period will be equal to prime-1 (Max Period = prime - 1)
Author: Nathan Tardy
Date: May 2022
'''
import math
import os
import random

rawData = open("primes-to-100k.txt", "r")
dataset = rawData.readlines()
rawData.close()

def primeReciprocalPeriod(prime):
    # Declaring necessary variables
    numbersList = [] # A list for the digits of the quotient
    primeLength = 0 # The length of the prime, measured in digits
    # Cleaning the data (if necessary)
    prime = str(prime)
    prime.strip('\n')
    prime = int(prime)
    # Getting the length of the prime (digits)
    strPrime = str(prime)
    for num in strPrime:
        primeLength += 1
    # Math to calculate the first number (first digit of the quotient)
    # Long Division
    dividend = 10*int(primeLength)
    number = math.floor(dividend/prime)
    numbersList.append(number)
    # Loop that keeps calculating digits of the quotient
    while True:
        dividend = (dividend-(prime*number))*10
        # In some cases, the prime is still greater than the dividend
        # For this, append a '0' to the numbers list (quotient digits) and then multiply the dividend by 10
        while (dividend < prime):
            numbersList.append(0)
            dividend = dividend * 10
        number = math.floor(dividend/prime)
        numbersList.append(number)
        # Changing the operations performed once the length of the numbers list is 2*prime - 1
        if (len(numbersList) == 2*(prime - 1)):
            # Indexing technique to figure out the length of the reciprocal period
            if (prime <= 5):
                index = 1
            else:
                index = 2
            while True:
                # As the value of index decreases, once it reaches a point where the value of index
                # splits the list into two identical segments, the period has been found
                if (numbersList[0:index] == numbersList[index:2*index]):
                    return (len(numbersList[0:index]))
                else:
                    index += 1

os.system('cls')

print("Welcome to the 'Shanks Bot'")
print("The program will return the period of the decimal representation of its reciprocal")
choice = int(input("Random Prime (1) or Enter a Prime (2): "))
if (choice == 1):
    prime = dataset[random.randint(0, len(dataset))]
    print(f"Prime: {prime}")
    print(f"Period: {primeReciprocalPeriod(prime)}")
elif (choice == 2):
    prime = int(input("Input a prime number: "))
    print(f"Period: {primeReciprocalPeriod(prime)}")
