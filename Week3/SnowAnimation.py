"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

possible_colors=[BLACK, WHITE, GREEN, RED, BLUE]
snow_color=random.choice(possible_colors) 
snow_size= random.randint(5, 20)

ypos= random.randint(0, 500)
xpos= random.randint(0, 700)

position= [xpos, ypos]

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
    # '''
    # This class will be used to create the SnowFlake Objects.
    # It takes: 
    #     size - an integer that tells us how big we want the snowflake
    #     position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
    #     wind - a boolean that lets us know if there is any wind or not.  
    # '''

    def __init__(self, size, position, wind=False):
        # size1= random.randint(2, 8)  
     
        self.size= size
        self.position= position
        self.wind= wind
    
    
    def fall(self, speed):
        self.speed= speed
       
        # """
        # Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        # A positive integer will have the snowflake falling down the screen. 
        # A negative integer will have the snowflake falling up the screen. 
        
        # If wind = True
        #     - the x direction of the snowflake changes
        # """
        
    def draw(self):
        pygame.draw.circle(screen, snow_color, position, snow_size)
        # """
        # Uses pygame and the global screen variable to draw the snowflake on the screen
        # """
snow1= SnowFlake(snow_size, position)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
# speed = 1


#INITIALIZE YOUR SNOWFLAKE HERE! 
speed1= random.randint(-20, 20)

# Snow List
snow_list = []

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
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Begin Snow

    for i in range(20):
        possible_colors=[BLACK, WHITE, GREEN, RED, BLUE]
        snow_color=random.choice(possible_colors) 
        snow_size= random.randint(5, 20)

        ypos= random.randint(0, 500)
        xpos= random.randint(0, 700)

        position= [xpos, ypos]

        snow1.draw()
    snow1.fall(speed1)



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
