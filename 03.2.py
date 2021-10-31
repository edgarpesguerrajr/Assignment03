#Enter the number of apples 
def apples():
    ApplesFunc = int(input ("Enter the quantity of apples that you want to buy: "))
    return ApplesFunc

#Enter the number of apples 
def oranges():
    OrangesFunc = int(input ("Enter the quantity of oranges that you want to buy: "))
    return OrangesFunc

#Number of apples multiplied by its price
def PriceOfApple():
    PriceApplesFunc = NoApples * 20
    return PriceApplesFunc

#Number of oranges multiplied by its price
def PriceOfOrange():
    PriceOrangesFunc = NoOranges * 25
    return PriceOrangesFunc

#Adding the total price of the apples and oranges
def Final(ApplePriceF, OrangesPriceF):
    print(f'The total amount is {ApplePriceF + OrangesPriceF}.')

NoApples = apples()
NoOranges = oranges()
ApplesPrice = PriceOfApple()
OrangesPrice = PriceOfOrange()
Final (ApplesPrice, OrangesPrice)

#Sir may note po ako dun sa 03.3 hehe