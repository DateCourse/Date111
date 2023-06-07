import os
class TCard:
    def __init__(self, value):
        self.value = value % 13 + 1  # 카드 넘버
        self.shape = value // 13  # 카드 모양

    def getValue(self):
        return self.value

    def getX(self):
        return self.x

    def getsuit(self):
        if self.x == 0:
            self.suit = "Spades"
        elif self.x == 1:
            self.suit = "Diamonds"
        elif self.x == 2:
            self.suit = "Hearts"
        else:
            self.suit = "Clubs"
        return self.suit

    def filename(self):
        return os.path.join('C:/Users/user/PycharmProjects/pythonProject1/cards', self.getsuit() + str(self.value) + ".png")