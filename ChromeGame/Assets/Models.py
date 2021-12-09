import pygame
import random

from Init import *

class Man:
    X_POS = 80
    Y_POS = 300
    Y_POS_DUCK = 340
    JUMP_SPEED = 8.5

    def __init__(self):
        self.ducking_img = DUCKING
        self.running_img = RUNNING
        self.jumping_img = JUMPING

        self.ducking = False
        self.running = True
        self.jumping = False

        self.jump_speed = self.JUMP_SPEED
        self.image = self.running_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS

    def update(self, userInput):
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if self.jumping:
            self.jump()


        if userInput[pygame.K_UP] and not self.jumping:
            self.ducking = False
            self.running = False
            self.jumping = True
        elif userInput[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif not (self.jumping or userInput[pygame.K_DOWN]):
            self.ducking = False
            self.running = True
            self.jumping = False

    def duck(self):
        self.image = self.ducking_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS_DUCK

    def run(self):
        self.image = self.running_img
        self.man_rect = self.image.get_rect()
        self.man_rect.x = self.X_POS
        self.man_rect.y = self.Y_POS

    def jump(self):
        self.image = self.jumping_img
        if self.jumping:
            self.man_rect.y -= self.jump_speed * 4
            self.jump_speed -= 0.8
        if self.jump_speed < - self.JUMP_SPEED:
            self.jumping = False
            self.jump_speed = self.JUMP_SPEED

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.man_rect.x, self.man_rect.y))


class Obstacle():
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self,game_speed,obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.video_value = 2
        if self.type == 0 or self.type == 1:
            self.rect.y = 325
        elif self.type == 2 or self.type == 3:
            self.rect.y = 300
        else:
            self.rect.y = 335
            self.video_value = 3

    def identify(self):
        return self.video_value


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        if self.type == 3 or self.type == 4 or self.type == 5:
            self.rect.y = 325
        else:
            self.rect.y = 300
        #self.rect.y = 300

    def identify(self):
        value = self.type + 3
        return 2


class Drone(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

    def identify(self):
        return 2
        #return 7


class Shrine(Obstacle):
    def __init__(self,image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 75

    def identify(self):
        return 9


class Sovereign:
    X_POS = 75
    Y_POS = SCREEN_HEIGHT - 30
    SPEED = 1
    HP = 5
    def __init__(self):
        self.image = SOVEREIGN
        self.sovereign_rect = self.image.get_rect()
        self.sovereign_rect.x = self.X_POS
        self.sovereign_rect.y = self.Y_POS

    def movement(self, userInput):
        if userInput[pygame.K_UP] and self.sovereign_rect.y - self.SPEED > 20:
            self.sovereign_rect.y -= self.SPEED
        if userInput[pygame.K_DOWN] and self.sovereign_rect.y + self.SPEED < SCREEN_HEIGHT - 30:
            self.sovereign_rect.y += self.SPEED


    def draw(self, SCREEN2):
        SCREEN.blit(self.image, (self.sovereign_rect.x, self.sovereign_rect.y))


class Eye:
    X_POS = SCREEN_WIDTH - 50
    Y_POS = 200
    def __init__(self):
        return