import pygame
import time
import math


pygame.init()


win_width = 900
win_height = 700
screen = pygame.display.set_mode((win_width, win_height))


pygame.display.set_caption("Mickey Mouse Clock")


mickey_body = pygame.image.load("main-clock.png")
mickey_left_hand = pygame.image.load("left-hand.png")
mickey_right_hand = pygame.image.load("right-hand.png")

minute_angle = 0
second_angle = 0


clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 50)


def draw_clock(screen):
   
    body_rect = mickey_body.get_rect(center=(win_width/2, win_height/2))
    screen.blit(mickey_body, body_rect)
    
    
    left_hand_rect = mickey_left_hand.get_rect(center=body_rect.center)
    left_hand_image = pygame.transform.rotate(mickey_left_hand, minute_angle)
    screen.blit(left_hand_image, left_hand_rect)
    
    
    right_hand_rect = mickey_right_hand.get_rect(center=body_rect.center)
    right_hand_image = pygame.transform.rotate(mickey_right_hand, second_angle)
    screen.blit(right_hand_image, right_hand_rect)
    
    
    digital_clock = font.render(time.strftime("%H:%M:%S"), True, (255, 255, 255))
    screen.blit(digital_clock, (win_width/2 - digital_clock.get_width()/2, 20))

running = True
while running:
    
    clock.tick(60)
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    current_time = time.localtime()
    
    
    minute_angle = -math.degrees(current_time.tm_min/60 * math.pi * 2) + 90
    second_angle = -math.degrees(current_time.tm_sec/60 * math.pi * 2) + 90
    
    
    screen.fill((0, 0, 0))
    
    
    draw_clock(screen)
    
   
    pygame.display.flip()


pygame.quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
