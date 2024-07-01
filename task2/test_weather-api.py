import unittest
import requests

class WeatherTest(unittest.TestCase):
    BASE_URL = "http://api.weatherapi.com/v1"
    API_KEY = "9ee886e34f6049ddb83160751240107"

    def test_valid_city(self):
        city = "London"
        response = requests.get(f"{self.BASE_URL}/current.json?q={city}&key={self.API_KEY}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("location", data)
        self.assertIn("current", data)
        self.assertEqual(data["location"]["name"], city)
        self.assertIn("temp_c", data["current"])
        self.assertIn("temp_f", data["current"])
        self.assertIn("humidity", data["current"])
        self.assertIn("wind_mph", data["current"])
        self.assertIn("wind_kph", data["current"])

    def test_invalid_city(self):
        city = "Invalid"
        response = requests.get(f"{self.BASE_URL}/current.json?q={city}&key={self.API_KEY}")
        self.assertIn(response.status_code, [400, 404])
        data = response.json()
        self.assertIn("error", data)
        self.assertIn("message", data["error"])

    def test_empty_city(self):
        city = ""
        response = requests.get(f"{self.BASE_URL}/current.json?q={city}&key={self.API_KEY}")
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)
        self.assertIn("message", data["error"])

    def test_edge_city(self):
        city = "Springfield"
        response = requests.get(f"{self.BASE_URL}/current.json?q={city}&key={self.API_KEY}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("location", data)
        self.assertIn("current", data)
        self.assertEqual(data["location"]["name"], city)
        self.assertIn("temp_c", data["current"])
        self.assertIn("temp_f", data["current"])
        self.assertIn("humidity", data["current"])
        self.assertIn("wind_mph", data["current"])
        self.assertIn("wind_kph", data["current"])

if __name__ == '__main__':
    unittest.main()
