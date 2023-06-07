from tkinter import *
from tkinter import messagebox
import random
class Game2048:
    # 숫자 배경 색 사전
    bg_color = {
        2: '#eee4da',
        4: '#ede0c8',
        8: '#edc850',
        16: '#edc53f',
        32: '#f67c5f',
        64: '#f65e3b',
        128: '#edcf72',
        256: '#edcc61',
        512: '#f2b179',
        1024: '#f59563',
        2048: '#edc22e',
    }
    # 숫자 색 사전
    color = {
        2: '#776e65',
        4: '#f9f6f2',
        8: '#f9f6f2',
        16: '#f9f6f2',
        32: '#f9f6f2',
        64: '#f9f6f2',
        128: '#f9f6f2',
        256: '#f9f6f2',
        512: '#776e65',
        1024: '#f9f6f2',
        2048: '#f9f6f2',
    }
    #nxn self.gridCell 격자에서 비어있는 셀 (숫자:0)들만 골라서
    #cells 리스트에 위치(r,c)를 모두 모아서 random.choice 랜덤하게 1개 선택하고 그 위치를 2로 설정
    def random_cell(self):
        cells = []
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    cells.append((r,c))
        (r,c) = random.choice(cells)
        self.gridCell[r][c] = 2
    def paintGrid(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    self.board[r][c] .configure(text='',bg='azure4')
                else: #숫자색과 배경색을 칠하기
                    self.board[r][c].configure(text=str(self.gridCell[r][c]), bg=self.bg_color[self.gridCell[r][c]], fg=self.color[self.gridCell[r][c]])
    def compressGrid(self):
        self.compress = False
        temp = [[0] * self.n for _ in range(self.n)] #nxn 0으로 초기화된 2D격자
        for r in range(self.n):
            cnt = 0
            for c in range(self.n):
                if self.gridCell[r][c] != 0:
                    temp[r][cnt] = self.gridCell[r][c]
                    if cnt != c:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp
    def mergeGrid(self):
        self.merge = False
        for r in range(self.n):
            for c in range(self.n - 1):
                if self.gridCell[r][c] == self.gridCell[r][c + 1] and self.gridCell[r][c] != 0:
                    self.gridCell[r][c] *= 2
                    self.gridCell[r][c + 1] = 0
                    self.score += self.gridCell[r][c]
                    self.merge = True
    def transpose(self):
        self.gridCell = [list(t) for t in zip(*self.gridCell)]
    def reverse(self):
        for r in range(self.n):
            self.gridCell[r].reverse()
    def can_merge(self):
        #좌우 검사
        for r in range(self.n):
            for c in range(self.n-1):
                if self.gridCell[r][c] == self.gridCell[r][c+1]:
                    return True
        #상하 검사
        for r in range(self.n-1):
            for c in range(self.n-1):
                if self.gridCell[r][c] == self.gridCell[r+1][c]:
                    return True
        return False
    def link_keys(self, event):
        if self.end or self.won:
            return
        #변수 초기화
        self.compress = False
        self.merge = False
        self.moved = False
        key = event.keysym #키 심볼
        if key == 'Up':
            self.transpose() #행과 열 전치
            self.compressGrid()  # 좌로 밀착
            self.mergeGrid()  # 좌우 같은 숫자 merge
            self.moved = self.compress or self.merge
            self.compressGrid()  # 한번 더 좌로 밀착
            self.transpose() #행과 열 전치
        elif key =='Down':
            self.transpose()  # 행과 열 전치
            self.reverse()
            self.compressGrid()  # 좌로 밀착
            self.mergeGrid()  # 좌우 같은 숫자 merge
            self.moved = self.compress or self.merge
            self.compressGrid()  # 한번 더 좌로 밀착
            self.reverse()
            self.transpose()  # 행과 열 전치
        elif key == 'Left':
            self.compressGrid() #좌로 밀착
            self.mergeGrid() #좌우 같은 숫자 merge
            self.moved = self.compress or self.merge
            self.compressGrid() #한번 더 좌로 밀착
        elif key == 'Right':
            self.reverse()
            self.compressGrid()  # 좌로 밀착
            self.mergeGrid()  # 좌우 같은 숫자 merge
            self.moved = self.compress or self.merge
            self.compressGrid()  # 한번 더 좌로 밀착
            self.reverse()
        flag =0
        for r in range(self.n):
            for c in range(self.n):
                if(self.gridCell[r][c] == 2048):
                    flag =1
                    break
        if flag == 1:
            self.won = True
            messagebox.showinfo('2048','Yon won!!')
            return
        for r in range(self.n):
            for c in range(self.n):
                if(self.gridCell[r][c] ==0):
                    flag = 1
                    break
        if not (flag or self.can_merge()):
            self.end = True
            messagebox.showinfo('2048','Game Over!!')
        if self.moved:
            self.random_cell()
        self.paintGrid()

    def __init__(self,size):
        self.n = size #size에 따라서 4x4, 5x5, 6x6 다양한 게임판 생성
        self.window = Tk()
        self.window.title('2048 Game')
        self.gameArea = Frame(self.window,bg='azure3')
        self.gridCell = [[0]*self.n for _ in range(self.n)] #nxn 2D 숫자 격자 (0으로 초기화, 0:빈셀)
        self.compress = False #좌로 밀착되었는가?
        self.merge = False #좌우 인접셀이 merge 되었는가?
        self.end = False #종료?
        self.won = False #승리?
        self.score = 0 #게임 점수
        self.board = [] #2D 라벨 격자 생성
        for r in range(self.n):
            rows = []
            for c in range(self.n):
                l = Label(self.gameArea, text='', bg='azure4', font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=r,column=c,padx=7,pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.pack()
        self.random_cell()
        self.random_cell()
        self.paintGrid()
        self.window.bind('<Key>', self.link_keys) #키입력 이벤트 핸들러 함수
        self.window.mainloop()

Game2048(4)


