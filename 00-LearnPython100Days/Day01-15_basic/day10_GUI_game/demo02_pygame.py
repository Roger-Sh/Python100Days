import pygame

def main():
    # init pygame
    pygame.init()
    # init window
    screen = pygame.display.set_mode((800, 600))

    # title
    pygame.display.set_caption('big ball eats small ball')

    # running loop
    running = True
    while running:
        # get event from event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
