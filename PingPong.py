from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Ping Pong")


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
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 615:
            self.rect.x += self.speed



clock = time.Clock()
FPS = 60
game = True
finish = ""
while game:
    if finish != True:
        pass
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
