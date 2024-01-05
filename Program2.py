#行李箱
class Luggage:
    def __init__(self, ID, Weight, DepartureAirport, Destination, PassengerName):
        self.ID = ID                                    # ID
        self.Weight = Weight                            # 重量
        self.DepartureAirport = DepartureAirport        # 出發機場
        self.Destination = Destination                  # 目的地
        self.PassengerName = PassengerName              # 旅客名字

    #查詢
    def Check(self):
        print(f"行李ID: {self.ID} 重量: {self.Weight} kg 出發機場: {self.DepartureAirport} 目的地: {self.Destination} 旅客名字: {self.PassengerName}")       

    #修改各個資訊。
    def Revise(self, new_ID):
        self.ID = new_ID     
        print(f"行李ID {self.ID} 行李ID: {self.ID} 的資訊已修改。")

    def Revise(self, new_weight ):
        self.Weight = new_weight        
        print(f"行李ID {self.ID} 重量: {self.Weight} kg 的資訊已修改。")

    def Revise(self, new_DepartureAirport):
        self.DepartureAirport = new_DepartureAirport     
        print(f"行李ID {self.ID} 出發機場: {self.DepartureAirport} 的資訊已修改。")
    
    def Revise(self, new_Destination):
        self.Destination = new_Destination     
        print(f"行李ID {self.ID} 目的地: {self.Destination} 的資訊已修改。")
    
    def Revise(self, new_PassengerName):
        self.PassengerName = new_PassengerName     
        print(f"行李ID {self.ID} 旅客名字: {self.PassengerName} 的資訊已修改。")  
        

# 登記證
class BoardingPass:
    def __init__(self, passenger_name, boarding_pass_number, boarding_time, gate_number, seat_location, luggage_count, luggage_ID):
        self.passenger_name = passenger_name                # 旅客名字
        self.boarding_pass_number = boarding_pass_number    # 登機證編號
        self.boarding_time = boarding_time                  # 登機時間
        self.gate_number = gate_number                      # 登機門編號
        self.seat_location = seat_location                  # 座位位置 A~E
        self.luggage_count = luggage_count                  # 行李件數
        self.luggage_ID = luggage_ID                        # 行李ID

    def CheckPass(self):
        print(f"登記證旅客名字: {self.passenger_name} 登機證編號: {self.boarding_pass_number} 登機時間: {self.boarding_time} 登機門編號: {self.gate_number} 座位位置 A~E: {self.seat_location} 行李件數: {self.luggage_count} 行李ID: {self.luggage_ID}")
    
    #修改各個資訊。
    def BoardingPass_Revise(self, new_passenger_name):
        self.passenger_name = new_passenger_name     
        print(f"旅客名字: {self.passenger_name} 旅客名字: {self.passenger_name} 的資訊已修改。")

    def BoardingPass_Revise(self, new_boarding_pass_number):
        self.boarding_pass_number = new_boarding_pass_number     
        print(f"旅客名字: {self.passenger_name} 登機證編號: {self.boarding_pass_number} 的資訊已修改。")

    def BoardingPass_Revise(self, new_boarding_time):
        self.boarding_time = new_boarding_time     
        print(f"旅客名字: {self.passenger_name} 登機時間: {self.boarding_time} 的資訊已修改。")

    def BoardingPass_Revise(self, new_gate_number):
        self.gate_number = new_gate_number     
        print(f"旅客名字: {self.passenger_name} 登機門編號: {self.gate_number} 的資訊已修改。")
    
    def BoardingPass_Revise(self, new_seat_location):
        self.seat_location = new_seat_location     
        print(f"旅客名字: {self.passenger_name} 座位位置 A~E: {self.seat_location} 的資訊已修改。")

    def BoardingPass_Revise(self, new_luggage_count):
        self.luggage_count = new_luggage_count     
        print(f"旅客名字: {self.passenger_name} 行李件數: {self.luggage_count} 的資訊已修改。")
    
    def BoardingPass_Revise(self, new_luggage_ID):
        self.luggage_ID = new_luggage_ID     
        print(f"旅客名字: {self.passenger_name} 行李ID: {self.luggage_ID} 的資訊已修改。")

# 創建三個行李物件
luggage1 = Luggage("A01", 35, "Tainan", "Kaohsiung", "John")
luggage2 = Luggage("A02", 20, "Kaohsiung", "Taipei", "Ken")
luggage3 = Luggage("A03", 10, "Chiayi", "Taichung", "Charlie")

luggage1.Check()
luggage2.Check()
luggage3.Check()
print("\n")

#修改

luggage3.Revise("Brian") 
print("已更新。")
luggage3.Check()
print("\n")

# 登記證
BoardingPass1 = BoardingPass("John", "4a9g", "11:30", "123", "A", 1, "A01")
BoardingPass2 = BoardingPass("Ken", "4b9a", "04:00", "755", "D", 2, "A02")
BoardingPass3 = BoardingPass("Charlie", "6d8d", "05:00", "867", "E", 1, "A03")

BoardingPass1.CheckPass()
BoardingPass2.CheckPass()
BoardingPass3.CheckPass()
print("\n")

