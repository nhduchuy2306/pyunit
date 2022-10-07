import unittest
from unittest.mock import Mock
from app.item_database import *
from app.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_can_add_item_to_cart(self):
        cart = ShoppingCart(5)
        cart.add("apple")
        assert cart.size() == 1

    def test_when_item_added_then_cart_contains_item(self):
        cart = ShoppingCart(5)
        cart.add("apple")
        self.assertIn("apple",cart.get_all_items())
        # self.assertIn("orange",cart.get_all_items())

    def test_when_add_more_than_max_items_should_fail(self):
        cart = ShoppingCart(5)
        for i in range(5):
            cart.add("apple")
        self.assertRaises(OverflowError,cart.add,"apple")
        
    def test_when_remove_item_success(self):
        cart = ShoppingCart(5)
        cart.add("apple")
        cart.add("orange")
        cart.add("strawberry")
        cart.add("blueberry")
        cart.add("coconut")
        cart.remove_item("coconut")
        self.assertNotIn("coconut", cart.get_all_items())
        
    def test_when_search_item_return_true(self):
        cart = ShoppingCart(5)
        cart.add("apple")
        cart.add("orange")
        cart.add("strawberry")
        cart.add("blueberry")
        cart.add("coconut")
        
        self.assertTrue(cart.search_item("coconut"))
        
    def test_get_total_price(self):
        cart = ShoppingCart(5)
        cart.add("apple")
        cart.add("orange")
        cart.add("strawberry")

        itemDatabase = ItemDatabase()
        def mock_get_item(item:str):
            if item=="apple":
                return 1.0
            if item=="orange":
                return 2.0
            if item=="strawberry":
                return 3.0
            
        itemDatabase.get_price = Mock(side_effect=mock_get_item)
        
        self.assertEqual(cart.get_total_price(itemDatabase),6)

if __name__ =='__main__':
    unittest.main(verbosity=2)