def main():
    txt = open("numbers.txt",'r');
    txt = str(txt.read());
    txt = txt.split(",")
    for x in range(len(txt)):
        print(txt[x])   

if __name__ == '__main__':
    main();