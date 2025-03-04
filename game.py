import pygame
import sys
import config # Import the config Module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        # Code for the first initial A
        pygame.draw.line(screen,config.BLUE,(200,100),(150,350), 5)
        pygame.draw.line(screen,config.BLUE,(200,100),(250,350), 5)
        pygame.draw.line(screen,config.BLUE,(180,200),(220,200), 5)
        # Code for  the second initial W
        pygame.draw.line(screen,config.BLUE,(300,100),(360,350), 5)
        pygame.draw.line(screen,config.BLUE,(360,350),(400,100), 5)
        pygame.draw.line(screen,config.BLUE,(400,100),(430,350), 5)
        pygame.draw.line(screen,config.BLUE,(430,350),(480,100), 5)
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()