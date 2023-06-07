from Dice import *

class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Upper Scores",
               "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    def getConfigs(self):
        return Configuration.configs

    def score(self, row, d):
        if 0 <= row < 6:
            return self.scoreUpper(d, row+1)
        elif row == 8:
            return self.scoreThreeOfAKind(d)
        elif row == 9:
            return self.scoreFourOfAKind(d)
        elif row == 10:
            return self.scoreFullHouse(d)
        elif row == 11:
            return self.scoreSmallStraight(d)
        elif row == 12:
            return self.scoreLargeStraight(d)
        elif row == 13:
            return self.scoreYahtzee(d)
        elif row == 14:
            return self.sumDie(d)
        else:
            return -1

    def scoreUpper(self, d, num):
        total_sum = 0
        for i in range(5):
            if d[i].getRoll() == num:
                total_sum += num
        return total_sum

    def scoreThreeOfAKind(self, d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 3:
                return self.sumDie(d)
        return 0

    def scoreFourOfAKind(self, d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 4:
                return self.sumDie(d)
        return 0

    def scoreFullHouse(self, d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in tmp:
            if i == 3:
                for j in tmp:
                    if j == 2:
                        return 25
        return 0

    def scoreSmallStraight(self, d):
        tmp = [0 for _ in range(7)]
        for i in range(5):
            tmp[d[i].getRoll()] += 1
        for i in range(3):
            if tmp[i+1] >= 1 and tmp[i+2] >= 1 and tmp[i+3] >= 1 and tmp[i+4] >= 1:
                return 30
        return 0
