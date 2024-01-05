#建立類別CarOrder，用於表示汽車訂單。
class CarOrder:
    #初始化了汽車名稱 (CarName)、價錢 (Price)、數量 (Quantity) 這三個屬性。
    def __init__(self, CarName, Price, Quantity):
        self.CarName = CarName
        self.Price = Price
        self.Quantity = Quantity
 
    #副函式。汽車價錢 = 價錢 * 數量
    #self 取得 Price 與 Quantity 屬性，並做乘法回傳CarPrice。
    def CarPrice(self):
        return self.Price * self.Quantity
    
     # 取得汽車名稱的副函式
    def getCarName(self):        
        return self.CarName
    
    # 取得汽車數量的副函式
    def getCarQuantity(self):        
        return self.Quantity

#建立物件
Car1 = CarOrder("Benz" , 100 , 1)
Car2 = CarOrder("Toyota" , 50 , 3)
Car3 = CarOrder("Honda" , 60 , 5)

#印出車輛的名稱
print(f"Car1車輛的名稱 : {Car1.CarName}")
print(f"Car2車輛的名稱 : {Car2.CarName}")
print(f"Car3車輛的名稱 : {Car3.CarName}\n")

#印出車輛訂單的價錢
print(f"Car1車輛的金額 : {Car1.CarPrice()} 元")
print(f"Car2車輛的金額 : {Car2.CarPrice()} 元")
print(f"Car3車輛的金額 : {Car3.CarPrice()} 元\n")

#印出車輛訂單的數量
print(f"Car1車輛的數量 : {Car1.getCarQuantity()} 輛")
print(f"Car2車輛的數量 : {Car2.getCarQuantity()} 輛")
print(f"Car3車輛的數量 : {Car3.getCarQuantity()} 輛\n")