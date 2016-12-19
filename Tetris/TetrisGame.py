from random import *
from Shapes import Shape
from Menu import Menu
import pygame
import sys

pygame.init()
size = width, height = 300, 440
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')
pygame.key.set_repeat(75)

class Area:

	def __init__(self, width, height, score):
		self.width = width
		self.height = height
		self.area = []
		self.lines_cleared = 0
		self.score = 0

		array_builder = []
		for row in range(int(self.height/20)):
			for column in range(int(self.width/20)):
				array_builder.append(0)
			self.area.append(array_builder)
			array_builder = []

	def matrix(self):
		return self.area

	def draw(self, shape, matrix, screen):
		self.check_state(shape, matrix)
		solid_color = (70,70,70)
		solid = pygame.image.load("outside.png").convert()
		solid.fill(solid_color,(1,1,18,18))
		for row, row_items in enumerate(matrix):
			for column, item in enumerate(row_items):
				x, y = column, row
				if item == 1:
					screen.blit(solid,(x*20, y*20))
	def drawbox(self, screen):
		border_color = (100,0,0)
		pygame.draw.rect(screen, border_color, (self.width + 2/3*2,0,2,self.height))
		pygame.draw.rect(screen, border_color, (self.width + 2/3*2,self.height/4,self.width,0))
		pygame.draw.rect(screen, border_color, (self.width + 2/3*2,self.height/4*3,self.width,0))
	
	def draw_next_shape(self,shape,screen):
		for index, item in enumerate(shape.x):
			screen.blit(shape.block, ((shape.x[index])*20, shape.y[index]*20))
	def check_state(self, shape, matrix):
		if shape.state == 1:
			for ind, i in enumerate(shape.x):
				if matrix[shape.y[ind]][shape.x[ind]] == 0:
					matrix[shape.y[ind]][shape.x[ind]] = 1
		
		old_lines_cleared = self.lines_cleared
		count = 0
		update_score = 0
		for row, row_items in enumerate(matrix):
			if sum(row_items) == 10:
				matrix.pop(row)
				matrix.reverse()
				matrix.append([0]*10)
				matrix.reverse()
				self.lines_cleared += 1
				count += 1
				update_score = 1
		
		if update_score == 1:
			self.score += (self.lines_cleared - old_lines_cleared) * count * 100

	def print_game_info(self, screen):
		myfont = pygame.font.SysFont("monospace", 16)
		font_color = (255,255,0)

		label_1 = myfont.render("Lines", 1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (250, self.height/8*7 - 20)

		label_2 = myfont.render("Cleared:", 1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (250, self.height/8*7)

		lines = myfont.render("%i" % self.lines_cleared, 1, font_color)
		lines_rect = lines.get_rect()
		lines_rect.center = (250, self.height/8*7 + 20)

		score_1 = myfont.render("Your", 1, font_color)
		score_1_rect = score_1.get_rect()
		score_1_rect.center = (250, self.height/2 - 20)

		score_2 = myfont.render("Score:", 1, font_color)
		score_2_rect = score_2.get_rect()
		score_2_rect.center = (250, self.height/2)

		score = myfont.render("%i" % self.score, 1, font_color)
		score_rect = score.get_rect()
		score_rect.center = (250, self.height/2 + 20)

		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(lines, lines_rect)

		screen.blit(score_1, score_1_rect)
		screen.blit(score_2, score_2_rect)
		screen.blit(score, score_rect)

class Gameover:
        
	def __init__(self, width, height, score):
		self.width = width
		self.height = height
		self._score = score
		self.pressContinue = 0

	def draw_Gameover(self,screen):
		font_color = (0,0,0)
		background_color = (255,255,255)
		pygame.draw.rect(screen, background_color, (0, 0, self.width, self.height), 0)
		
		tetris_font = pygame.font.Font("pdark.ttf",32)
		tetris_font.set_bold(1)
		
		label_1 = tetris_font.render("Game Over", 1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 150)
		
		tetris_font = pygame.font.SysFont("monospace", 32)
		tetris_font.set_bold(1)
		label_2 = tetris_font.render("Score:", 1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (150, 230)

		score = tetris_font.render("%i" % self._score, 1, font_color)
		score_rect = score.get_rect()
		score_rect.center = (150, 280)
		
		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(score, score_rect)

	def press_continue(self,screen):
		tetris_font = pygame.font.SysFont("monospace", 12)
		font_color = (0,0,0)
		
		label_1 = tetris_font.render("Press any button to continue",1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (150, 350)
		
		screen.blit(label_1, label_1_rect)

def check_input():
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				shape.rotate(area.matrix())
			if event.key == pygame.K_DOWN:
				shape.test_y(area.matrix())
				if shape.collision != 1:
					shape.move_down(area.matrix())
			if event.key == pygame.K_LEFT:
				shape.move_left(area.matrix())
			if event.key == pygame.K_RIGHT:
				shape.move_right(area.matrix())
			if event.key == pygame.K_SPACE:
				shape.test_y(area.matrix())
				while shape.collision != 1:
					shape.move_down(area.matrix())
					shape.draw_shape(area.matrix(), screen)
					area.draw(shape, area.matrix(), screen)
	return area

def menu_input():
	while not menu.gameStart:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_DOWN:
					menu.move_cursor(-1)
					menu.update_menu(screen)
					pygame.display.flip()
				
				if event.key == pygame.K_UP:
					menu.move_cursor(1)
					menu.update_menu(screen)
					pygame.display.flip()
		
				if event.key == pygame.K_RETURN:
					menu.gameStart=1	

#MAIN
while 1:
	area = Area(width - 100, height, 0)

	shape_queue = []	
	for i in range(5):
		shape_queue.append(randint(0,6))
	shape_color=(randint(1,255), randint(1,255), randint(1,255))

	shape = Shape(shape_color, shape_queue[0])

	gameOver=Gameover(width,height,area.score)

	screen.fill((255,255,255))
	area.drawbox(screen)
	menu=Menu(width,height)
	menu.draw_menu(screen)
	menu.update_menu(screen)
	pygame.display.flip()

	menu_input()
	init = 1000 
	start_time = pygame.time.get_ticks()
	
	while menu.singlePlayer and shape.game_state:
		check_input()
		time = pygame.time.get_ticks() - start_time
		if shape.state == 1:
			next_shape.deactivate()
			shape_queue.pop(0)
			shape_queue.append(randint(0,6))
			shape = Shape(shape_color,shape_queue[0], 0,5,0)
			shape_color=(randint(1,255), randint(1,255), randint(1,255))
		if init < time:			
			shape.move_down(area.matrix())
			init += 300
		screen.fill((0,0,0))
		shape.draw_shape(area.matrix(), screen)
		area.draw(shape, area.matrix(), screen)
		area.print_game_info(screen)
		next_shape = Shape(shape_color,shape_queue[1],0,12,0)
		next_shape.update_shape(area.matrix())
		area.draw_next_shape(next_shape,screen)
		area.drawbox(screen)
		pygame.display.flip()
		gameOver=Gameover(width,height,area.score)
		
	while menu.info and not menu.infoDone:
		menu.draw_info(screen)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				menu.infoDone=1
				
	while not menu.info and not gameOver.pressContinue:
		gameOver.draw_Gameover(screen)
		gameOver.press_continue(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				gameOver.pressContinue=1

# resets the game variables.
	menu.reset_game()
	
