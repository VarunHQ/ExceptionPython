valid = False

while not valid:
    try:
        n = int(input("Enter number: "))
        while n % 2 == 0:
            print("bye!")
            n = int(input("Enter number: "))
        valid = True
    except ValueError:
        print("Invalid input.")