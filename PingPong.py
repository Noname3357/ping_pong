from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 405:
            self.rect.y += self.speed

bg_color = (150, 200, 255)
window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
window.fill(bg_color)

R_Player = Player("racket.png", 5, 140, 210, 15, 90)
L_Player = Player("racket.png", 5, 545, 210, 15, 90)

clock = time.Clock()
FPS = 60
game = True
finish = ""
while game:
    if finish != True:
        window.fill(bg_color)
        R_Player.reset()
        R_Player.update_r()
        L_Player.reset()
        L_Player.update_l()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
