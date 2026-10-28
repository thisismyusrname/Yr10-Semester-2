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
#Main Routine starts here

keep_going = ""
while keep_going == "":
    print(f"Welcome to Fence Cost Calculator")
#Width"
    width = number_check((f"Enter Width: "))
#Length
    length = number_check((f"Enter Length: "))
    print()
#Calculate the perimeter
    perimeter = 2 * (length + width)
#Display result
    print(f"Perimeter={perimeter}m")
    print()
#Cost per m
    price_per_m = number_check("Price per m: ")
    print()
# Calculate Cost for the fence
    fence_cost =  perimeter * price_per_m
    print(f"Fence = ${fence_cost}")
    print()
#Final Cost
    print(f"That will cost ${fence_cost}")
    print()
# End or continue the loop
    keep_going = input("Press Enter to continue, or any key to quit: ")
print("Thank you for using the Fence Cost Calculator")