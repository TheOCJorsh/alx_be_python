# This script generates a multiplication table for any number entered by the user.
# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))
# To print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} *  {i} = {number * i}")
