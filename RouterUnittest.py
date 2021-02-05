from RouterClass import Router
import unittest

class TestRouter(unittest.TestCase):

    def test_createObject(self):
        hostname = "R1"
        brand = "Cisco"
        model = "Catalyst 8300-1N1S-4T2X"
        r1 = Router(hostname, brand, model)
        self.assertTrue(r1.getHostname() == hostname)
        self.assertTrue(r1.getBrand() == brand)
        self.assertTrue(r1.getModel() == model)


if __name__ == "__main__":
    unittest.main()
