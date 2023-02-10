import sys

def main():
    arg = check_argv()
    capital_cities, states = switch_key_value(my_dict_c()), switch_key_value(my_dict_s());
    if arg == 1:
        return (1);
    if arg in capital_cities:
        print(states[capital_cities[arg]]);
    else:
        print("Unknown state");

def switch_key_value(dictionary):
    return ({value: key for key, value in dictionary.items()})

def check_argv():
    if len(sys.argv) != 2:
        return (1);
    return (sys.argv[1]);

def my_dict_s():
    states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
    return(states);

def my_dict_c():
    capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}
    return(capital_cities);

if __name__ == '__main__':
    main();