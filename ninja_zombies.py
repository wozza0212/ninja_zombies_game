from turtle import color
import pygame
from sys import exit

pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
# import a font
test_font = pygame.font.Font(None, 50)

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800

# Any time you import a new image into pygame, it is classed as anew surface
background = pygame.image.load('ninja_zombies/resources/graveyardtilesetnew/png/BG.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
# Floor tiles
floor_square = pygame.image.load('ninja_zombies/resources/graveyardtilesetnew/png/Tiles/Tile (2).png')
floor_square = pygame.transform.scale(floor_square, (200, 50))
#Text surface
text_surface = test_font.render('Kills:', False, 'White')


# Draw the floor with one function
def draw_floor( floor_square, floor_tiles):
    for x in floor_tiles:
        screen.blit(floor_square,x)



def main():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = 1
                elif event.key == pygame.K_LEFT:
                    direction = -1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    direction = 0
            


        screen.blit(background, (0, 0))
        # Pygrame draws un order of code, so floor must be drawn after the background
        draw_floor(floor_square, [(0,350),(200, 350),(400, 350),(600, 350)])
        # screen.blit(floor_square,(0, 350))
        # screen.blit(floor_square, (200, 350))
        # screen.blit(floor_square,(400, 350))
        # screen.blit(floor_square, (600, 350))
        screen.blit(text_surface, (650, 20))

        pygame.display.update()
        clock.tick(60)

main()