import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

running = True
score = 0
autoclick_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score += 1
    
    autoclick_counter += 1
    if autoclick_counter >= 6000: # auto-click every 10 seconds
        score += 1
        autoclick_counter = 0
    
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (350, 275))
    pygame.display.update()
    clock.tick(60)

pygame.quit()