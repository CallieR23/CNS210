#!/usr/bin/python37
import os.path
import argparse

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

def main():

    parser_formatter= argparse.ArgumentDefaultsHelpFormatter 
    parser = argparse.ArgumentParser(description='This program finds the nth number in the Fibonacci sequence and outputs to the file directed.', formatter_class=parser_formatter)

    parser.add_argument('-n', dest='number', required=True, type=int, help="Sequence number in Fibonacci sequence")
    parser.add_argument('-f', dest='filename', required=True, type=str, help="String for file name")

    args = parser.parse_args()
    number = args.number
    print(args.number)
    print(args.filename)

    #filename=input("What is the name of the file: ")
    #number=int(input("How many terms: "))

    for n in range(0,int(number)+1):
        print(fibonacci(n))

    try:
        f = open(args.filename, "w")

        for number in range(0,number+1):
            f.write(str(fibonacci(number)) + "\n")

    except:
        print("Error")

    f.close()
if __name__ == '__main__':
    main()