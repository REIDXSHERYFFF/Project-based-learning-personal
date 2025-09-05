class pizza:
    def __init__(self, size, crust, toppings=None):
        self.size = size
        self.crust = crust
        self.toppings = toppings if toppings else []

    def add_topping(self, topping):
        self.toppings.append(topping)
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping} isn't on your topping used on your pizza")    


    def describe_pizza(self):
        print(f'size: {self.size.title()}')
        print(f'crust: {self.crust.title()}')
        if self.toppings:
            print(f'topping: ')
            for topping in self.toppings:
                print(f" - {topping.title()}")
        else:
            print('no toppings added yet')    

my_pizza = pizza("large", "thin")
my_pizza.add_topping ('pepperonie')
my_pizza.add_topping('mushrooms')
my_pizza.add_topping('onions')

my_pizza.describe_pizza()