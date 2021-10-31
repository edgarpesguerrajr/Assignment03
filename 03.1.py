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
    print(f'Ako si {PangalanF} na {EdadF} taong gulang at nakatira sa {LugarF}')

Pangalan = Name()
Edad = Age()
Lugar = Address()
Final(Pangalan, Edad, Lugar)