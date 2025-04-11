import pygame as pg

class DamageText(pg.sprite.Sprite):
  def __init__(self, x, y, damage, colour):
    pg.sprite.Sprite.__init__(self)
    dmg_font = pg.font.Font("Assets/fonts/game_over.ttf", 42)
    self.image = dmg_font.render(damage, True, colour)
    self.rect = self.image.get_rect()
    self.rect.center = (x , y)
    self.counter = 0

  def update(self):
    #move text upwards
    self.rect.y -= 1
    self.counter += 1
    #vanish text
    if self.counter>20:
      self.kill()

class MenuScreen():
  def __init__(self):
    self.font = pg.font.Font("Assets/fonts/game_over.ttf", 120)
    self.small_font = pg.font.Font("Assets/fonts/game_over.ttf", 80)
    self.title = self.font.render("Battle of Odds", True, (0, 10, 84))
    self.tagline = self.small_font.render("A Turn-based game where anyone can win", True, (0, 10, 84))
    self.menu_bg = pg.image.load("Assets/bg.png")

  def mainmenu(self, surf):
    surf.blit(self.menu_bg, (0,0))
    surf.blit(self.title, ((surf.get_width()/2 - self.title.get_width()/2), 200))
    surf.blit(self.tagline, ((surf.get_width()/2 - self.tagline.get_width()/2), 270))

    play_txt = self.small_font.render("Press SPACE to play", True, (0, 10, 84))
    surf.blit(play_txt, ((surf.get_width()/2 - self.title.get_width()/2), 600))
    

  

