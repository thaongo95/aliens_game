import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('assets/space-shuttle.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.speed = 1
		self.movingRight = False
		self.movingLeft = False
		self.movingUp = Falses
		self.movingDown = False
	def update_pos(self):
		if self.movingRight:
			self.rect.centerx += self.speed 
		if self.movingLeft:
			self.rect.centerx -= self.speed 
		if self.movingUp:
			self.rect.centery -= self.speed 
		if self.movingDown:
			self.rect.centery += self.speed 
	def blitme(self):
		self.screen.blit(self.image, self.rect)
