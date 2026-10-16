try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 / num2
    print("Result is: ", result)

except ZeroDivisionError as ex:
    print("Division of zero is not possible.")

except ValueError as ex:
    print("Choose only whole numbers.")

except:
    print("Invaild input.")

else:
    print("Division done!")

finally:
    print("Finally block will execute no matter what exception happens. ")
