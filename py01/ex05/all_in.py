import sys

def main():
    arg = check_argv();
    if arg == 1:
        return (1);
    states, capital_cities = my_dict_s(), my_dict_c();
    verify_param(states, capital_cities, arg);

def verify_param(states, capital_cities, arg):
    arg = arg.split(",");
    i = 0;

    while i < len(arg):
        arg[i] = arg[i].strip();
        if arg[i] == '':
            arg.pop(i);
            i -= 1;
        else:
            if is_state(states, capital_cities, " ".join(arg[i].title().split())) != 0:
                if is_capital_cities(states, capital_cities, " ".join(arg[i].title().split())) != 0:
                    print(arg[i], "is neither a capital city nor a state");
        i += 1;

def is_state(states, capital_cities, arg):
    if arg in states:
        print(capital_cities[states[arg]], "is the capital of", arg);
        return (0);
    return (1);

def is_capital_cities(states, capital_cities, arg):
    states, capital_cities = switch_key_value(states, capital_cities);
    if arg in capital_cities:
        print(arg , "is the capital of", states[capital_cities[arg]]);
        return (0);
    return (1);

def switch_key_value(dictionary1, dictionary2):
    return ({value: key for key, value in dictionary1.items()}, {value: key for key, value in dictionary2.items()});


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