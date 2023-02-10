class   HotBeverages:
    def __init__(self, name = "hot beverage", price = 0.30):
        self.name = name;
        self.price = price;
    def description(self):
        return ("Just some hot water in a cup.");
    def __str__(self):
        return(f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}");

class   Coffee(HotBeverages):
    def __init__(self):
        super().__init__("coffee", 0.40);
    def description(self):
        return ("A coffee, to stay awake.");

class   Tea(HotBeverages):
    def __init__(self):
        super().__init__("tea", 0.30);
    def description(self):
        return ("Just some hot water in a cup.");

class   Chocolate(HotBeverages):
    def __init__(self):
        super().__init__("chocolate", 0.50);
    def description(self):
        return ("Chocolate, sweet chocolate...");

class   Cappuccino(HotBeverages):
    def __init__(self):
        super().__init__("cappuccino", 0.45);
    def description(self):
        return ("Un po’ di Italia nella sua tazza!");

def my_FT():
    c1 = HotBeverages();
    print(c1);
    c2 = Coffee()
    print(c2);
    c3 = Tea();
    print(c3);
    c4 = Chocolate();
    print(c4);
    c5 = Cappuccino();
    print(c5);

if __name__ == "__main__":
    my_FT();