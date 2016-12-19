from random import *
import pygame


class Menu:
	"""
	Class to draw the menu and keep it updated
	
	Gives information to the main file for which
	screen to display and which game to play.
	"""
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.singlePlayer=1
		self.info=0
		self.gameStart=0
		self.infoDone=0
		self.tetris=0
	
	# draws the menu screen with the title and names
	def draw_menu(self,screen):
		font_color = (0,0,0)
		
		tetris_font = pygame.font.Font("pdark.ttf",32)
		tetris_font.set_bold(1)

		tetrisBG=(255*(1-self.tetris),255*(1-self.tetris),255*(1-self.tetris))
		tetrisFont=(255*self.tetris,255*self.tetris,255*self.tetris)
		pygame.draw.rect(screen, tetrisBG, (90,80,140,35),0)

		label_1 = tetris_font.render("TETRIS",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 100)
		
		tetris_font = pygame.font.SysFont("monospace", 10)
		
		screen.blit(label_1, label_1_rect)
	
        # how to play the game
	def draw_info(self,screen):
		background_color=(0,0,0)
		font_color = (255,255,255)

		tetris_font = pygame.font.Font("pdark.ttf",32)
		tetris_font.set_bold(1)

		pygame.draw.rect(screen, background_color, (0,0,self.width,self.height),0)
		
		label_1 = tetris_font.render("INFO",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 100)
		
		
		tetris_font = pygame.font.SysFont("monospace", 12)
		
		label_2 = tetris_font.render("1. Use AROW KEY",1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 150)
		
		label_7 = tetris_font.render("to play game.",1, font_color)
		label_7_rect = label_7.get_rect()
		label_7_rect.center = (150, 160)

		label_3 = tetris_font.render("Use UP arow key",1, font_color)
		label_3_rect = label_3.get_rect()
		label_3_rect.center = (150, 200)
		
		label_8 = tetris_font.render("to rotate the Shape.",1, font_color)
		label_8_rect = label_8.get_rect()
		label_8_rect.center = (150, 210)
		
		label_4 = tetris_font.render("SPACE BAR to drop the Shape immediately.",1, font_color)
		label_4_rect = label_4.get_rect()
		label_4_rect.center = (150, 260)
		
		tetris_font = pygame.font.SysFont("monospace", 10)
		label_5 = tetris_font.render("Score=(number of lines^2)*100",1, font_color)
		label_5_rect = label_5.get_rect()
		label_5_rect.center = (150, 300)
		
		label_6 = tetris_font.render("Press any key to continue",1, font_color)
		label_6_rect = label_6.get_rect()
		label_6_rect.center = (150, 350)
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(label_3, label_3_rect)
		screen.blit(label_4, label_4_rect)
		screen.blit(label_5, label_5_rect)
		screen.blit(label_6, label_6_rect)
		screen.blit(label_7, label_7_rect)
		screen.blit(label_8, label_8_rect)
		
	# updates the menu
	def update_menu(self,screen):
		
		tetris_font = pygame.font.Font("pdark.ttf",16)
		tetris_font.set_bold(0)
		
		singlePlayerBG=(255*(1-self.singlePlayer),255*(1-self.singlePlayer),255*(1-self.singlePlayer))
		infoBG=(255*(1-self.info),255*(1-self.info),255*(1-self.info))
		
		singlePlayerFont=(255*self.singlePlayer,255*self.singlePlayer,255*self.singlePlayer)
		infoFont=(255*self.info,255*self.info,255*self.info)
		
		
		pygame.draw.rect(screen, singlePlayerBG, (70,180,160,20),0)
		label_2 = tetris_font.render("Start Game",1, singlePlayerFont)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 190)

		pygame.draw.rect(screen, infoBG, (90,240,120,20),0)
		label_3 = tetris_font.render("Info",1, infoFont)
		label_3_rect = label_3.get_rect()
		label_3_rect.center = (150, 250)
		
		screen.blit(label_2, label_2_rect)
		screen.blit(label_3, label_3_rect)

	# function to switch the current selection on the menu screen
	def move_cursor(self,direction):
		if self.singlePlayer:
			if direction == 1:
				self.singlePlayer = 0
				self.info = 1
			elif direction == -1:
				self.singlePlayer = 0
				self.info = 1
		elif self.info:
			if direction == -1:
				self.singlePlayer = 1
				self.info = 0
			if direction == 1:
				self.singlePlayer = 1
				self.info = 0
				
	# reset game
	def reset_game(self):
		self.singlePlayer = 1
		self.info = 0
		self.gameStart = 0
		self.infoDone=0
