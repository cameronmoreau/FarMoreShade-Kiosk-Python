import os, sys
import pygame
#import pygame.locals import *

if not pygame.font:
	print('Warning, fonts disabled')

FONT_PATH = "fonts/IndieFlower.ttf"
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
		bg = pygame.image.load('images/booth_main1_blur.jpg')
		bg = pygame.transform.scale(bg, (screenWidth, screenHeight))

		fontHeader = pygame.font.Font(FONT_PATH, 64)
		fontStart = pygame.font.Font(FONT_PATH, 32)

		#Header text
		textHeader = fontHeader.render('Far-More Shade', True, COLOR_WHITE)
		textHeaderBounds = textHeader.get_rect()
		textHeaderBounds.center = (screenWidth / 2, screenHeight / 3)

		#Pass Start text
		self.textStart = fontStart.render('Tap to Start', True, COLOR_WHITE)
		self.textStartBounds = self.textStart.get_rect()
		self.textStartBounds.center = (screenWidth / 2, screenHeight - 100)
		
		#Draw bg and header text
		self.screen.blit(bg, (0, 0))
		self.screen.blit(textHeader, textHeaderBounds)

	def update(self):
		#This will update later
		self.screen.blit(self.textStart, self.textStartBounds)

if __name__ == "__main__":
	window = App()
	window.MainLoop()