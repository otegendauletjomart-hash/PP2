import pygame
import random
import time
from persistence import save_score

WIDTH, HEIGHT = 400, 600


# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        # границы
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# ================= ENEMY (КАК В ТВОЁМ КОДЕ) =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.speed = 8

        self.generate_random_rect()

    # 🔥 ВАЖНО: как в твоей версии
    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# ================= COIN =================
class Coin(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.weight = random.choice([1, 2, 3])

        self.spawn()

    def spawn(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, 4)

        if self.rect.top > HEIGHT:
            self.weight = random.choice([1, 2, 3])
            self.spawn()


# ================= GAME =================
class Game:
    def __init__(self, screen):
        self.screen = screen

        # assets
        self.bg = pygame.image.load("resources/AnimatedStreet.png")
        self.player_img = pygame.image.load("resources/Player.png")
        self.enemy_img = pygame.image.load("resources/Enemy.png")
        self.coin_img = pygame.transform.scale(
            pygame.image.load("resources/Coin.png"), (30, 30)
        )
        self.nitro_img = pygame.transform.scale(
            pygame.image.load("resources/nos.jpeg"), (30, 30)
)

        pygame.mixer.music.load("resources/background.wav")
        pygame.mixer.music.play(-1)

        self.crash = pygame.mixer.Sound("resources/crash.wav")

        self.font = pygame.font.SysFont("Verdana", 24)

        # player
        self.player = Player(self.player_img)

        # groups
        self.all = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.nitros = pygame.sprite.Group()
        self.all.add(self.player)

        # ================= СПАВН (КАК В ОРИГИНАЛЕ) =================
        self.enemy = Enemy(self.enemy_img)
        self.coin = Coin(self.coin_img)

        self.all.add(self.enemy, self.coin)
        self.enemies.add(self.enemy)
        self.coins.add(self.coin)

        self.score = 0
        self.coins_collected = 0
        self.distance = 0

        self.N = 5

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.bg, (0, 0))
    
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
            # ================= NITRO SPAWN =================
            if random.randint(1, 250) < 2:
                n = Nitro(self.nitro_img)
                self.all.add(n)
                self.nitros.add(n)

            # collision
            nitro_hits = pygame.sprite.spritecollide(self.player, self.nitros, True)

            for n in nitro_hits:
                self.player.speed = 10
                self.nitro_start = time.time()
                self.player.move()
            if hasattr(self, "nitro_start"):
                    if time.time() - self.nitro_start > 4:
                        self.player.speed = 5

            # ================= ДВИЖЕНИЕ =================
            for obj in self.all:
                obj.move()
                self.screen.blit(obj.image, obj.rect)

            if hasattr(self, "nitro_start"):
                if time.time() - self.nitro_start > 4:
                   self.player.speed = 5

            # ================= COIN COLLISION =================
            hits = pygame.sprite.spritecollide(self.player, self.coins, False)

            for c in hits:
                self.score += c.weight
                self.coins_collected += 1

                # respawn coin
                c.spawn()

                # difficulty
                if self.coins_collected % self.N == 0:
                    self.enemy.speed += 1

            # ================= ENEMY COLLISION =================
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.crash.play()
                time.sleep(1)
                running = False

            if hasattr(self, "nitro_start"):
                if time.time() - self.nitro_start > 4:
                    self.player.speed = 5   

            # ================= UI =================
            self.distance += 1

            score_text = self.font.render(f"Score: {self.score}", True, "black")
            coin_text = self.font.render(f"Coins: {self.coins_collected}", True, "black")
            dist_text = self.font.render(f"Dist: {self.distance}", True, "black")

            self.screen.blit(score_text, (10, 10))
            self.screen.blit(coin_text, (10, 40))
            self.screen.blit(dist_text, (10, 70))

            pygame.display.flip()
            clock.tick(60)

        save_score({
            "name": "Player",
            "score": self.score,
            "distance": self.distance
        })
class Nitro(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()

        self.spawn()
        self.timer = time.time()

    def spawn(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, 4)

        if time.time() - self.timer > 6:
            self.kill()