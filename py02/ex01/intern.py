class   Intern:
    def __init__(self, name = None):
        if name == None:
            name = "My name? I’m nobody, an intern, I have no name.";
        self.name = name;
    def __str__(self):
        return(f"{self.name}");
    class   Coffe:
        def __str__(self):
            return(f"This is the worst coffee you ever tasted.");
    def work(self):
        raise   Exception("I’m just an intern, I can’t do that...");
    def make_coffe(self):
        return(self.Coffe());

def my_FT():
    c1 = Intern();
    c2 = Intern("Mark");
    print(c2);
    print(c2.make_coffe());
    print(c1);
    print(c1.work());

if __name__ == "__main__":
    my_FT();