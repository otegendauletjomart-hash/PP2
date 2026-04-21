class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.step = 20

    def move_left(self):
        if self.x - self.step >= self.radius:
            self.x -= self.step
        else:
            self.x = self.radius

    def move_right(self):
        if self.x + self.step <= self.screen_width - self.radius:
            self.x += self.step
        else:
            self.x = self.screen_width - self.radius

    def move_up(self):
        if self.y - self.step >= self.radius:
            self.y -= self.step
        else:
            self.y = self.radius

    def move_down(self):
        if self.y + self.step <= self.screen_height - self.radius:
            self.y += self.step
        else:
            self.y = self.screen_height - self.radius