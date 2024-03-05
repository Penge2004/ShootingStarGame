import pygame

pygame.font.init()     # for the writing fonts
pygame.init()

WIDTH, HEIGHT = 1915 , 1000        # screen dimensions
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))    # generating the window
pygame.display.set_caption('Shooting star')

BACKGROUND_IMAGE = pygame.image.load(r"C:\Users\nagyb\jpg_for_pygame\pexels-felix-mittermeier-957061.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

FONT = pygame.font.SysFont('comicsans', 30)   # the font of the texts


def draw(player, elapsed_time, stars,score,best_score):      # the rendering function
    WINDOW.blit(BACKGROUND_IMAGE, (0, 0))  # where it puts the left top corner of the back image

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, 'white')  # time counter
    WINDOW.blit(time_text, (10, 10)) # renders the time text

    pygame.draw.rect(WINDOW, 'blue', player) # this is the player

    score_text = FONT.render(f"Score: {score}",1,'white')
    best_score_text = FONT.render(f"Your best score: {best_score}", 1, 'white')
    WINDOW.blit(score_text,(WIDTH-300,10))
    WINDOW.blit(best_score_text,(WIDTH-300,40))

    for star in stars:
        pygame.draw.rect(WINDOW, star['color'], star['rect']) # it renders the shooting stars

    pygame.display.update()   # updates the visuals of the game