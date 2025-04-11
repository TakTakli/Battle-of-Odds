import pygame as pg, os, random
from effects import DamageText

damage_text_group = pg.sprite.Group()

class Entity():
  def __init__(self, name, x, y, total_hp, atk):
    self.name = name
    self.coords = x,y
    self.total_hp = total_hp
    self.hp = total_hp
    self.atk = atk
    self.alive = True
    self.update_time = pg.time.get_ticks()
    self.action = 0 
    self.frame = 0
    self.animations = [] #list containing all animations
    self.image = None
    self.rect = None

  def load_animation(self):
    anim_type = ''
    for i in range(4):
      if i == 0:
        anim_type = 'Idle'
      elif i==1:
        anim_type = 'Attack'
      elif i==2:
        anim_type = 'Hurt'
      else:
        anim_type = 'Die'
      temp = []
      for filename in os.listdir(f"Assets/{self.name}/{anim_type}"):
        img_file = os.path.join(f"Assets/{self.name}/{anim_type}", filename)
        if os.path.isfile(img_file):
          img = pg.image.load(img_file)
          img = pg.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
          temp.append(img)
      self.animations.append(temp)
    self.image = self.animations[self.action][self.frame]
    self.rect = self.image.get_rect()
    self.rect.center = self.coords

  def draw_img(self, surf):
    surf.blit(self.image, self.rect)

  def update(self):
    animation_cd = 100
    self.image = self.animations[self.action][self.frame]

    #checks if enough time has passed since the last update and frame is not the last death frame
    if pg.time.get_ticks() - self.update_time > animation_cd and self.image!= self.animations[3][len(self.animations[3])-1]:
      # if self.image == self.animations[1][self.frame]:
      #   if self.name == "Enemy":
        # self.rect.center = (self.coords[0]-100, self.coords[1])
      self.update_time = pg.time.get_ticks()
      self.frame +=1


    #resets animation to idle once complete
    if self.frame>=len(self.animations[self.action]) and self.action!=3:
      self.action = 0
      self.frame = 0
      self.update_time = pg.time.get_ticks()

    #if either dies
    if self.action == 3:
      self.frame == len(self.animations[self.action]) - 1
      return True

  def hurt(self):
    self.frame = 0
    self.action = 2
    self.update_time = pg.time.get_ticks()

  def die(self):
    self.frame = 0
    self.action = 3
    self.update_time = pg.time.get_ticks()


  def attack(self, target):

    dmg_increment = random.randint(-4, 4)
    dmg = self.atk + dmg_increment
    target.hp -= dmg
    target.hurt()
    dmg_txt = DamageText(target.rect.centerx, target.rect.y, str(dmg), (140, 0, 0))
    damage_text_group.add(dmg_txt)

    if target.hp < 1:
      target.hp = 0
      target.alive = False
      target.die()
    
    self.action = 1
    self.frame = 0
    self.update_time = pg.time.get_ticks()
    







    
    


      