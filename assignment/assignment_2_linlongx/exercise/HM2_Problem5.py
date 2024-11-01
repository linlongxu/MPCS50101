#Problem 5

P_5 = True
while P_5:

    try:
        number = input("Please enter a number: ")
        sum = 0

        for i in range(len(number)):
            digit = int(number[i])
            if i % 2 != 0:
                sum += digit
            else:
                sum-= digit

        if sum % 11 == 0:
            print ("This number can be devisible by 11.")
        else:
            print ("This number can't be devisible by 11.")

    except ValueError:
        print ("Please enter a integer.")