import pygame

pygame.init()
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

ball_radius = 25
ball_pos = [300, 200]

ball_speed = 20

white = (255, 255, 255)
red = (255, 0, 0)

def draw_ball(screen, pos):
    pygame.draw.circle(screen, red, pos, ball_radius)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1]-= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += ball_speed
    
    if ball_pos[0] < ball_radius:
        ball_pos[0] = ball_radius
    elif ball_pos[0] > width - ball_radius:
        ball_pos[0] = width - ball_radius
    elif ball_pos[1] < ball_radius:
        ball_pos[1] = ball_radius
    elif ball_pos[1] > height - ball_radius:
        ball_pos[1] = height - ball_radius

    screen.fill(white)
    draw_ball(screen, ball_pos)

    pygame.display.update()
pygame.quit()