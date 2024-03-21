import sys
import pygame
import time
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as funcs
from pygame.sprite import Group
from alien import Alien

def run_game():
	pygame.init()
	previousTime=time.time()
	
	game_settings=Settings()
	
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	ship = Ship(screen)
	alien = Alien(game_settings, screen)
	aliens = Group()
	bullets = Group()
	
	funcs.create_fleet(game_settings, screen, ship, aliens)
	pygame.display.set_caption("Alien Invasion")

	
	
	while True:
		print(time.time()-previousTime)
		
		funcs.check_events(game_settings, screen, ship, bullets)
		
		ship.update_pos(game_settings)
		bullets.update()	
		
		funcs.update_bullets(bullets)
		
		funcs.update_screen(game_settings, screen, ship, aliens, bullets)
		
		previousTime=time.time()
		
run_game()
