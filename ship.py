import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('assets/space-shuttle.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.movingRight = False
		self.movingLeft = False
		self.movingUp = False
		self.movingDown = False
		
	def update_pos(self, game_settings):
		if self.movingRight:
			self.rect.centerx = float(self.rect.centerx) + game_settings.move_speed 
		if self.movingLeft:
			self.rect.centerx = float(self.rect.centerx) - game_settings.move_speed 
		if self.movingUp:
			self.rect.centery = float(self.rect.centery) - game_settings.move_speed 
		if self.movingDown:
			self.rect.centery = float(self.rect.centery) + game_settings.move_speed 
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	def center_ship(self):
		self.center = self.screen_rect.centerx
