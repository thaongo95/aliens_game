import sys

from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

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
	elif event.key == pygame.K_q:
		sys.exit()
		
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
		
def update_bullets(game_settings, screen, ship, aliens, bullets):	
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(game_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(game_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens)==0:
		bullets.empty()
		create_fleet(game_settings, screen, ship, aliens)
	
def get_number_aliens_x(game_settings, alien_width):
	available_space_x = game_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
	available_space_y = (game_settings.screen_height - (8 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(game_settings, screen, aliens, alien_number, row_number):
	alien = Alien(game_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
		
def create_fleet(game_settings, screen, ship, aliens):
	alien = Alien(game_settings, screen)
	number_aliens_x= get_number_aliens_x(game_settings, alien.rect.width)
	number_rows =  get_number_rows( game_settings, ship.rect.height, alien.rect.height)	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(game_settings, screen, aliens, alien_number, row_number)
			
def check_fleet_edges(game_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(game_settings, aliens)
			break

def change_fleet_direction(game_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += game_settings.fleet_drop_speed
	game_settings.fleet_direction *= -1

def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
	if stats.ships_left > 0:
		stats.ships_left -=1
		aliens.empty()
		bullets.empty()
	
		create_fleet(game_settings, screen, ship, aliens)
		ship.center_ship()
	
		sleep(0.5)
	else:
		stats.game_active = False
		
def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(game_settings, stats, screen, ship, aliens, bullets)
			break
		
def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
	check_fleet_edges(game_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(game_settings, stats, screen, ship, aliens, bullets)
	check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)
	
def update_screen(game_settings, screen, ship, aliens, bullets):
	
	screen.fill(game_settings.backgroundColor)
	ship.blitme()
	#for alien in aliens:
		#alien.blitme()
	aliens.draw(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	pygame.display.flip()

