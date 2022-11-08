import csv
import os

def userinp():
    first = input('Enter First Name: ')
    last = input('Enter Last Name: ')
    email = input('Enter Email: ')

#def writecsv():
    with open('test.csv', 'a', newline='') as csvfile:
        fieldnames = ['first','last','email']
        csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        csv_writer.writerow({'first': first,'last': last,'email': email})

def readcsv():
    with open('test.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for line in csv_reader:
            print(line['first'])

userinp()
readcsv()