import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class representing a single alien in the fleet"""

	def __init__(self, ai_game):
		"""Initialize the alien and it's starting position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image, set it's rect attribute
		self.image = pygame.image.load("project_pics/zoid.bmp")
		self.rect = self.image.get_rect()

		#Start each new alien near the top left of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store exact horizontal position of alien
		self.x = float(self.rect.x)