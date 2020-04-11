#!/usr/bin/python37
import os.path
import argparse

parser = argparse.ArgumentParser(description='This program finds the nth number in the Fibonacci sequence and outputs to the file directed.')

parser.add_argument('-n', metavar='number', dest='number', type=int, nargs="+", help="Sequence number in Fibonacci sequence")
parser.add_argument('-f', metavar='filename', type=str, nargs="+", help="String for file name")

args = parser.parse_args()
number = args.number
print(args.number)

filename=input("What is the name of the file: ")
number=input("How many terms: ")

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

for number in range(0,number+1):
    print(fibonacci(number))

try:
    f = open(filename, "w")

    for number in range(0,number+1):
        f.write(str(fibonacci(number)) + "\n")

except:
    print("Error")

f.close()