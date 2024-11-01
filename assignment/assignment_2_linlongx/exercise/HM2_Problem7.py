#Problem7
P_7 = True
while P_7:
    try:
        height = int(input("Please enter the height of pyramid: "))

        def pyramid(height):
            for i in range(1, height + 1):
                print('*' * i)

        pyramid(height)

    except:
        print ("Please enter the integer.")