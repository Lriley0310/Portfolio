import pygame
from pygame.locals import *
import random

pygame.init()

#window config
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

#color assign
grey = (100, 100, 100)
green = (91, 129, 80)
red = (255, 38, 0 )
white = (255, 255, 255)
yellow = (255, 254, 0)

#settings
gameover = False
speed = 2
score = 0

#marker sizes
marker_width = 10
marker_height = 50

#road and curb
road =(100, 0, 300, height)
left_curb = (95, 0, marker_width, height)
right_curb = (395, 0, marker_width, height)

# x cords
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

#lane marker animation
lane_marker_move_y = 0

class Vehichle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        #image scale
        image_scale = 75 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Vehicle_sprite(Vehichle):

    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)

#start cords
player_x = 250
player_y = 400

#player car
player_group = pygame.sprite.Group()
player = Vehicle_sprite(player_x, player_y)
player_group.add(player)

#other vehicles
image_files = ['white_car.png', 'semi_trailer.png', 'taxi.png', 'van.png']
Vehichle_images = []
for image_files in image_files:
    image = pygame.image.load('images/' + image_files)
    Vehichle_images.append(image)

#sprite group
vehicle_group = pygame.sprite.Group()

#crash load
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

#lane movement
lane_marker_move_y = 0

clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        #player movement
        if event.type == KEYDOWN:

            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
            #collision check
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True
                    #crah image position
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center[player.rect.right, (player.rect.center[1] + vehicle.rect.center[1] / 2)]
    #grass      
    screen.fill(green)

    #road
    pygame.draw.rect(screen,grey,road)

    #curb
    pygame.draw.rect(screen, yellow, left_curb)
    pygame.draw.rect(screen, yellow, right_curb)

    #lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white,(left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    #draw player car
    player_group.draw(screen)

    #add up 
    if len(vehicle_group) < 2:

        #enought space
        add_vehichle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehichle = False

        if add_vehichle:
            #random lane
            lane = random.choice(lanes)
            #random sprite
            image = random.choice(Vehichle_images)
            vehicle = Vehichle(image, lane, height / -2)
            vehicle_group.add(vehicle)
    #npc movement
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        #vehicle removal
        if vehicle.rect.top >= height:
            vehicle.kill()
            #score adding
            score += 1
            #speed up
            if score > 0 and score % 5 == 0:
                speed += 1
    #npc draw
    vehicle_group.draw(screen)

    #score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 450)
    screen.blit(text, text_rect) 

    #collision check
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]

    #gameover display
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)     
        text = font.render('Game Over. Play again? (Y or N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect) 

    pygame.display.update()

    #play again checkl
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            if event.type == KEYDOWN:
                if event.key == K_y:
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    gameover = False
                    running = False

pygame.quit()


