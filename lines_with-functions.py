import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption("Draw Lines Without Using a Function")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main(screen):
    # Arguments for first line 
    start_pos1 = [350, 350]
    end_pos1 = [550, 500]
    line_color1 = config.RED
    line_thickness1 = 25  # Set line width (thickness) in pixels

    # Arguments for second line 
    start_pos2 = [250, 350]
    end_pos2 = [225, 330]
    line_color2 = config.BLUE
    line_thickness2 = 2  # Set line width (thickness) in pixels


    # Argument for the third line
    start_pos3 = [650, 550]
    end_pos3 = [300, 530]
    line_color3 = config.PURPLE
    line_thickness3 = 13



    # Arguement for the fourth line
    start_pos4 = [10, 150]
    end_pos4 = [100, 150]
    line_color4 = config.ORANGE
    line_thickness4 = 33



    # Arguement for the fifth line
    start_pos5 = [210, 200]
    end_pos5 = [290, 100]
    line_color5 = config.YELLOW
    line_thickness5 = 9



    # Arguement for the sixth line
    start_pos6 = [510, 300]
    end_pos6 = [600, 400]
    line_color6 = config.GREEN
    line_thickness6 = 69






    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color (optional)
        screen.fill(config.WHITE)  # Assuming you have a WHITE constant in config

        # Draw the lines
        pygame.draw.line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        pygame.draw.line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        pygame.draw.line(screen, line_color3, start_pos3, end_pos3, line_thickness3)
        pygame.draw.line(screen, line_color4, start_pos4, end_pos4, line_thickness4)
        pygame.draw.line(screen, line_color5, start_pos5, end_pos5, line_thickness5)
        pygame.draw.line(screen, line_color6, start_pos6, end_pos6, line_thickness6)

        pygame.display.flip()  # Update the display

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    screen = init_game()  # Initialize the game and get the screen
    main(screen)  # Pass the screen to the main function