import sys

import pygame

from ag_settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

	def __init__(self):
		"""Start Game, create required resources"""

		pygame.init()

		self.clock = pygame.time.Clock()

		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Fleshy headed mutant, are you friendly?")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main game loop"""

		while True:
			#Watch for keyboard and mouse events
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()
			self.clock.tick(60)
			

	def _check_events(self):
		"""Respond to key/mouse commands"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
	
	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""Create new bullet and add to bullet group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		# Update Bullet position
		self.bullets.update()

		# Delete old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		
		self._check_bullet_collisions()

	def _check_bullet_collisions(self):
		# Check for any bullets that have hit aliens
		# if true, remove alien and bullet
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		#create new fleet if aliens is empy
		if not self.aliens:
			"""Remove any existing bullets, restart fleet"""
			self.bullets.empty()
			self._create_fleet()

	def _check_fleet_edges(self):
		"""Check if any aliens in alien sprite group have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
	
	def _change_fleet_direction(self):
		"""Drop alien fleet and change direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _update_aliens(self):
		"""Check if any aliens are at screen edge; if so, update"""
		self._check_fleet_edges()
		self.aliens.update()

	def _create_fleet(self):
		"""Create the Alien Fleet"""
		# Make an Alien
		# Spacing between each alien is equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine number of rows of aliens that will fit on screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
			(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Create rows of aliens
		for row_number in range(number_rows):	
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		# Create an alien and place it in the row
		alien = Alien(self)
		alien_width , alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _update_screen(self):
		# Redraw the screen during each pass through the loop
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		# my work
		#for alien in self.aliens.sprites():
		#	alien.alien_blit()
	
		# Make most recently drawn screen visible.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run.
	ai = AlienInvasion()
	ai.run_game()