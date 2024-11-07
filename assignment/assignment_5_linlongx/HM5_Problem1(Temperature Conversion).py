def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        return round((fahrenheit - 32) * 5 / 9, 2)
    except ValueError:
        return None