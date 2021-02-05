from RouterClass import Router
import unittest

hostname = "temp hostname"
brand = "temp brand"
model = "temp model"
r1 = Router(hostname, brand, model)

class TestRouter(unittest.TestCase):
        
    def test_basicMethods(self):
        newHostname = "R1"
        newBrand = "Cisco"
        newModel = "Catalyst 8300-1N1S-4T2X"
        r1.setHostname(newHostname)
        r1.setBrand(newBrand)
        r1.setModel(newModel)
        self.assertTrue(r1.getHostname() == newHostname)
        self.assertTrue(r1.getBrand() == newBrand)
        self.assertTrue(r1.getModel() == newModel)


if __name__ == "__main__":
    unittest.main()
