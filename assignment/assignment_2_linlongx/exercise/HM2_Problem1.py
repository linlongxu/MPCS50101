#Create a temperature converter program


p_1 = True

while (p_1):

    x=float(input("Enter a temperature in Fahrenheit:"))


    if x % 1==0 and x > 0:

        dc = (x - 32) * 5 / 9
        print ('The temperature is ', dc, 'in Celsius.')


    else:

        print ('Please enter a positive, whole number numeric termperature.')

