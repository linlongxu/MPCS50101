# Problem 2
P_2 = True

while (P_2):
    try:
        x = int(input("Enter a score: "))

        if x % 1 == 0 and x > 0:
            if x >= 90 and x<=100:
                print ("You received an A!")

            elif x >= 80 and x<90:
                print ("You received a B!")

            elif x >= 70 and x<80:
                print ("You received a C!")

            elif x >= 60 and x<70:
                print ("You received a D!")

            else:
                print ("You received a F!")
    except:
        print ("That is not valid input.")