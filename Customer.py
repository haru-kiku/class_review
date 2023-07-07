class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
    def entry_fee(self):
        if self.is_child():
            return 1000
        if self.is_adult():
            return 1500
        if self.is_sinia():
            return 1200
    
    def is_child(self):
        return 0 <= self.age < 20
    
    def is_adult(self):
        return 20 <= self.age < 65
    
    def is_sinia(self):
        return 65 <= self.age
    
    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"
    


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.full_name())  # "Ken Tanaka"という値を返す
print(ken.age)  # 15 という値を返す
print(ken.entry_fee())  # 1000 という値を返す
print(ken.info_csv())  #  "ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.full_name())  # "Tom Ford" という値を返す
print(tom.age)  # 57 という値を返す
print(tom.entry_fee())  # 1500 という値を返す
print(tom.info_csv())  # "Tom"

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age)  # 73 という値を返す
print(ieyasu.entry_fee())  # 1200 という値を返す
print(ieyasu.info_csv())
