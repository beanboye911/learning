import pygame, random, time

pygame.init()

bgColor = (255, 255, 255)
scoreColor = (0, 0, 0)
gameoverColor = (255, 5, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('impractical game')
clock = pygame.time.Clock()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

lemon = pygame.image.load('thumbnail.png')
enemy = pygame.image.load('enemy.jpg')
ded = pygame.image.load('ded.jpg')
dedSound = pygame.mixer.Sound('screm.wav')

def showLemon(x, y):
    gameDisplay.blit(lemon, (x, y))

def showEnemy(x, y):
    gameDisplay.blit(enemy, (x, y))

def crash(x, y):
    pygame.mixer.Sound.play(dedSound)
    pygame.mixer.music.stop()
    gameDisplay.blit(ded, (x, y))
    font = pygame.font.SysFont(None, 100)
    text = font.render('Game Over', True, gameoverColor)
    gameDisplay.blit(text, (200, 250))
    pygame.display.update()
    time.sleep(2)

def showScore(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f'Score {score}', True, scoreColor)
    gameDisplay.blit(text, (0, 0))

gameover = False

x=400
y=300
speedx = 0
speedy = 0
score = 0

enemyX = random.randint(0, 100)
enemyY = 0
enemySpeed = 7

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx = -5
            if event.key == pygame.K_RIGHT:
                speedx = 5
            if event.key == pygame.K_UP:
                y -=10
            if event.key == pygame.K_DOWN:
                y +=10

    gameDisplay.fill(bgColor)

    enemyY += enemySpeed
    if enemyY > 600:
        enemyX = random.randint(0, 800)
        enemyY = 0
        score += 10
    
    x += speedx
    y += speedy
    showLemon(x, y)
    showEnemy(enemyX, enemyY)
    showScore(score)

    if enemyX > x -128 and enemyX < x + 128 and enemyY > y-125 and enemyY < y+125:
        crash(x, y)
        gameover = True
    pygame.display.update()
    clock.tick(60)

pygame.quit()
