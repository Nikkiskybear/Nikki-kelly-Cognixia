
import pygame
import random
def playgame():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


    targetx = random.randint(0, screen.get_width())
    targety = random.randint(0, screen.get_height())
    s = pygame.Rect(targetx, targety, 20, 20)

    score = 0

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        screen.fill("black")
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Score: " + str(score), 1, (255,255,0))
        screen.blit(label, (100,100))
        #pygame.draw.polygon(screen, "blue", target )
        pygame.draw.rect(screen, "green", s)
        pygame.draw.circle(screen, "red", player_pos, 20)

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