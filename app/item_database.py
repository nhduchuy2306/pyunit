import requests
import json

class ItemDatabase:
    def __init__(self):
        pass
    
    # def get_price(self,item:str)->float:
    #     BASE_URL = 'https://www.ec.europa.eu/agrifood'
    #     res = requests.get(BASE_URL+f'/api/fruitAndVegetable/prices?memberStateCodes=PT,SI&products={item}&months=1,2,3&beginDate=12/02/2018&endDate=23/03/2020')
    #     return res
    
    def get_price(self,item:str)->float:
        pass
    
if __name__ == '__main__':
    itemDatabase = ItemDatabase()
    json_data = itemDatabase.get_price("oranges")

    print(float(itemDatabase.get_price("oranges").json()[0]['price'][1:]))