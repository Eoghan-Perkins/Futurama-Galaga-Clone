class Settings:
	"""Class storing settings for Alien Game"""

	def __init__(self):
		# Inititialiozes game settings

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)

		# Ship settings
		self.ship_speed = 10.0

		# Bullet Settings
		self.bullet_speed = 15.0
		self.bullet_width = 2
		self.bullet_height = 15
		self.bullet_color = (238, 75, 43)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1