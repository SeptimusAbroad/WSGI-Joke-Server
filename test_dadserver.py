import unittest
import requests
import dadserver


class DadjokeTests(unittest.TestCase):
    def test_external_api(self):
        """This test should tell us if the icanhazdadjoke API is up and running by checking to
        see if the get request from server returns a 200 code."""
        dadjoke_server_response = requests.get("https://icanhazdadjoke.com")
        self.assertTrue(dadjoke_server_response.ok)

    def test_local_server(self):
        """This test should check if a get request returns a 200 code from our local server."""
        local_server_response = requests.get("http://localhost:8080")
        self.assertTrue(local_server_response.ok)

    def test_dadjoke3000_data_type(self):
        """This test checks to see if the data type that the dadjoke function returns is being converted to a
        bytestring"""
        dadjoke3000_response = dadserver.dadjoke3000()
        self.assertEqual(type(dadjoke3000_response[0]), bytes)


if __name__ == "__main__":
    unittest.main()
