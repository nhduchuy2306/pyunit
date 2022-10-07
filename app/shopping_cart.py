from typing import List

class ShoppingCart:
    def __init__(self, max_size:int):
        self.items : List  = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more items")
        self.items.append(item)
    
    def size(self) -> int:
        return len(self.items)
    
    def get_all_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get_price(item)
        return total_price
    
    def remove_item(self, item:str):
        for goods in self.items:
            if goods == item:
                self.items.remove(goods)
                break
    
    def search_item(self, item:str) -> bool:
        for goods in self.items:
            if goods == item:
                return True
        return False
    
def main():
    price_map = {
        "orange": 10000,
        "apple": 20000,
        "strawberry": 25000,
    }
    
    shop = ShoppingCart(5)
    shop.add("orange")
    shop.add("apple")
    shop.add("strawberry")
    shop.add("orange")
    shop.add("apple")
    # shop.add("strawberry")
    
    # print(shop.size())
    # print(shop.get_all_items())
    # print("--------------------------")
    # shop.remove_item("orange")
    # print(shop.size())
    # print(shop.get_all_items())

if __name__ == "__main__":
    main()