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
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    pygame.draw.rect(surface,color,((j+self.position)*SIZE,(i+self.speed)*SIZE,SIZE-1,SIZE-1))

                if (i+self.speed) > ROW:
                    self.Next_round()
        if pygame.key.get_pressed()[pygame.K_s]:
            self.speed +=1   #按住持續下降
    def Left_index(self,tetrimino,rotation):
        for j in range(len(tetrimino[rotation][0])):
            for i in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    return(i)
                
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
    
    def put_into_Board(self,i,tetrimino,rotation,speed,postion,Game_Board):
        if i + self.speed == ROW:
            for x in range(tetrimino[rotation]):
                for y in range(tetrimino[rotation][0]):
                    if tetrimino[rotation][x[y]] == '1':
                        Game_Board[y+postion][x+speed] = 1
            self.Next_round

