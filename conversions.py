
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0
    
    kelvins = float(celsius + 273.15)
    print("Celsius to Kelvins is: ", kelvins)
    return kelvins
pass
def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    
    fahrenheit = float((celsius * 9/5) + 32)

    print("Celsius to Fahrenheit is: ", fahrenheit)
    return fahrenheit
pass
def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    
    kelvins = float((fahrenheit - 32) * 5/9 + 273.15)
    print("Fahrenheit to Kelvins is: ", kelvins)
    return kelvins
pass

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    
    celsius = float((fahrenheit - 32) * 5/9)
    print("Fahrenheit to Celsius is: ", celsius)
    return celsius
pass


def convertKelvinToFahrenheit(kelvins):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    
    fahrenheit = float((kelvins - 273.15) * 9/5 + 32)
    print("Kelvin to Fahrenheit is: ", fahrenheit)
    return fahrenheit
pass

def convertKelvinToCelsius(kelvins):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    
    celsius = float(kelvins - 273.15)
    print("Kelvin to Celcius is: ", celsius)
    return celsius
pass




