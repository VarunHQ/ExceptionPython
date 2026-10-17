print("Welcome to the Food Bill Calculator!")
valid = False

while not valid:
    try:
        bill = float(input("Enter the bill amount (In decimals): "))
        discount = float(input("Enter the Discount amount (In decimals): "))
        people = int(input("Enter the number of people (Whole numbers only): ")) 
        
        final_bill = bill - discount
        payment_for_each = final_bill / people
        
    except ValueError:
        print("Please enter only valid numbers given in each field.")
        
    except ZeroDivisionError:
        print("Number of people cannot be zero.")
        
    else:
        print("Final bill is:", final_bill)
        print("Payment for each person is:", payment_for_each)
        valid = True 
        
    finally:
        print("Attempt Finished. Thank you for using this program to calculate your food bill!")
