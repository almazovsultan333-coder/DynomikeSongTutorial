# Угадай цвет
import pygame
import sys
import random

pygame.init()

width,height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Угадай цвет")



COLORS = {

"RED": (255, 0, 0),

"GREEN": (0,255, 0),

"BLUE": (0, 0, 255),

"YELLOW": (255, 255, 0), 

"CYAN": (0, 255, 255),

"MAGENTA": (255, 0, 255),

"WHITE": (255, 255, 255),

"BLACK": (0,0,0),

"TEAL" : (0, 128, 128), 

"PURPLE": (128,0,128),

'ORANGE':(255,165,0)

}

# Список цветов и текущий цвет
color_keys = list(COLORS.keys())
current_color = random.choice(color_keys) # Случайный начальный цвет

# Основной игровой цикл
while True: # бесконечный цикл
    for event in pygame.event.get(): # Обработка событий
        if event.type == pygame.QUIT: # Закрытие окна
            pygame.quit() # Выход из Pygame
            sys.exit() # Выход из программы

        if event.type == pygame.KEYDOWN: # Проверка нажатия клавиши
            # Изменение цвета фона при нажатии любой клавиши
            if event.key == pygame.K_r: # Если нажата 'R'
                current_color = "RED"
            elif event.key == pygame.K_g: # Если нажата 'G'
                current_color = "GREEN"
            elif event.key == pygame.K_b: # Если нажата 'B'
                current_color = "BLUE"
            elif event.key == pygame.K_y: # Если нажата 'Y'
                current_color = "YELLOW"
            elif event.key == pygame.K_c: # Если нажата 'C'
                current_color = "CYAN"
            elif event.key == pygame.K_m: # Если нажата 'M'
                current_color = "MAGENTA"
            elif event.key == pygame.K_w: # Если нажата 'W'
                current_color = "WHITE"
            elif event.key == pygame.K_k: # Если нажата 'K'
                current_color = "BLACK"
            elif event.key == pygame.K_z:
                current_color = "TEAL" 
            elif event.key == pygame.K_p: 
                current_color = "PURPLE"  
            elif event.key == pygame.K_o:
                current_color = "ORANGE"     

# Заливка экрана текущим цветом
screen.fill(COLORS[current_color])

    # Обновление экрана
pygame.display.flip()


pygame.display.set_mode((200, 200))
sound = pygame.mixer.Sound("red-7991.mp3")

running = True
while running:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:  
        running = False
  elif event.type == pygame.KEYDOWN:  
   if event.key == pygame.K_r:  
    sound.play() 


pygame.quit()
        
    
  