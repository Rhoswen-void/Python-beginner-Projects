

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): #instance method
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Business Analyst", "Vice President", "Project Manager", "Senior Developer"]
        return position in valid_positions # returns a True or False value

# Make sure this line has ZERO indentation (all the way to the left border)
print(Employee.is_valid_position("Cook"))