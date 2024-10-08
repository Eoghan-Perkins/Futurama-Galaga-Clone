import pygame

class Ship:

	def __init__(self, ai_game):
		"""Initialize the ship and starting positiom"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		# Load in ship image and get its rect
		self.image = pygame.image.load('project_pics/Ship2.bmp')
		self.rect = self.image.get_rect()
		
		# Start each ship at screen bottom center
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's horizontal/vertical position(s)
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update ship's horizontal value"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			
		"""Update Ships' vertical value"""
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

