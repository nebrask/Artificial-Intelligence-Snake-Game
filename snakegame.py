import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
white = (255, 255, 255)
display_width = 500
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
snake_block = 10
snake_list = []
snake_speed = 15


def snake_body(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, green, [i[0], i[1], snake_block, snake_block])



def snakegame():
    game_over = False
    game_end = False
    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
    snake_list = []
    length_of_snake = 1

    while not game_over:
        score = length_of_snake - 1
        score_font = pygame.font.SysFont("comicsansms", 15)
        value = score_font.render("Score: " + str(score), True, white)

        while game_end:
            dis.fill(black)
            font_style = pygame.font.SysFont("comicsansms", 25)
            restart = font_style.render("Press R if you want to start again", True, white)
            dis.blit(restart, [display_width / 10, display_height / 13])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        snakegame()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        dis.blit(value, [display_width / 1.20, display_height / 40])
        pygame.display.update()

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_end = True
        snake_body(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


snakegame()

# class Snake:
#   pass

# class Food:
#   pass

# def next_turn():
#   pass

# def change_direction():
#   pass

# def check_collision
