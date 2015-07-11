import os, sys
import pygame
#import pygame.locals import *

if not pygame.font:
	print('Warning, fonts disabled')

FONT_PATH = "fonts/IndieFlower.ttf"

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

class App:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Far-More Shade')

		self.width = pygame.display.Info().current_w
		self.height = pygame.display.Info().current_h
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
		self.screenState = IntroScreen(self.screen)

	def MainLoop(self):
		while 1:
			self.screen.fill(COLOR_BLACK)

			for event in pygame.event.get():
				#Close button
				if event.type == pygame.QUIT:
					sys.exit()

				#Any key down
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()

				#Any mouse button down
				'''if event.type == pygame.MOUSEBUTTONDOWN:
					#whatever
					print('something')'''

			self.screenState.update()
			pygame.display.update()


class IntroScreen:
	def __init__(self, screen):
		self.screen = screen

		screenWidth = pygame.display.Info().current_w
		screenHeight = pygame.display.Info().current_h

		#Load resources and fonts
		self.bg = pygame.image.load('images/booth_main1_blur.jpg')
		self.bg = pygame.transform.scale(self.bg, (screenWidth, screenHeight))

		fontHeader = pygame.font.Font(FONT_PATH, 128)
		fontStart = pygame.font.Font(FONT_PATH, 64)

		#Header text
		self.textHeader = fontHeader.render('Far-More Shade', True, COLOR_WHITE)
		self.textHeaderBounds = self.textHeader.get_rect()
		self.textHeaderBounds.center = (screenWidth / 2, 200)

		#Pass Start text
		self.textStart = fontStart.render('Tap to Start', True, COLOR_WHITE)
		self.textStartBounds = self.textStart.get_rect()
		self.textStartBounds.center = (screenWidth / 2, screenHeight - 100)

		self.pulseScale = 1
		self.pulseScaleIsIncreasing = True

	def update(self):
		"""
		if self.pulseScaleIsIncreasing:
			self.pulseScale += 0.1
		#else:
			#self.pulseScale -= 0.1

		if self.pulseScale >= 1.2 and self.pulseScaleIsIncreasing:
			self.pulseScaleIsIncreasing = False
		if self.pulseScale <= 1 and not self.pulseScaleIsIncreasing:
			self.pulseScaleIsIncreasing = True
		#This will update later

		print(self.pulseScale)

		w,h = self.textStart.get_size()
		w = (int)(w * self.pulseScale)
		h = (int)(h * self.pulseScale)
		self.textStart = pygame.transform.scale(self.textStart, (w, h))"""

		self.screen.blit(self.bg, (0, 0))
		self.screen.blit(self.textHeader, self.textHeaderBounds)
		self.screen.blit(self.textStart, self.textStartBounds)
		#self.screen.blit(self.textStart, (10, 10))

if __name__ == "__main__":
	window = App()
	window.MainLoop()