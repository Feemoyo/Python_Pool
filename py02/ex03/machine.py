import  random
import  beverages
class   CoffeeMachine:
    def __init__(self, index = 0, broken = False):
        self.index = index;
        self.broken = broken;


    class   EmptyCup(beverages.HotBeverages):
        def __init__(self):
            super().__init__("empty cup", 0.90);
        def description(self):
            return ("An empty cup?! Gimme my money back!");

    class   BrokenMachineException(Exception):
        def __init__(self):
            super().__init__(self);
            self.broken = True;
            raise   Exception ("This coffee machine has to be repaired.");

    def repair(self):
        if self.broken == True:
            self.broken = False;
            self.index = 0

    def serve(self, derived):
        if self.index < 10:
            self.index += 1;
            return(random.choice([derived(), self.EmptyCup()]));
        else:
            self.broken = True;
            raise self.BrokenMachineException();


def company():
    machine = CoffeeMachine();
    drinks = (beverages.HotBeverages, beverages.Coffee, beverages.Tea, beverages.Chocolate, beverages.Cappuccino);
    i = 0;
    while i != 100:
        try:
            print(machine.serve(random.choice(drinks)))
        except Exception as error:
            print("=======================================");
            print(error);
            print("=======================================");
            machine.repair();
        i += 1;

if __name__ == "__main__":
    company();