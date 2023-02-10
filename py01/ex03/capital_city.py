import sys

def main():
    arg = check_argv()
    states, capital_cities = my_dict();
    if arg == 1:
        return (1);
    if arg in states:
        print(capital_cities[states[arg]]);
    else:
        print("Unknown state");

def check_argv():
    if len(sys.argv) != 2:
        return (1);
    return (sys.argv[1]);

def my_dict():
    states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
    capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}
    return(states, capital_cities);

if __name__ == '__main__':
    main();