# Ask user for width and loop until they 
# enter a number that is more than zero
def number_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

#Main Routine Goes here
for item in range(0, 2):
    width = number_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = number_check("Height: ")
    print(height)
