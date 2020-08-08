import pygame

pygame.init()

bgColor = (255, 255, 255)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('impractical game')

lemon = pygame.image.load('thumbnail.png')

def showLemon(x, y):
    gameDisplay.blit(lemon, (x, y))

gameover = False

x=400
y=300

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -=10
            if event.key == pygame.K_RIGHT:
                x +=10

    gameDisplay.fill(bgColor)
    showLemon(x, y)
    pygame.display.update()

pygame.quit()
