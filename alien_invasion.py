import sys
import pygame
import time
from settings import Settings
from ship import Ship
import game_functions as funcs

def run_game():
	pygame.init()
	previousTime=time.time()
	
	game_set=Settings()
	
	screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
	ship = Ship(screen)
	
	pygame.display.set_caption("Alien Invasion")

	
	
	while True:
		print(time.time()-previousTime)
		
		funcs.check_events(ship)
		ship.update_pos()
		funcs.update_screen(game_set, screen, ship)
		
		previousTime=time.time()
		
run_game()
