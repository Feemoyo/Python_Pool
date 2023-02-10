def main():
    d = exchange_dict(list_tuples());
    for key, value in sorted(d.items()):
        print(key, ":", value);

def exchange_dict(list_tuples):
    d = dict(list_tuples);
    new_d = {};
    for name, year in d.items():
        if year in new_d:
            new_d[year] = new_d[year] + " " + name
        else:
            new_d[year] = name;
    return (new_d);

def list_tuples():
    d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]
    return (d);

if __name__ == '__main__':
    main();