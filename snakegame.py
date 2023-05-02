import pygame
import random

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (50, 78, 168)
green = (50, 168, 83)
font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()

snake_block_size = 10
snake_speed = 10
snake_list = []
snake_length = 1

# Food
food_block_size = 10
food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0

def draw_snake(snake_block_size, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:
            # draw blue head
            pygame.draw.rect(screen, blue, [x[0], x[1], snake_block_size, snake_block_size])
        else:
            # draw green body
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block_size, snake_block_size])

def message(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 3])

#Loop
game_over = False
game_close = False
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_x_change = 0
snake_y_change = 0

score = 0

while not game_over:
    while game_close:
        screen.fill(white)
        message("Game Over! Press Q-Quit", blue)
        score_text = font.render("Score: " + str(score), True, black)
        screen.blit(score_text, [0, 0])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_close = True

    snake_x += snake_x_change
    snake_y += snake_y_change
    screen.fill(white)
    pygame.draw.rect(screen, red, [food_x, food_y, food_block_size, food_block_size])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    draw_snake(snake_block_size, snake_list)
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])
    pygame.display.update()

    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_block_size) / 10.0) * 10.0
        snake_length += 1
        score += 10

    clock.tick(snake_speed)

pygame.quit()
quit()