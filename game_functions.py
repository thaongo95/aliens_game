import sys

import pygame
from bullet import Bullet

def check_event_keydown(event, game_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.movingRight= True
	elif event.key == pygame.K_LEFT:
		ship.movingLeft = True
	elif event.key == pygame.K_UP:
		ship.movingUp = True
	elif event.key == pygame.K_DOWN:
		ship.movingDown = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings, screen, ship, bullets)
		
def check_event_keyup(event, game_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.movingRight= False
	elif event.key == pygame.K_LEFT:
		ship.movingLeft = False
	elif event.key == pygame.K_UP:
		ship.movingUp = False
	elif event.key == pygame.K_DOWN:
		ship.movingDown = False
		
def check_events(game_settings, screen, ship, bullets):	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_event_keydown(event, game_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_event_keyup(event, game_settings, screen, ship, bullets)
			
def fire_bullet(game_settings, screen, ship, bullets):
	if len(bullets) < game_settings.bullet_allowed:
		new_bullet = Bullet(game_settings, screen, ship)
		bullets.add(new_bullet)
		
def update_bullets(bullets):	
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	
def update_screen(game_settings, screen, ship, bullets):
	
	screen.fill(game_settings.backgroundColor)
	ship.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	pygame.display.flip()

