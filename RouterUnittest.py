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
        self.assertFalse(r1.get_interface("g0/0") == {})     # found interface
        self.assertTrue(r1.get_interface("g0/1") == {})      # not found interface  

    def test_04_showInterfaces(self):
        self.assertTrue(r1.show_interfaces())
        self.assertTrue(r1.show_interfaces("g0/0"))
        self.assertFalse(r1.show_interfaces("fake0/0"))

if __name__ == "__main__":
    unittest.main()
