import sys

import pygame

def check_events(ship):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.movingRight= True
			elif event.key == pygame.K_LEFT:
				ship.movingLeft = True
			elif event.key == pygame.K_UP:
				ship.movingUp = True
			elif event.key == pygame.K_DOWN:
				ship.movingDown = True  
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.movingRight= False
			elif event.key == pygame.K_LEFT:
				ship.movingLeft = False
			elif event.key == pygame.K_UP:
				ship.movingUp = False
			elif event.key == pygame.K_DOWN:
				ship.movingDown = False
def update_screen(game_set, screen, ship):
	
	screen.fill(game_set.backgroundColor)
	ship.blitme()
	
	pygame.display.flip()

