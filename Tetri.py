from Tetrimino_list import L
import pygame
from Board import ROW,COL,SIZE,SCORE_FEILD,Board

class Tetrimino():
    def __init__(self) -> None:
        super().__init__()
        self.tetrimino = L
        self.position = 3 
        self.rotation = 0

    def Draw(self,surface,tetrimino,color,rotation):
        for i in range(len(tetrimino[rotation][0])):
            for j in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    pygame.draw.rect(surface,color,((j+self.position)*SIZE,i*SIZE,SIZE-1,SIZE-1))
    def Left_index(self,tetrimino,rotation):
        for i in range(len(tetrimino[rotation][0])):
            for j in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    return(i)
                
    def Right_index(self,tetrimino,rotation):
        for i in range(len(tetrimino[rotation][0])):
            for j in range(len(tetrimino[rotation])):
                if tetrimino[rotation][i][j] == '1':
                    right = j
        return(right)