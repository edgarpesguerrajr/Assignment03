#Asking for the available money
def TotalMoney():
    MoneyMoney = int(input('ENTER YOUR AVAILABLE MONEY: '))
    return MoneyMoney

#Asking for the desired price of the apple
def DesiredPriceOfApple():
    PricePrice = int(input('ENTER YOUR DESIRED PRICE OF AN APPLE: '))
    return PricePrice

#Dividing the desired price of the apple to the available money
def ComputationOfTotalApple():
    TotalTotal = (Money // Price)
    return TotalTotal

#Multiplying the desired price of the apple to the total apples that can be bought
def ComputationOfTotalAmount():
    AmountAmount = (Price * Total)
    return AmountAmount

#Subtracting the available money to the total amount of the apples
def ComputationOfChange():
    ChangeChange = (Money - Amount)
    return ChangeChange

def Final(TotalF, ChangeF):
    print (f'You can buy {TotalF} apples and your change is {ChangeF} pesos.')

Money = TotalMoney()
Price = DesiredPriceOfApple()
Total = ComputationOfTotalApple()
Amount = ComputationOfTotalAmount()
Change = ComputationOfChange()
Final (Total, Change)

#Ang galing niyo po magturo sir, sobrang warm po ng atmosphere pag nagtuturo po kayo.
#Hindi rin po nakakahiyang magtanong, dahil naeexplain niyo po ng maayos at malinaw yung sagot.