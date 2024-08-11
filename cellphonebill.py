
# verizon code
# python 3.12
# takes in 4 peoples bill then the total bill #b1 through b3
# (total bill - 4 people) = x
# x/4 = r 
#output
#b1+r 
#b2+r
#b3+r 
#br4+r

# Get user inputs directly as floats
first, second, third, fourth = map(float, input("Enter a, b, c and d (separated by spaces): ").split())
bill = float(input("Enter the total bill amount: $"))
month = str(input("Enter the this month "))

# Calculate total spent and remaining amount
total_spent = first + second + third + fourth
remaining = bill - total_spent

if remaining == 0:
    print("the values you entered has no remainder it is all equal")
else:
    # Validate if total can be split equally
    if remaining <= 1 :
        print("maybe overage??")
        print("Error: The total bill is having issues being split equally into three parts.")
    else:
        # Calculate amount to be split (assuming equal split) 
        # the numner of total people 
        split_amount = remaining / 4

        # Print results with formatted output for two decimal places
        print("\n")
        print(f"Remaining amount: ${remaining:.2f}")
        print(f"total spent for 4 people: ${total_spent:.2f}")  
        
        print("Verizon Bill :")
        print("\n")
        print("Due the 4th of " + month + " 2024")
        print("Bill total: $" + str(bill))
        print("\n")
        print(f"paid ❌ tony: ${first + split_amount:.2f}")
        print(f"paid ❌ bob: ${second + split_amount:.2f}")
        print(f"paid ❌ debbie: ${third + split_amount:.2f}")
        print(f"paid ❌ scott: ${fourth + split_amount:.2f}")

        print("\n")
        print(f"value amount needed per person times: ${split_amount:.2f}")

        #math using round() to get the value to subtract from remaining
        rsplit_amount = round(split_amount, 2)
        check = float(remaining) - (rsplit_amount*4) 
        
        print("\n")
        print(f"the difference for this is the following: ${check:.2f}")

       
