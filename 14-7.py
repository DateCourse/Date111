from tkinter import *
import tkinter.messagebox #에러메시지 출력하는 모듈
from tkinter.filedialog import askopenfilename #파일오픈 대화상자
def openFile():
    fn=askopenfilename()
    filename.set(fn)

def showResult2():
    fn = filename.get()
    try:
        infile = open(fn, "r")
        counts = [0] * 26  # [0,0,...]
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha():  # a,b,c,d,...,z,97,98,99,...ord('a'),chr(97)
                    counts[ord(ch) - ord('a')] += 1
        width = int(canvas['width'])
        height = int(canvas['height'])
        maxCounts = max(counts) #빈도수가 높은 최대 값
        heightBar = height*0.75 #canvas 크기의 75%가 최대 막대 바의 높이
        widthBar = width - 20 #canvas 전체 너비에서 좌 10 우 10을 뺀 값
        for i in range(26):  # i=0,1,2,25,a,b,c
            canvas.create_rectangle(i*widthBar/26 +10, height - heightBar*counts[i]/maxCounts - 20, (i+1)*widthBar/26, height-20 )
            canvas.create_text(i*widthBar/26 +10 + 0.5*widthBar/26, height-10, text=chr(i+ord('a')))
        infile.close()

    except IOError:
        tkinter.messagebox.showwarning(filename + "파일이 존재하지 않습니다.")
    pass

'''
def showResult():
    fn = filename.get()
    try:
        infile = open(fn, "r")
        counts = [0]*26 #[0,0,...]
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha(): #a,b,c,d,...,z,97,98,99,...ord('a'),chr(97)
                    counts[ord(ch)-ord('a')] += 1
        for i in range(26): #i=0,1,2,25,a,b,c
            if counts[i] != 0:
                text.insert(END,chr(i+ord('a'))+"-"+str(counts[i])+'번 나타납니다.\n')
        infile.close()

    except IOError:
        tkinter.messagebox.showwarning(filename+"파일이 존재하지 않습니다.")
'''

window = Tk()
window.title("문자의 출현 빈도수")
frame1 = Frame(window)
frame1.pack()
#scrollbar = Scrollbar(frame1)
#scrollbar.pack(side=RIGHT, fill=Y)
#text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand = scrollbar.set)
#text.pack()
#scrollbar.config(command=text.yview)
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()
Label(frame2,text="파일명을 입력하세요:").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable = filename).pack(side=LEFT)
Button(frame2,text="열기",command=openFile).pack(side=LEFT)
Button(frame2,text="결과보기",command=showResult2).pack(side=LEFT)
window.mainloop()