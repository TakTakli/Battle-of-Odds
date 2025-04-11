# !!! PLEASE INSTALL PYGAME BEFORE RUNNING THE FILE WITH "pip install pygame" !!!

#(! FOR VSCODE !) 
#IF PYGAME DOES NOT DETECT AFTER INSTALLATION, SET INTERPRETER PATH TO THE "Global" PATH (C:\Python{version}\python.exe) INSTEAD OF THE "Recommended" PATH 
#IF FileNotFound ERROR FOR ASSETS, PLEASE OPEN THE ROOT FOLDER AND RUN main.py FROM THERE

import pygame as pg, sys, csv
from entities import Entity
from entities import damage_text_group
from effects import MenuScreen

#set hp and atk from csv
hp_list = []
atk_list = []
with open("Assets/pokemon_data.csv") as csv_file:
  data = csv.DictReader(csv_file)
  for line in data:
    hp_list.append(int(line["HP"]))
    atk_list.append(int(line["Attack"]))

health = []
attack = []
for i in range(2):
  max_hp = max(hp_list)
  max_atk = atk_list[list.index(hp_list, max_hp)]
  
  health.append(max_hp)
  attack.append(max_atk)

  hp_list.remove(max_hp)

#initialise game
pg.init()
winsize = winw, winh = 1600, 900
window = pg.display.set_mode(winsize)
pg.display.set_caption("Battle of Odds")
clock = pg.time.Clock()

#load bg
bg = pg.image.load("Assets/bg.png")
tile = pg.image.load("Assets/tile.png")
grass = pg.image.load("Assets/grass.png")
panel = pg.image.load("Assets/panel.png")


def draw_assets():
  window.blit(bg, (0,0))
  window.blit(tile, (0,0))
  player.draw_img(window)
  witch.draw_img(window)
  window.blit(grass, (0,0))
  window.blit(panel, (0,0))
  window.blit(player_txt, (400 - (player_txt.get_width()/2), 800))
  window.blit(witch_txt, (1190 - (witch_txt.get_width()/2), 800))
  window.blit(tutorial_txt, (window.get_width()/2 - tutorial_txt.get_width()/2 , 780))

  #update hp text
  player_hptxt = hp_font.render(f"{player.hp}/{player.total_hp}", True, colour) 
  witch_hptxt = hp_font.render(f"{witch.hp}/{witch.total_hp}", True, colour)
  window.blit(player_hptxt, (400 - (player_txt.get_width()/2), 830))
  window.blit(witch_hptxt, (1190 - (witch_txt.get_width()/2), 830))

#create character instance
player = Entity("Player", 700, 635, health[0]-3, attack[0]-3)
witch = Entity("Enemy", 900, 645, health[1], attack[1]+2)
player.load_animation()
witch.load_animation()

#create text
font = pg.font.Font("Assets/fonts/game_over.ttf", 62)
colour = (0,10,84)
player_txt = font.render("Player", True, colour)
witch_txt = font.render("Witch", True, colour)
tutorial_txt = font.render("[ Hit SPACE to attack ]", True, colour)


hp_font = pg.font.Font("Assets/fonts/game_over.ttf", 54)


game_over = pg.font.Font("Assets/fonts/game_over.ttf", 120)
win_txt = game_over.render("You Won!", True, colour)
lose_txt = game_over.render("You Lost!", True, colour)

#game
def game_loop():
  pg.mixer.music.load("Assets/sounds/game_audio.mp3")
  pg.mixer.music.play(-1)
  attack = False
  current_fighter = 1
  total_fighters = 2
  action_cd = 0
  action_wait_time = 11
  while True:
    draw_assets()
    damage_text_group.draw(window)
    damage_text_group .update()

    #if player wins or loses
    if player.update() == True:
      window.blit(lose_txt, ((window.get_width()/2 - lose_txt.get_width()/2), 200))      
    if witch.update() == True:
      window.blit(win_txt, ((window.get_width()/2 - win_txt.get_width()/2), 200))


    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
          attack = True
      if event.type == pg.KEYUP:
        if event.key == pg.K_SPACE:
          attack = False

    
    if current_fighter == 1 and player.alive == True and attack == True:
      if witch.alive == True:
        player.attack(witch)
        atk_sound = pg.mixer.Sound("Assets/sounds/slash.mp3")
        atk_sound.play()
        current_fighter +=1
    
    if current_fighter == 2 and witch.alive == True:
      if player.alive == True:
        action_cd +=1
        if action_cd >= action_wait_time:
          witch.attack(player)
          matk_sound = pg.mixer.Sound("Assets/sounds/magic_atk.mp3")
          matk_sound.play()
          matk_sound.set_volume(0.5)
          current_fighter +=1
          action_cd = 0

    #resets once both characters have had their turns
    if current_fighter > total_fighters:
      current_fighter = 1



    clock.tick(60)
    pg.display.update()

run = True
game = MenuScreen()


#main game loop
pg.mixer.music.load("Assets/sounds/menu_screen.mp3")
pg.mixer.music.play(-1)
while run:
  game.mainmenu(window)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        space_hit = pg.mixer.Sound("Assets/sounds/start.mp3")
        space_hit.play()
        pg.mixer.music.stop()
        game_loop()
  clock.tick(60)
  pg.display.update()

  


  

