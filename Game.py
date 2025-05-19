import pygame
import sys
from Board import ROW,COL,SIZE,SCORE_FEILD,Board
from Tetri import Tetrimino,Game_Board
from Tetrimino_list import L,S,Z,I,J,T

FPS = 5
GAME_ON = True                                                                                                                                            
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
                if event.key == pygame.K_RETURN:
                    if not GAME_ON:
                        GAME_ON = True
                        Game_Board.Restar()
                if event.key == pygame.K_a and  (my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position)> 0 and  not my_tetrimino.Coliide_left(my_tetrimino.tetrimino,my_tetrimino.rotation):
                    my_tetrimino.position -= 1
                if event.key == pygame.K_d and (my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position)< COL-1 and not my_tetrimino.Coliide_right(my_tetrimino.tetrimino,my_tetrimino.rotation):
                    my_tetrimino.position += 1
                if event.key == pygame.K_j:

                #rotation    
                # L transform
                    if my_tetrimino.tetrimino == L and my_tetrimino.rotation ==2 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == L and my_tetrimino.rotation ==0 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    # S transform
                    elif my_tetrimino.tetrimino == S and my_tetrimino.rotation ==1 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == S and my_tetrimino.rotation ==3 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    # Z transform
                    elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation ==1 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation ==3 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    # LINE transform
                    elif my_tetrimino.tetrimino == I and my_tetrimino.rotation ==1 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position >= 8:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == I and my_tetrimino.rotation ==1 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == I and my_tetrimino.rotation ==3 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position >= 8:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == I and my_tetrimino.rotation ==3 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    # J transform
                    elif my_tetrimino.tetrimino == J and my_tetrimino.rotation ==0 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == J and my_tetrimino.rotation ==2 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    # T transform
                    elif my_tetrimino.tetrimino == T and my_tetrimino.rotation ==1 and my_tetrimino.Left_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 0:
                        my_tetrimino.rotation = my_tetrimino.rotation
                    elif my_tetrimino.tetrimino == T and my_tetrimino.rotation ==3 and my_tetrimino.Right_index(my_tetrimino.tetrimino,my_tetrimino.rotation) + my_tetrimino.position == 9:
                        my_tetrimino.rotation = my_tetrimino.rotation

                    elif my_tetrimino.Coliide_roatation(my_tetrimino.tetrimino,my_tetrimino.rotation):
                        my_tetrimino.rotation = my_tetrimino.rotation #選轉碰撞
                    else:
                        my_tetrimino.rotation += 1
                    if my_tetrimino.rotation > 3:
                        my_tetrimino.rotation = 0  #旋轉重置
                        
    if GAME_ON:
# pygame 鍵盤輸入
        Main_Window.fill('#ffffff')
        Game_Board.Update(Main_Window)
        my_tetrimino.Draw(Main_Window,my_tetrimino.tetrimino,'red',my_tetrimino.rotation)
        
        pygame.display.update()
        if Game_Board.Game_Over():
            GAME_ON =False