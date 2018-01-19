# #objects
class objects_food:
	food = ['Water','Bread','Beer','Cheese','Mushrooms','Salt','Pepper','Potato','Oil','Tomato','Onion']
	

#images

import pygame
from pygame import *
def image_01():
	WIN_WIDTH = 640
	WIN_HEIGHT = 480
	DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
	bg = pygame.image.load('img_01.jpg')

	def main():
		pygame.init()
		screen = pygame.display.set_mode(DISPLAY)
		pygame.display.set_caption("SCP-087 - Лестница")
		

		while 1:
			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit
			screen.blit(bg, (0,0))
			pygame.display.update()
		

	if __name__ == "__main__":
			main()