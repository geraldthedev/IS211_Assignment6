import conversions
import conversions_refactored
import unittest

class TestKel(unittest.TestCase):
    cel =(300, 225, 37, 50, 127)
    far =(300, 225, 37, 50, 127)
    kel =(300, 225, 37, 50, 127)


    def test_cel_temp(self):
        for celsius in self.cel:
            cel_kelTemp = conversions.convertCelsiusToKelvin(celsius)
            cel_farTemp = conversions.convertCelsiusToFahrenheit(celsius)
    
    def test_far_temp(self):
        for fahrenheit in self.far:
            far_celTemp = conversions.convertFahrenheitToCelsius(fahrenheit)
            far_kelTemp = conversions.convertFahrenheitToKelvin(fahrenheit)
    
    def test_kel_temp(self):
        for kelvins in self.kel:
            kel_celTemp = conversions.convertKelvinToCelsius(kelvins)
            kel_kelTemp = conversions.convertKelvinToFahrenheit(kelvins)
            
class TestMile(unittest.TestCase):
    fromUnit= (25,48,100,65,85)
    toUnit = [1760, 1609.34]
    value = fromUnit

    def test_mile_conv(self):
        for fromUnit, toUnit, value in self.fromUnit, self.toUnit, self.value:
            mile_conv = conversions_refactored.convert(fromUnit, toUnit, value)
pass        



if __name__ == '__main__':
    unittest.main()