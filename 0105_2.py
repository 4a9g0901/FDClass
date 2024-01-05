#行李箱
class Luggage:
    def __init__(self, ID, Weight, DepartureAirport, Destination, PassengerName):
        self.ID = ID                                    # ID
        self.Weight = Weight                            # 重量
        self.DepartureAirport = DepartureAirport        # 出發機場
        self.Destination = Destination                  # 目的地
        self.PassengerName = PassengerName              # 旅客名字

    def Check(self):
        print(f"行李ID: {self.ID} 重量: {self.Weight} kg 出發機場: {self.DepartureAirport} 目的地: {self.Destination} 旅客名字: {self.PassengerName}")       

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
            

# 創建三個行李物件
luggage1 = Luggage("A01", 35, "Tainan", "Kaohsiung", "John")
luggage2 = Luggage("A02", 20, "Kaohsiung", "Taipei", "Ken")
luggage3 = Luggage("A03", 10, "Chiayi", "Taichung", "Charlie")

luggage1.Check()
luggage2.Check()
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









