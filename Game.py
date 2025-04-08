import pygame
import sys
from Board import ROW,COL,SIZE,SCORE_FEILD,Board
from Tetri import Tetrimino,Game_Board
from Tetrimino_list import L

FPS = 30
                                                                                                                                              
pygame.init()

Main_Window = pygame.display.set_mode(((COL+SCORE_FEILD)*SIZE,ROW*SIZE))
Main_Tittle = pygame.display.set_caption("俄羅斯方塊")
my_tetrimino = Tetrimino()
clock = pygame.time.Clock()

while True:
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    #Pygame模板
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and (my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position)> 0:
                my_tetrimino.position -= 1
            if event.key == pygame.K_d and (my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position)< COL-1:
                my_tetrimino.position += 1
            if event.key == pygame.K_j:
                #rotation    
                if my_tetrimino.tetrimino ==L and my_tetrimino.rotation ==0 and (my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position) == COL-1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == L and my_tetrimino.rotation ==2 and (my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position) == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                else:
                    my_tetrimino.rotation += 1
                if my_tetrimino.rotation > 3:
                    my_tetrimino.rotation = 0  #旋轉重置
                   

# pygame 鍵盤輸入
    Main_Window.fill('#ffffff')
    Game_Board.Update(Main_Window)
    my_tetrimino.Draw(Main_Window,my_tetrimino.tetrimino,'red',my_tetrimino.rotation)
    
    pygame.display.update()
