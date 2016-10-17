import pygame
import random
pygame.init()

width = 1000
height = 500

white = (255,255,255)
black = (0,0,0)

dice1 = pygame.image.load("Teningar/sd1.png")
dice2 = pygame.image.load("Teningar/sd2.png")
dice3 = pygame.image.load("Teningar/sd3.png")
dice4 = pygame.image.load("Teningar/sd4.png")
dice5 = pygame.image.load("Teningar/sd5.png")
dice6 = pygame.image.load("Teningar/sd6.png")

dice = [dice1,dice2,dice3,dice4,dice5,dice6]

dice_len, dice_height = dice1.get_rect().size
screen = pygame.display.set_mode((width,height)) 

pygame.display.set_caption("plato el plomo?")

comp_dice = list()
user_dice = list()

for x in xrange(0,5):
	comp_dice.append(random.randint(1,6))
	user_dice.append(random.randint(1,6))

running = True

while running:
	x = 10
	y = 10

	screen.fill(white)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for a in xrange(0, len(comp_dice)):
		screen.blit(dice[comp_dice[a]-1], (x,y))
		x = x + dice_len
	
	y = y+dice_height
	x = 10

	for a in xrange(0,len(user_dice)-1):
		screen.blit(dice[user_dice[a]-1], (x,y))
		x = x + dice_len
	screen.blit(dice[random.randint(0,5)], (x,y))
#Gera 2 takka
#kasta osynilega aftur
#kasta ollum aftur

	pygame.draw.rect(window)	



	pygame.display.update()

pygame.quit()