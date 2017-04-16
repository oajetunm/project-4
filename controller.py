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


class Button:

	def __init__(self, text, rect):
		self.text = text
		self.rect = rect

	def draw(self, surface):
		pygame.draw.rect(surface, GRAY, self.rect)

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

	def on_click(self, event):
		print("button clicked")



class DataChangeButton(Button):

    def __init__(self, text, rect, chart):
        Button.__init__(self, text, rect)
        self.chart = chart
        self.sorted = False

    def on_click(self, event):
        # we will just toggle between sorted and unsorted data
        if (self.sorted):
            data = model.get_data()
            self.sorted = False
        else:
            data = model.get_sorted_data()
            self.sorted = True
        self.chart.set_values(data)


pygame.init()

screen = pygame.display.set_mode((900, 600))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

data = model.get_data()
screen_rect = screen.get_rect()
bc = view.BarChart(screen.get_rect(), values=data, ticks = 5)

button = DataChangeButton("Ascending",pygame.Rect(10, screen_rect.height - 70, 150, 60),bc)
button_1 = DataChangeButton("Descending",pygame.Rect(200, screen_rect.height - 70, 150, 60),bc)
button_2 = DataChangeButton("DEM",pygame.Rect(400, screen_rect.height - 70, 150, 60),bc)
button_2b = DataChangeButton("GOP",pygame.Rect(600, screen_rect.height - 70, 150, 60),bc)
button_3 = DataChangeButton("Raw",pygame.Rect(800, screen_rect.height - 70, 150, 60),bc)
button_4 = DataChangeButton("Percent",pygame.Rect(900, screen_rect.height - 70, 150, 60),bc)

# display loop
done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button.handle_event(event)
			button_1.handle_event(event)
			button_2.handle_event(event)
			button_2b.handle_event(event)
			button_3.handle_event(event)
			button_4.handle_event(event)

	bc.draw(screen)

	button.draw(screen)
	button_1.draw(screen)
	button_2.draw(screen)
	button_2b.draw(screen)
	button_3.draw(screen)
	button_4.draw(screen)

	pygame.display.update()
