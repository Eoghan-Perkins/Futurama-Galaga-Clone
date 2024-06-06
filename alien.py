import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class representing a single alien in the fleet"""

	def __init__(self, ai_game):
		"""Initialize the alien and it's starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image, set it's rect attribute
		self.image = pygame.image.load("project_pics/zoid.bmp")
		self.rect = self.image.get_rect()

		#Start each new alien near the top left of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store exact horizontal position of alien
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.moving_right = False
		self.moving_left = True
		self.moving_down = False
		self.moving_up = False

	def update(self):

		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):

		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
		
	# my work
	def my_update(self):
		
		self.counter = 0;
		while(self.counter < 100):
			if self.moving_left:
				self.x -= self.settings.alien_speed
				self.moving_left = False
				self.moving_up = True
				self.counter+=1
			elif self.moving_up:
				self.y -= self.settings.alien_speed
				self.moving_up = False
				self.moving_right = True
				self.counter+=1
			elif self.moving_right:
				self.x += self.settings.alien_speed
				self.moving_right = False
				self.moving_down = True
				self.counter+=1
			elif self.moving_down:
				self.y += self.settings.alien_speed
				self.moving_down = False
				self.moving_left = True
				self.counter+=1
		self.counter = 0
				
		self.rect.x = self.x
		self.rect.y = self.y

	def alien_blit(self):
		self.screen.blit(self.image, self.rect)