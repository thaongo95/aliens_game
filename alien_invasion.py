import sys
import pygame
import time
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as funcs
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
	pygame.init()
	previousTime=time.time()
	
	game_settings=Settings()
	
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	ship = Ship(screen)
	#alien = Alien(game_settings, screen)
	aliens = Group()
	bullets = Group()
	
	stats = GameStats(game_settings)
	
	funcs.create_fleet(game_settings, screen, ship, aliens)
	pygame.display.set_caption("Alien Invasion")

	while True:
		print(time.time()-previousTime)
		
		funcs.check_events(game_settings, screen, ship, bullets)
		
		
		#bullets.update()
		if stats.game_active:
			ship.update_pos(game_settings)	
			funcs.update_bullets(game_settings, screen, ship, aliens, bullets)
			funcs.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
		
		funcs.update_screen(game_settings, screen, ship, aliens, bullets)
		
		previousTime=time.time()
		
run_game()
