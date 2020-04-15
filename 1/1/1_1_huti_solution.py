 1from abc import *

class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list): #주문 메뉴 리스트
        pass
    
    @abstractmethod
    def get_total_price(self): #음식 가격 총합 리턴
        pass
    
class Food:
    def __init__(self, name, price):
        self.name = name   #음식 이름
        self.price = price    #음식 가격
        
class PizzaStore(DeliveryStore):        #피자 배달 전문점
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]    #피자 메뉴
        menu_prices = [11100, 12600, 13300, 21000, 19500];  #피자 가격
        self.menu_list = [] #주문할 수 있는 음식명 리스트
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))
        
        self.order_list = []        #주문 받은 음식명 리스트
    
    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)

    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price 
            
def solution(order_list):
    delivery_store = PizzaStore()
    
    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price

#The following is code to output testcase.
order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")