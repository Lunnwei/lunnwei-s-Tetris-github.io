from Tetrimino_list import L,Tetrimino_LIST
import pygame
from Board import ROW,COL,SIZE,SCORE_FEILD,Board
import random

Game_Board = Board()

class Tetrimino():
    def __init__(self) -> None:
        super().__init__()
        self.tetrimino = random.choice(Tetrimino_LIST)
        self.position = 3 
        self.rotation = 0
        self.speed = 0

    def Draw(self,surface,tetrimino,color,rotation):
        print("speed: ", self.speed)
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    pygame.draw.rect(surface,color,((j+self.position)*SIZE,(i+int(self.speed))*SIZE,SIZE-1,SIZE-1))
                
                    if (i+self.speed+1) < ROW and Game_Board.board[j+self.position][i+int(self.speed+1)]:
                        for x in range(len(tetrimino[rotation])): #ROW
                            for y in range(len(tetrimino[rotation][0])): #COL
                                if tetrimino[rotation][x][y] == '1':
                                    Game_Board.board[y+self.position][x+int(self.speed)] = 1
                        self.Next_round()

        self.Put_into_Board(i,tetrimino,rotation,self.speed,self.position,Game_Board.board)
        # self.speed += 1
        if pygame.key.get_pressed()[pygame.K_s]:
            self.speed +=1   #按住持續下降
        
    def Coliide_roatation(self,tetrimino,rotation):
        if rotation < 3:
            for j in range(len(tetrimino[rotation+1][0])):
                for i in range(len(tetrimino[rotation+1])):
                    if tetrimino[rotation+1][i][j] == '1' and  Game_Board.board[j+self.position][i+int(self.speed+1)]:
                        return True
        if rotation == 3:
            for j in range(len(tetrimino[0][0])):
                for i in range(len(tetrimino[0])):
                    if tetrimino[0][i][j] == '1' and  Game_Board.board[j+self.position][i+int(self.speed+1)]:
                        return True
            
    def Coliide_left(self,tetrimino,rotation):
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':  
                    if (j+self.position-1)>0 and Game_Board.board[j+self.position-1][i+int(self.speed)]:
                        return True  
                      
    def Coliide_right(self,tetrimino,rotation):
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':  
                    if (j+self.position+1)<COL and Game_Board.board[j+self.position+1][i+int(self.speed)]:
                        return True  

    def Left_index(self,tetrimino,rotation):
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    return(i) #i改j???
                
    def Right_index(self,tetrimino,rotation):
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    right = j
        return(right)

    def Next_round(self):#處底下輪                                                                                                                                                                                                                                                                                                                                                                              
        self.tetrimino = random.choice(Tetrimino_LIST)
        self.position = 3
        self.rotation = 0
        self.speed = 0    
    
    def Put_into_Board(self,i,tetrimino,rotation,speed,postion,Game_Board):
        if i + int(self.speed) == ROW:
            for x in range(len(tetrimino[rotation])): #ROW
                for y in range(len(tetrimino[rotation][0])): #COL
                    if tetrimino[rotation][x][y] == '1':
                        Game_Board[y+postion][int(x+speed)] = 1
            self.Next_round()

    def update(self,surface,tetrimino,color,rotation):
        self.Draw(surface,tetrimino,color,rotation)
        self.speed += 0.05