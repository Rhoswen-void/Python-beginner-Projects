class Car:
    def __init__(self, model, year, for_sale, color):
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.color = color

    def drive(self):
        print(f"You are driving your {self.color} {self.model}")

    def stop(self):
        print(f"Your {self.color} {self.model} stopped")

    def sale(self):
        if self.for_sale:
            print(f"Yes the {self.color} {self.model} is for sale.")
        else:
            print(f"Yes the {self.color} {self.model} is not for sale.")
            