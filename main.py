import os, sys
import pygame
#import pygame.locals import *

if not pygame.font:
	print('Warning, fonts disabled')

FONT_PATH = "fonts/IndieFlower.ttf"

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

STATE_INTRO = 0
STATE_CATEGORY = 1
STATE_CATEOGRY_PATTERNS = 2
STATE_CATEOGYR_SHOP = 3
STATE_CATEGORY_THIRD = 4

DATA_DIR = "data/Categories"

class App:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Far-More Shade')

		self.width = pygame.display.Info().current_w
		self.height = pygame.display.Info().current_h
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
		self.setState(STATE_INTRO)
		#self.setState(STATE_CATEGORY)

	def setState(self, state):
			if(state == STATE_INTRO):
				self.screenState = IntroScreen(self)

			elif(state == STATE_CATEGORY):
				self.screenState = CategoryScreen(self)

			elif(state == STATE_CATEOGRY_PATTERNS):
				self.screenState = CategoryScreen(self, state)

			elif(state == STATE_CATEGORY_SHOP):
				self.screenState = CategoryScreen(self, state)

			elif(state == STATE_CATEGORY_THIRD):
				self.screenState = CategoryScreen(self, state)


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

				self.screenState.events(event)

			self.screenState.update()
			pygame.display.update()

class IntroScreen:
	def __init__(self, app):
		self.app = app
		self.screen = app.screen

		screenWidth = pygame.display.Info().current_w
		screenHeight = pygame.display.Info().current_h

		#Load resources and fonts
		self.bg = pygame.image.load('images/booth_main1_blur.jpg')
		self.bg = pygame.transform.scale(self.bg, (screenWidth, screenHeight))

		fontHeader = pygame.font.Font(FONT_PATH, 164)
		fontStart = pygame.font.Font(FONT_PATH, 46)

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

	def events(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.app.setState(STATE_CATEGORY)

class CategoryScreen:
	def __init__(self, app, category=STATE_CATEGORY):
		self.app = app
		self.screen = app.screen
		self.category = category
		self.screenWidth = pygame.display.Info().current_w
		self.screenHeight = pygame.display.Info().current_h

		#Load image resources
		self.bg = pygame.image.load('images/bg-repeat.png')

		#Setup titlebar
		self.titleBar = pygame.Surface((self.screenWidth, 100))
		self.titleBar.set_alpha(80)
		self.titleBar.fill((0, 0, 0))

		#Basic fonts and other vars
		fontBack = pygame.font.Font(FONT_PATH, 52)
		backButtonPadding = 30

		#Back button text
		self.backButtonText = fontBack.render('Back', True, COLOR_WHITE)
		self.backButtonTextBounds = self.backButtonText.get_rect()
		self.backButtonTextBounds.center = (
			(self.backButtonText.get_width() + backButtonPadding) / 2, 
			self.titleBar.get_height() / 2
		)

		#Back button rectangle
		self.backButton = pygame.Surface((
			self.backButtonText.get_width() + backButtonPadding,
			self.titleBar.get_height()
		))
		self.backButton.set_alpha(80)
		self.backButton.fill((0, 0, 0))

		if(self.category == STATE_CATEGORY):
			print(self.getCategories())

	def update(self):
		self.fillBackground()
		self.screen.blit(self.titleBar, (0, 0))
		self.screen.blit(self.backButton, (0, 0))
		self.screen.blit(self.backButtonText, self.backButtonTextBounds)

	def events(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if(self.backButton.get_rect().collidepoint(event.pos)):
				self.app.setState(STATE_INTRO)

	def fillBackground(self):
		bgWidth, bgHeight = self.bg.get_size()
		currentW = 0
		currentH = 0

		while currentH <= self.screenHeight:
			while currentW <= self.screenWidth:
				self.screen.blit(self.bg, (currentW, currentH))
				currentW += bgWidth
			currentH += bgHeight
			currentW = 0

	def getCategories(self):
		categories = []
		for name in os.listdir(DATA_DIR):
			if os.path.isdir(os.path.join(DATA_DIR, name)):
				categories.append(name)
		return categories



if __name__ == "__main__":
	window = App()
	window.MainLoop()