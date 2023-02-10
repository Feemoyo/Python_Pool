import sys, os, re

def main():
    d = {};
    new_file = "";
    dot_template, file_name = check_argv();
    if dot_template == 1:
        return (1);
    file_html = open(file_name + ".html", "w");
    with open("settings.py") as file:
        lines = file.readlines();
        for line1 in lines:
            key, value = line1.split("=");
            d[key.strip()] = value.strip();

    with open(dot_template) as template:
        tem_line = template.readlines();
        new_file = ""
        for i in tem_line:
            new_file += i;
        file_html.write(new_file.format(**d));
    file_html.close();

def check_argv():
    if len(sys.argv) != 2:
        print("Wrong number of params");
        return (1, 1);
    file_name, file_extension = os.path.splitext(sys.argv[1])
    if file_extension != ".template":
        print("Wrong parameter");
        return (1, 1);
    if os.path.exists(sys.argv[1]) == False or os.path.exists("settings.py") == False:
        print("A non-existing file");
        return (1, 1);
    return (sys.argv[1], file_name);

if __name__ == '__main__':
    main();