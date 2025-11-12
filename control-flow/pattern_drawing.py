# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Initialize the row counter
counter = 0
# Outer loop controls the number of rows
while counter < size:
    # Inner loop prints the asterisks on the same line
    for column in range(size):
        print("*", end="")
    # Move to a new line after each row
    print()
    counter += 1
