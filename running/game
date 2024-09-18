import pygame
import math
import random

pygame.init()

# Global constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game')

# Load sprite images
RUNNING = [pygame.image.load("sprite_1.png"), pygame.image.load('sprite_2.png'),
           pygame.image.load('sprite_3.png'), pygame.image.load('sprite_4.png'),
           pygame.image.load('sprite_5.png'), pygame.image.load('sprite_6.png')]
JUMP = pygame.image.load('jump.png')
DUCKING = pygame.image.load('duck.png')
GHOST = [pygame.image.load('ghost1.png'), pygame.image.load('ghost2.png'), pygame.image.load('ghost3.png'),
         pygame.image.load('ghost4.png')]
CACTUS = [pygame.image.load('c1.png'), pygame.image.load('c2.png'), pygame.image.load('c3.png'),
          pygame.image.load('c4.png'), pygame.image.load('c5.png'), pygame.image.load('c6.png'),
          pygame.image.load('c7.png'), pygame.image.load('c8.png'), pygame.image.load('c9.png'),
          pygame.image.load('c10.png'), pygame.image.load('c11.png'), pygame.image.load('c12.png')]

# Create a class for the hero
class Hero:
    x_pos = 80
    y_pos = 500
    y_pos_duck = 560
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMP
        self.duck_img = DUCKING

        self.hero_run = True
        self.hero_jump = False
        self.hero_duck = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.x_pos
        self.hero_rect.y = self.y_pos
        self.hero_hitbox = pygame.Rect(self.hero_rect.x + 20, self.hero_rect.y + 10, self.hero_rect.width - 40, self.hero_rect.height - 20)

    def update(self, userInput):
        if self.hero_duck:
            self.duck()
        if self.hero_run:
            self.run()
        if self.hero_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.hero_jump:
            self.hero_run = False
            self.hero_jump = True
            self.hero_duck = False
        elif userInput[pygame.K_DOWN] and not self.hero_jump:
            self.hero_jump = False
            self.hero_run = False
            self.hero_duck = True
        elif not (self.hero_jump or userInput[pygame.K_DOWN]):
            self.hero_run = True
            self.hero_jump = False
            self.hero_duck = False


    def jump(self):
        self.image = self.jump_img
        if self.hero_jump:
            self.hero_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.hero_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = self.duck_img
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.x_pos
        self.hero_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.hero_rect = self.image.get_rect()
        self.hero_rect.x = self.x_pos
        self.hero_rect.y = self.y_pos
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.hero_rect.x, self.hero_rect.y))
        self.hero_hitbox.topleft = (self.hero_rect.x, self.hero_rect.y)
# Create a class for obstacles
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height - 10)
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        self.hitbox.x = self.rect.x + 10
        self.hitbox.y = self.rect.y + 10
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = 0
        image = [pygame.transform.scale(img, (img.get_width() // 3.5, img.get_height() // 3.5)) for img in image]
        super().__init__(image, self.type)
        self.rect.y = 480
        self.index = 0


    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class Ghost(Obstacle):
    def __init__(self, image):
        self.type = 0
        image = [pygame.transform.scale(img, (img.get_width() // 2.5, img.get_height() // 2.5)) for img in image]
        super().__init__(image, self.type)
        self.rect.y = 400
        self.index = 0


    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1

def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1
    font = pygame.font.Font('freesansbold.ttf', 20)  # Initialize the font
    text = font.render('Points: ' + str(points), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    screen.blit(text, textRect)

def scroll_background(bg, bg_width, scroll, game_speed, tiles, obstacles, player):
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        scroll -= game_speed
        scroll -= 5

        if abs(scroll) > bg_width:
            scroll = 0

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Cactus(CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(Ghost(GHOST))

    for obstacle in obstacles:
        obstacle.draw(screen)
        obstacle.update()
    player.draw(screen)
    return bg, tiles, scroll

def check_collisions(obstacles, player, death_count):
    for obstacle in obstacles:
        if player.hero_hitbox.colliderect(obstacle.hitbox):
            if player.hero_duck:
                if obstacle.hitbox.y + obstacle.hitbox.height - player.hero_hitbox.y < 10:
                    continue  # No collision if the hero is ducking under the obstacle
            else:
                pygame.time.delay(2000)
                death_count += 1
                return False, death_count

    return True, death_count

# Main game function
def main_game():
    global game_speed, points, obstacles

    clock = pygame.time.Clock()
    player = Hero()
    game_speed = 14
    points = 0
    obstacles = []
    death_count = 0

    game_active = True

    # Background setup
    bg = pygame.image.load('bg.png')
    bg_width = bg.get_width()
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        bg, tiles, scroll = scroll_background(bg, bg_width, scroll, game_speed, tiles, obstacles, player)
        game_active, death_count = check_collisions(obstacles, player, death_count)
        if not game_active:
            menu(death_count)

        score()
        pygame.display.update()
        clock.tick(30)

# Menu function
def menu(death_count):
    global points

    while True:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            screen.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)
        screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                points = 0
                return

# Start the menu
menu(0)

# Enter the game loop
while True:
    points = 0
    main_game()

# Cleanup
pygame.quit()
