import pygame, random
width, height, exited = 300, 600, False
pygame.init()
space = pygame.display.set_mode((width, height))
x_ship, y_ship = width//2 - 25, 550
x_y_width_of_enemies = [[random.randint(0, width), 0, random.randint(50, 150)]]
timePassed, dx = 0, 0
while True:
    if exited: break
    space.fill((0,0,0))
    if x_y_width_of_enemies[-1][1] > 25+150: # if last enemy is distanced 150 pixels from top, add one
        x_y_width_of_enemies.append([random.randint(0, width), 0, random.randint(0, 150)])
    fx, fy, fw = x_y_width_of_enemies[0] # x, y and width of first enemy
    if fy >= height: # if fist enemy leaves the space, delete him
        del x_y_width_of_enemies[0]
    if fy+50 > height-50 and ((x_ship < fx and x_ship+50 > fx) or (fx < x_ship and fx+fw>x_ship)):
        break # if we hit an enemy ship we end the game
    for x_y_w in x_y_width_of_enemies: # go through all enemies
        x, y, w = x_y_w
        # draw enemies
        enemy = pygame.Rect(x, y, w, 50)
        pygame.draw.rect(space, (255, 255, 255), enemy)
        if timePassed > 4: # move enemy every 5 updates
            x_y_w[1] = x_y_w[1]+1
    if timePassed > 4: # set updates counter to 0
        timePassed = 0
    # Draw the ship
    ship = pygame.Rect(x_ship, y_ship, 50, 50)
    pygame.draw.rect(space, (255, 255, 255), ship)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -0.15
            if event.key == pygame.K_RIGHT:
                dx = 0.15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
    x_ship += dx
    x_ship = width - 50 if x_ship >= width - 50 else x_ship
    x_ship = 0 if x_ship <= 0 else x_ship
    timePassed += 1
