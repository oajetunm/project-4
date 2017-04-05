import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# a class to display a horizontal bar chart in pygame
class BarChart:

	# rect: a pygame.rect encoding size and position
	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=10, 
		plot_area_width_ratio=0.8, plot_area_height_ratio=0.8, bar_color=GREEN,
		max_val=0):
		pass


	def draw(self, surface):
		pass

# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000,700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data =	[
	 		("apples", 6), 
	 		("bananas", 7), 
 			("grapes", 4),
  			("pineapple", 1),
  			("cherries", 15)
        	]   

	# display using default values			
	bc = BarChart(values=data)

	data2 = [
			('Jenny', 80),
			('Stanley', 90),
			('Timothy', 92)
			]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0,400,800,150), 
		values=data2, 
		ticks=5, 
		plot_area_width_ratio=0.85, 
		plot_area_height_ratio=0.9, 
		bar_color=RED,
		max_val=100
		)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()	



