#Problem 4

P_4 = True

while P_4:

    try:
        user_input = input("""Please enter three numbers
as the format of a, b, c: """)
        a, b, c = user_input.split()



        def max_of_three(a, b, c):
            if a >= b and a >= c:
                return a
            elif a >= b and a <= c:
                return c
            else:
                return b
        max_number = max_of_three(a, b, c)

        print ("The largest number is: ", max_number)

    except ValueError:
        print ("Please enter three numbers as the correct format!!!")
