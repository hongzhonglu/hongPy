# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-

'''
Here are four key best practices about main() in Python that you just saw:

Put code that takes a long time to run or has other effects on the computer in a function or class, so you can control exactly when that code is executed.

Use the different values of __name__ to determine the context and change the behavior of your code with a conditional statement.

You should name your entry point function main() in order to communicate the intention of the function, even though Python does not assign any special significance to a function named main().

If you want to reuse functionality from your code, define the logic in functions outside main() and call those functions within main().

'''

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()