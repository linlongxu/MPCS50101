#Create a temperature converter program


try:
    x=float(input("Enter a temperature in Fahrenheit:"))
    dc = (x - 32) * 5 / 9
    print ('The temperature is ', dc, 'in Celsius.')

except:
        print ('Please enter a valid number numeric termperature.')