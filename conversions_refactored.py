import conversions
import test

miles = 0
yards = 1760
meters = 1609.34
fromUnit = miles
toUnit = [yards, meters]
value = fromUnit

def convert(fromUnit, toUnit, value):
    fromUnit = miles
    toUnit = [yards, meters]
    value = fromUnit

    for unit in toUnit:
        new_value = value * unit
        print(new_value)
    return new_value
pass

