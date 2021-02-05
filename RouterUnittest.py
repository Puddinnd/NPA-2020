from RouterClass import Router
import unittest

hostname = "temp hostname"
brand = "temp brand"
model = "temp model"
r1 = Router(hostname, brand, model)

class TestRouter(unittest.TestCase):
        
    def test_01_basicMethods(self):
        newHostname = "R1"
        newBrand = "Cisco"
        newModel = "Catalyst 8300-1N1S-4T2X"
        r1.setHostname(newHostname)
        r1.setBrand(newBrand)
        r1.setModel(newModel)       
        self.assertTrue(r1.getHostname() == newHostname)
        self.assertTrue(r1.getBrand() == newBrand)
        self.assertTrue(r1.getModel() == newModel)

    def test_02_addInterface(self):
        intname = "g0/0"
        self.assertTrue(r1.add_interface(intname))     # add new interface
        self.assertFalse(r1.add_interface(intname))    # interface already exists

    def test_03_getInterface(self):
        intname1 = "g0/0"
        intname2 = "g0/1"
        self.assertFalse(r1.get_interface(intname1) == {})     # found interface
        self.assertTrue(r1.get_interface(intname2) == {})      # not found interface  

if __name__ == "__main__":
    unittest.main()
