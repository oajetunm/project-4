import pygame
import view
import model

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
mv = 10000000


class Button:
	#chosen = True
	def __init__(self, text, rect):
		self.text = text
		self.rect = rect
		self.chosen = True

	def draw(self, surface, color = GRAY):
		pygame.draw.rect(surface, color, self.rect)

		font = pygame.font.Font(None, 20)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			(x, y) = pygame.mouse.get_pos()
			if x >= self.rect.x and \
				x <= self.rect.x + self.rect.width and \
				y >= self.rect.y and \
				y <= self.rect.y + self.rect.height:

				self.on_click(event)
	#
	def on_click(self, event):
		self.chosen = True

'''

class DataChangeButton(Button):
	def __init__(self, text, rect, chart):
		Button.__init__(self, text, rectt)
		self.chart = chart
		self.sorted = False
		# self.chosen = True
	def on_click(self, event):

		if (self.sorted):
			data = model.get_data()
			self.sorted = False
		else:
			data = model.get_sorted_data()
			self.sorted = True
		self.chart.set_values(data)
'''

party='dem'
raw=True
sort_ascending=True

pygame.init()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

screen_rect = screen.get_rect()

#data = model.get_data(party, raw , sort_ascending = sort_ascending)
#screen_rect = screen.get_rect()
# bc_rect =  pygame.Rect(screen_rect.x, screen_rect.y,
# 	screen_rect.width, screen_rect.height)
# bc = view.BarChart(bc_rect, plot_area_width_ratio =0.92 , plot_area_height_ratio =0.8,  values=data, ticks = 5, max_val = 10000000)

button = Button("dem", pygame.Rect(750,120,100,50))
button_gop = Button("gop", pygame.Rect(750,180,100,50))
button_up = Button("up",pygame.Rect(750,230,100,50))
button_down = Button("down", pygame.Rect(750,280,100,50))
button_raw = Button("raw",pygame.Rect(750,340,100,50))
button_percent = Button("%",pygame.Rect(750, 450,100,50))



# display loop
done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		else:
			button.handle_event(event)
			if button.chosen == True:
				b1c = view.RED
				b2c = view.GRAY

				party = "dem"
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = mv)
				button_gop.chosen = False
				#print("DEM Selected")

			button_gop.handle_event(event)
			if button_gop.chosen == True:
				b2c = view.RED
				b1c = view.GRAY
				party = "gop"
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = mv)
				button.chosen = False
				#print("GOP Selected")
			button_up.handle_event(event)
			if button_up.chosen == True:
				b3c = view.RED
				b4c = view.GRAY
				sort_ascending = True
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = mv)
				button_down.chosen = False
				#print("DEM Selected")

			button_down.handle_event(event)
			if button_down.chosen == True:
				b4c = view.RED
				b3c = view.GRAY
				sort_ascending = False
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = mv)
				button_up.chosen = False
				#print("GOP Selected")
			button_raw.handle_event(event)
			if button_raw.chosen == True:
				b5c = view.RED
				b6c = view.GRAY
				raw = True
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = mv)
				button_percent.chosen = False
				#print("DEM Selected")

			button_percent.handle_event(event)
			if button_percent.chosen == True:
				b6c = view.RED
				b5c = view.GRAY
				raw = False
				data = model.get_data(party =party, raw=raw, sort_ascending=sort_ascending)
				bc = view.BarChart(pygame.Rect(50,50,1000,600), values=data, ticks = 5, max_val = 1.0)
				button_raw.chosen = False


	bc.draw(screen)

	button.draw(screen, b1c)
	button_gop.draw(screen, b2c)
	button_up.draw(screen, b3c)
	button_down.draw(screen, b4c)
	button_raw.draw(screen, b5c)
	button_percent.draw(screen, b6c)


	pygame.display.update()

pygame.quit()
