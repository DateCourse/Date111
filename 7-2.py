class Stock:
    def __init__(self,name,symbol,previousPrice,currentPrice):
        self.__name = name #Stock __name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__Symbol
    def getpreviousPrice(self):
        return self.__previousPrice
    def setPreviousPrice(self,value):
        self.__PreviousPrice = value
    def getCurrentPrice(self):
        return self.__currentPrice
    def setCurrentPrice(self,value):
        self.__setCurrentPrice = value
    def getChangePercent(self):
        return "{0:.2f}%".format(\
        100 *(self.__currentPrice - self.__previousPrice) / self.__previousPrice)
stock = Stock("intel","INTC",20500,20350)
print("가격 변화율 %: ", stock.getChangePercent())



