import pygame
from persistence import load_leaderboard, load_settings, save_settings


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 40)
        self.small = pygame.font.SysFont(None, 30)

        self.settings = load_settings()

        # меню пункты
        self.menu_items = ["PLAY", "LEADERBOARD", "SETTINGS", "QUIT"]
        self.index = 0

    # ================= MAIN MENU =================
    def run(self):
        while True:
            self.screen.fill("gray")

            title = self.font.render("RACER GAME", True, "black")
            self.screen.blit(title, (100, 120))

            # пункты меню
            for i, item in enumerate(self.menu_items):
                color = "yellow" if i == self.index else "white"
                text = self.small.render(item, True, color)
                self.screen.blit(text, (150, 220 + i * 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.KEYDOWN:

                    # вверх / вниз
                    if event.key == pygame.K_UP:
                        self.index = (self.index - 1) % len(self.menu_items)

                    if event.key == pygame.K_DOWN:
                        self.index = (self.index + 1) % len(self.menu_items)

                    # выбор
                    if event.key == pygame.K_RETURN:
                        return self.menu_items[self.index].lower()

            pygame.display.flip()

    # ================= LEADERBOARD =================
    def show_leaderboard(self):
        data = load_leaderboard()

        while True:
            self.screen.fill("black")

            title = self.font.render("LEADERBOARD", True, "white")
            self.screen.blit(title, (100, 50))

            y = 120
            for i, d in enumerate(data):
                text = self.small.render(
                    f"{i+1}. {d['name']} | {d['score']} | {d['distance']}",
                    True,
                    "white"
                )
                self.screen.blit(text, (50, y))
                y += 30

            back = self.small.render("ESC - BACK", True, "yellow")
            self.screen.blit(back, (120, 500))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    # ================= SETTINGS =================
    def settings_screen(self):
        options = ["sound", "color"]
        index = 0

        while True:
            self.screen.fill("darkblue")

            title = self.font.render("SETTINGS", True, "white")
            self.screen.blit(title, (120, 80))
            
            values = [
                str(self.settings["sound"]),
                self.settings["color"]
            ]

            for i, opt in enumerate(options):
                color = "yellow" if i == index else "white"
                text = self.small.render(
                    f"{opt}: {values[i]}",
                    True,
                    color
                )
                self.screen.blit(text, (80, 200 + i * 40))

            hint = self.small.render("ENTER change | ESC back", True, "yellow")
            self.screen.blit(hint, (70, 450))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        index = (index - 1) % len(options)

                    if event.key == pygame.K_DOWN:
                        index = (index + 1) % len(options)

                    if event.key == pygame.K_RETURN:
                        if options[index] == "sound":
                            self.settings["sound"] = not self.settings["sound"]

                        elif options[index] == "color":
                            self.settings["color"] = (
                                "red" if self.settings["color"] == "blue" else "blue"
                            )

                    if event.key == pygame.K_ESCAPE:
                        save_settings(self.settings)
                        return

            pygame.display.flip()