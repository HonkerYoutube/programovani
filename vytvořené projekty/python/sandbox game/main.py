import pygame
import elements

pygame.init()

window_x = 800
window_y = 900

window = pygame.display.set_mode((window_x, window_y))
running = True
display = pygame.display
mouse = pygame.mouse
mouse_pos = mouse.get_pos()
counter = 0

selected_element = "silicon"
category = ""
group = pygame.sprite.Group()

for value in elements.Elements:
    if value.values() == selected_element:
        category = "Metals"
        break
for value in elements.Elements:
    if value.values() == selected_element:
        category = "SemiMetals"
        break
for value in elements.Elements:
    if value.values() == selected_element:
        category = "NonMetals"
        break

class block(pygame.sprite.Sprite):
    def __init__(self, element, x, y, id):
        pygame.sprite.Sprite.__init__(self)

        self.element_values = {}
        for thing in elements.Elements:
            if thing.get("name") == element:
                self.element_values = thing

        self.size = 10
        self.color = self.element_values.get("color")
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.element = element
        self.melting_point = 0
        self.boiling_point = 0
        self.x = x
        self.y = y
        self.id = id
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)


        self.melting_point = self.element_values.get("melting point")
        self.boiling_point = self.element_values.get("boiling point")
        self.color = self.element_values.get("color")
    
    def calculate(self):
        self.y -= 25
    def draw(self, window):
        self.block_pos = [round(num, -1) for num in mouse.get_pos()]   # snap to grid
        print(self.block_pos)
        self.x, self.y = self.block_pos[0], self.block_pos[1]

        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    def update(self):
        self.calculate()
        self.draw(window)






def build_grid():
    for i1 in range(0, window_x, 10):
        for y1 in range(0, window_y, 10):
            # group.add((round(i1, -1), (round(y1, -1))))
            rect = pygame.Rect(i1, y1, i1 + 10, y1 + 10)
            pygame.draw.rect(window, (0, 40, 0), rect, 1)


while running:
    window.fill((0, 0, 0))
    build_grid()
    group.update()
    group.draw(window)

    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            group.add(block(selected_element, mouse_pos[0], mouse_pos[1], counter))
            group.draw(window)

            print(f"counter: {counter}")



    
    pygame.display.set_caption(f"sandbox")
    keys = pygame.key.get_pressed()

    display.flip()
