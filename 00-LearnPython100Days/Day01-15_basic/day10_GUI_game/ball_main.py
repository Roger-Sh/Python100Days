import pygame
from random import randint

import ball_game.ball as ba
import ball_game.color as co


def main():
    # container for all balls
    balls = []

    # init pygame
    pygame.init()

    # init screen
    screen = pygame.display.set_mode((800, 600))
    # title
    pygame.display.set_caption('大球吃小球')

    # running loop
    running = True
    while running:
        # loop event queue
        for event in pygame.event.get():
            # exit event
            if event.type == pygame.QUIT:
                running = False

            # handle mouse event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # get mouse click position
                x, y = event.pos

                # get radius, sx, sy, color randomly
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = co.Color.random_color()

                # generate a random ball in mouse click position
                ball = ba.Ball(x, y, radius, sx, sy, color)

                # put ball in ball container
                balls.append(ball)

        # screen background
        screen.fill((255, 255, 255))

        # check balls, draw or remove
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        # screen flip
        pygame.display.flip()

        # change ball position per 50ms
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)

            # check this ball can eat other ball or not
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
