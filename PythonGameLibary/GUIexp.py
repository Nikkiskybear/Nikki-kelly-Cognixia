
import pygame
import random
#runs the game and returns the score
def playgame():
    #gets everything set up
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    #sets the player starting posision 
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    #sets the target position
    targetx = random.randint(0, screen.get_width())
    targety = random.randint(0, screen.get_height())
    s = pygame.Rect(targetx, targety, 20, 20)

    score = 0

    while running:
        #if window is closed ends the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #fills in the screen and renders all the parts
        screen.fill("black")
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Score: " + str(score), 1, (255,255,0))
        screen.blit(label, (100,100))
        #pygame.draw.polygon(screen, "blue", target )
        pygame.draw.rect(screen, "green", s)
        pygame.draw.circle(screen, "red", player_pos, 20)
        #moves the player on key press
        #stops the player from moving off the screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
            if player_pos.y < 0:
                player_pos.y = 0
            
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
            if player_pos.y > screen.get_height():
                player_pos.y = screen.get_height()
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
            if player_pos.x < 0:
                player_pos.x = 0
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
            if player_pos.x > screen.get_width():
                player_pos.x = screen.get_width()
        #checks if the player collieds with the target and adds the score
        collide = s.collidepoint(player_pos)
        if collide:
            targetx = random.randint(0, screen.get_width())
            targety = random.randint(0, screen.get_height())
            s = pygame.Rect(targetx, targety, 20, 20)
            score += 1
        

    
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
    return score