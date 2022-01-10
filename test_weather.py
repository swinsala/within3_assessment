# Unit testing script for within3.py 
# Owner: Oluwaseun Winsala

# import the application file

import within3 
import unittest

within3.weather.zip_code = 32901

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather_ = within3.weather()
    
    def test_zip_code(self):
        actual = self.within3.weather.get('/')
        expected = "http://localhost:5000/?zip_code=32901"
        #expected = "https://api.openweathermap.org/data/2.5/weather?zip_code=32901&APPID=6f8628fda32712e5b77d10cd5672d8e4"
        self.assertEqual(actual, expected)        
    
'''    
if __name__ == "__main__":
    unittest.main()
'''