
def main():
    a,b,c,d,e,f,g,h,i = 42, '42', "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set();
    print(a , "has a type", type(a));
    print(b, "has a type", type(b));
    print(c, "has a type", type(c));
    print(d, "has a type", type(d));
    print(e, "has a type", type(e));
    print(f, "has a type", type(f));
    print(g, "has a type", type(g));
    print(h, "has a type", type(h));
    print(i, "has a type", type(i));

if __name__ == '__main__':
    main()