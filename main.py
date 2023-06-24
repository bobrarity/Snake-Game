import pygame
import random


pygame.init()

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.update()
pygame.display.set_caption('Snake')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

snake_size = 10
snake_speed = 10

clock = pygame.time.Clock()
dis.fill(white)
font_style = pygame.font.SysFont('Font style', 50)
score_font = pygame.font.SysFont('Score font', 35)


def your_score(score):
    value = score_font.render(f'Your score: {str(score)}', True, green)
    dis.blit(value, [0, 0])


def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [60, dis_height / 2])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message('Game Over! Press Q -  Quit  or R - Restart', black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_size, snake_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)
        your_score(length_of_snake - 1)

        pygame.draw.rect(dis, black, [x1, y1, snake_size, snake_size])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print('Ate')
            foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
