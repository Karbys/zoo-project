import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price_C1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50) # Fault fixed
    def test_child_ticket_price_C1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100) # Fault fixed
    def test_child_ticket_price_C1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "undefined") # Fault fixed
    def test_child_ticket_price_C1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150) # Fault fixed
    def test_child_ticket_price_C1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()