import random
def main():
    words = ['write','program','that','teacher','student','korea','hangman']
    while True:
        index = random.randint(0,len(words)-1)
        hiddenWord = words[index] #숨긴 단어 랜덤하게 생성
        guessWord = ['*']*len(hiddenWord)
        NofCorrectChar = 0
        NofMiss = 0
        while NofCorrectChar < len(hiddenWord):
            ch = input('(추측) 단어 '+ toString(guessWord)+'에 포함되는 문자를 입력>')
            if ch in guessWord:
                print('\t',ch,'은/는 이미 포함되어 있습니다.')
            elif hiddenWord.find(ch) == -1:
                print('\t',ch,'은/는 포함되어 있지 않습니다.')
                NofMiss += 1
            else:
                k = hiddenWord.find(ch)
                while k >= 0:
                    guessWord[k] = ch
                    NofCorrectChar += 1
                    k = hiddenWord.find(ch,k+1)
        print('정답은 ',hiddenWord,'입니다.',NofMiss,'번 실패했습니다.')
        YesNo = input('다른 단어 맞추기를 하시겠습니까? Y/N >')
        if YesNo == 'n':
            break
def toString(guessWord):
    result=''
    for c in guessWord:
        result += c
        return result

main()