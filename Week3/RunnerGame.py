import pygame
import random
from CityScroller import Scroller


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

class RunnerSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.color= color
        self.width= width
        self.height= height
        self.image= pygame.Surface((width, height))
        mouse_pos= pygame.mouse.get_pos()
        self.rect= self.image.get_rect(center= mouse_pos)
        self.image.fill(self.color)




# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done= False



FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (168, 250, 239)
clock = pygame.time.Clock()



front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)




# self.x_pos= mouse_pos


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    all_sprites_list= []
        
    all_sprites_list= pygame.sprite.Group()        
    runner= RunnerSprite(WHITE, 40, 40)
    all_sprites_list.add(runner)
   

    # --- Drawing code should go here
    pygame.draw.circle(screen, (255, 186, 105), [80, 80], 40, 0)
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

    all_sprites_list.draw(screen)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
