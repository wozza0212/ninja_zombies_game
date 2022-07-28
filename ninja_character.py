import pygame

class NinjaCharacter(pygame.sprite.Sprite):
    moving_images = {
        'walk_right':[pygame.image.load(f'resources/ninjas/move_right/Run__00{x}.png') for x in range(0,10)],
        'walk_left':[pygame.image.load(f'resources/ninjas/move_right/Run__00{x}.png') for x in range(0,10)],
        'idle':[pygame.image.load(f'resources/ninjas/idle/Idle__00{x}.png') for x in range(0,10)]
    }

    def __init__(self, x, y, width, height):
        self.x_position = x
        self.y_position = y

        self.width = width
        self.height = height

        self.object_image = self.moving_images['idle']
        

