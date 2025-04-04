class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    def set_celsius(self, value):
        if value < -273.15:
            print("Temperature cannot be below absolute zero!")
        else:
            self.__celsius = value

    def get_celsius(self):
        return self.__celsius


tem = Temperature(25)
print(tem.to_fahrenheit())  
tem.set_celsius(-300)       
print(tem.get_celsius())   
tem.set_celsius(30)