import pygame
import time         # the time to be handled
import random       # coordinates
from Scores.score_handling import save_new_best,get_best_score
from Displays.draw_screen import draw
from pygame import mixer

def music():
    mixer.music.load(r"C:\Users\nagyb\Downloads\Space Ambience Atmosphere  Free Sound Effect.mp3")  # music
    mixer.music.play(-1)

def run():

    WIDTH, HEIGHT = 1915, 1000
    PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
    PLAYER_VELOCITY = 5
    STAR_WIDTH = 10
    STAR_HEIGHT = 20  # some basic numbers for the moving objects
    STAR_VELOCITY = 3
    STAR_COLORS = ['yellow', 'green', 'red', 'blue']  # for the meteor(stars)
    STAR_COLOR_PROBABILITY = [0.6, 0.2, 0.1, 0.1]


    music()      # to have music

    best_score = int(get_best_score())    # calls  the function that reads from the best score file


    PLAYER_Y_RENDER_MODIFIER_WHEN_BLUE_STAR = 0        # for later after blue star
    PLAYER_Y_RENDER = HEIGHT - PLAYER_HEIGHT + PLAYER_Y_RENDER_MODIFIER_WHEN_BLUE_STAR

    player = pygame.Rect(WIDTH//2, PLAYER_Y_RENDER, PLAYER_WIDTH, PLAYER_HEIGHT)  # the player proprieties

    clock = pygame.time.Clock()
    start_time = time.time()   # for the time

    star_add_increment = 1500  # to render faster after some time
    star_count = 0
    stars = [] # the stars are stored in a list

    FONT = pygame.font.SysFont('comicsans', 30)  # the font of the texts
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # generating the window

    score= 0
    hit = False
    run = True

    while run:

        star_count += clock.tick(120)
        elapsed_time = time.time() - start_time # to keep track of the time

        if star_count > star_add_increment:
            for _ in range(3):  # generates 3 stars
                star_x = random.randint(0, WIDTH - STAR_WIDTH) # random x coordinate
                star_color = random.choices(STAR_COLORS,STAR_COLOR_PROBABILITY)[0]  # the color of the star
                star = {'rect': pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT), 'color': star_color}
                # the proprieties of the shooting star
                stars.append(star) # it stores in a list

            star_add_increment = max(100, star_add_increment - 50)
            star_count = 0      # for the faster rendering after some time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:     # quit from the game window
                run = False
                break


        # controlls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:            # we can exit the game with escape as well
            break

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - PLAYER_VELOCITY >= 0: # in parantheses bc when not the arrow goes out of
            player.x -= PLAYER_VELOCITY                                                   # the boundrie
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:  # copy because we will remove stars from stars list
            star['rect'].y += STAR_VELOCITY
            if star['rect'].y > HEIGHT:
                stars.remove(star)                     # for wall collisions
            elif star['rect'].y + star['rect'].height > player.y and star['rect'].colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            if star['color'] == 'yellow':
                lost_text = FONT.render('YOU LOST!', 1, 'white')
                WINDOW.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2,
                                        HEIGHT / 2 - lost_text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(4000)

                # update best score when it's the case
                if best_score < score:
                    best_score = score
                    save_new_best(str(best_score))

                break
            else:
                # Continue the game if the collision is any other color
                if star['color'] == 'green':
                    STAR_WIDTH += 5
                    score += 1

                elif star['color'] == 'red':
                    PLAYER_VELOCITY += 2
                    score += 1


                elif star['color'] == 'blue':
                    score += 1

                    PLAYER_WIDTH += 15
                    PLAYER_HEIGHT += 10
                    PLAYER_Y_RENDER_MODIFIER_WHEN_BLUE_STAR = 10

                    player.width = PLAYER_WIDTH
                    player.height = PLAYER_HEIGHT

                    PLAYER_Y_RENDER = HEIGHT - PLAYER_HEIGHT + PLAYER_Y_RENDER_MODIFIER_WHEN_BLUE_STAR
                    # Update the player's vertical rendering position

                    player.y = PLAYER_Y_RENDER

                hit = False




        draw(player, elapsed_time, stars,score,best_score)

    pygame.quit()