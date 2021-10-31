def Name():
    NameFunc = input ('Name: ')
    return NameFunc

def Age():
    AgeFunc = input ('Age: ')
    return AgeFunc

def Address():
    AddressFunc = input ('Address: ')
    return AddressFunc

def Final(PangalanF, EdadF, LugarF):
    print(f'Hi, my name is {PangalanF}. I am {EdadF} years old and I live in {LugarF}.')

Pangalan = Name()
Edad = Age()
Lugar = Address()
Final(Pangalan, Edad, Lugar)