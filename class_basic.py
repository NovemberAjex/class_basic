class vehicle1():
    def __init__(self,name,make,model,passenger_capacity):
        self.name=name
        self.make=make
        self.model=model
        self.passenger_capacity = passenger_capacity
    def vehicle_detail(self):
        print(f"""\t\tThe name of this vehicel is {self.name} and the make of this car is {self.make} and the model is {self.model} 
        and the passenger capacity is {self.passenger_capacity}""")
class vehicle2():
    def __init__(self,name,make,engine_capacity,horsepower):
        self.name=name
        self.make=make
        self.engine_capacity  =engine_capacity
        self.horsepower = horsepower
    def vehicle_detail(self):
        print(f"The name of the car is {self.name} and the make of this car {self.make} and the engine capacity is {self.engine_capacity} and the horsepower is {self.horsepower}")

car_1 = vehicle1("cultus","Suzuki","2022",5)
car_1.vehicle_detail()
car_2 =  vehicle2("Corolla","Toyota",1350,93)
car_2.vehicle_detail()
