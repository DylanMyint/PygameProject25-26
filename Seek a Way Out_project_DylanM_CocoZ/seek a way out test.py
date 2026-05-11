from gamelib import *

#main program
game = Game(1000,800,"Seek a Way Out")
bk = Animation("images/crystalcave.png", 6, game, 9600/5, 2160/2, 2)
bk.resizeTo(game.width, game.height + 50)
game.setBackground(bk)

#functions
def positionObjects(object):
    for i in range(len(object)):   
        x = randint(50, 750)
        y = -randint(700, 2500)
        s = randint(3, 4)
        object[i].moveTo(x, y)
        object[i].setSpeed(s, 180)
        object[i].visible = True

def jumpingCollision1():
    global landed
    if not landed and not (Main.collidedWith(platform1,"rectangle") and
                           Main.collidedWith(platform4,"rectangle") and
                           Main.collidedWith(platform6,"rectangle") and
                           Main.collidedWith(platform5,"rectangle") and
                           Main.collidedWith(platform2,"rectangle") and
                           Main.collidedWith(platform3,"rectangle") and
                           Main.collidedWith(platform7,"rectangle") and
                           Main.collidedWith(platform8,"rectangle")):
        Main.y += 2
    if((Main.collidedWith(platform1,"rectangle") and Main.bottom < platform1.top + 15 and Main.right > platform1.left and Main.left< platform1.right)  or 
       (Main.collidedWith(platform4,"rectangle") and Main.bottom < platform4.top + 15 and Main.right > platform4.left and Main.left< platform4.right)  or 
       (Main.collidedWith(platform6,"rectangle") and Main.bottom < platform6.top + 15 and Main.right > platform6.left and Main.left< platform6.right)  or 
       (Main.collidedWith(platform5,"rectangle") and Main.bottom < platform5.top + 15 and Main.right > platform5.left and Main.left< platform5.right)  or 
       (Main.collidedWith(platform2,"rectangle") and Main.bottom < platform2.top + 15 and Main.right > platform2.left and Main.left< platform2.right)  or 
       (Main.collidedWith(platform3,"rectangle") and Main.bottom < platform3.top + 15 and Main.right > platform3.left and Main.left< platform3.right)  or 
       (Main.collidedWith(platform7,"rectangle") and Main.bottom < platform7.top + 15 and Main.right > platform7.left and Main.left< platform7.right)  or 
       (Main.collidedWith(platform8,"rectangle") and Main.bottom < platform8.top + 15 and Main.right > platform8.left and Main.left< platform8.right)):
        landed = True
    else:
        landed = False

def jumpingCollision2():
    global landed
    if not landed and not (Main.collidedWith(stone1_1,"rectangle") and
                           Main.collidedWith(stone1_2,"rectangle") and
                           Main.collidedWith(stone1_3,"rectangle") and
                           Main.collidedWith(stone1_4,"rectangle") and
                           Main.collidedWith(stone2_1,"rectangle") and
                           Main.collidedWith(stone2_2,"rectangle") and
                           Main.collidedWith(stone2_3,"rectangle") and
                           #Main.collidedWith(stone3_1,"rectangle") and
                           #Main.collidedWith(stone3_2,"rectangle") and
                           Main.collidedWith(stone3_2_2,"rectangle") and
                           Main.collidedWith(stone3_3,"rectangle") and
                           Main.collidedWith(stone4_1,"rectangle") and
                           Main.collidedWith(stone4_2,"rectangle") and
                           Main.collidedWith(stone5_1,"rectangle") and
                           #Main.collidedWith(stone5_2,"rectangle") and
                           Main.collidedWith(stone6_1,"rectangle") and
                           Main.collidedWith(stone6_2,"rectangle") and
                           Main.collidedWith(stone6_3,"rectangle") and
                           Main.collidedWith(stone7_1,"rectangle") and
                           Main.collidedWith(stone7_2,"rectangle") and
                           Main.collidedWith(stone7_3,"rectangle")):
        Main.y += 2
    if((Main.collidedWith(stone1_1,"rectangle") and Main.bottom < stone1_1.top + 15 and Main.right > stone1_1.left and Main.left< stone1_1.right)  or 
       (Main.collidedWith(stone1_2,"rectangle") and Main.bottom < stone1_2.top + 15 and Main.right > stone1_2.left and Main.left< stone1_2.right)  or 
       (Main.collidedWith(stone1_3,"rectangle") and Main.bottom < stone1_3.top + 15 and Main.right > stone1_3.left and Main.left< stone1_3.right)  or 
       (Main.collidedWith(stone1_4,"rectangle") and Main.bottom < stone1_4.top + 15 and Main.right > stone1_4.left and Main.left< stone1_4.right)  or 
       (Main.collidedWith(stone2_1,"rectangle") and Main.bottom < stone2_1.top + 15 and Main.right > stone2_1.left and Main.left< stone2_1.right)  or 
       (Main.collidedWith(stone2_2,"rectangle") and Main.bottom < stone2_2.top + 15 and Main.right > stone2_2.left and Main.left< stone2_2.right)  or 
       (Main.collidedWith(stone2_3,"rectangle") and Main.bottom < stone2_3.top + 15 and Main.right > stone2_3.left and Main.left< stone2_3.right)  or
       #(Main.collidedWith(stone3_1,"rectangle") and Main.bottom < stone3_1.top + 15 and Main.right > stone3_1.left and Main.left< stone3_1.right)  or 
       #(Main.collidedWith(stone3_2,"rectangle") and Main.bottom < stone3_2.top + 15 and Main.right > stone3_2.left and Main.left< stone3_2.right)  or
       (Main.collidedWith(stone3_2_2,"rectangle") and Main.bottom < stone3_2.top + 15 and Main.right > stone3_2.left and Main.left< stone3_2.right)  or
       (Main.collidedWith(stone3_3,"rectangle") and Main.bottom < stone3_3.top + 15 and Main.right > stone3_3.left and Main.left< stone3_3.right)  or 
       (Main.collidedWith(stone4_1,"rectangle") and Main.bottom < stone4_1.top + 15 and Main.right > stone4_1.left and Main.left< stone4_1.right)  or 
       (Main.collidedWith(stone4_2,"rectangle") and Main.bottom < stone4_2.top + 15 and Main.right > stone4_2.left and Main.left< stone4_2.right)  or 
       (Main.collidedWith(stone5_1,"rectangle") and Main.bottom < stone5_1.top + 15 and Main.right > stone5_1.left and Main.left< stone5_1.right)  or 
       #(Main.collidedWith(stone5_2,"rectangle") and Main.bottom < stone5_2.top + 15 and Main.right > stone5_2.left and Main.left< stone5_2.right)  or
       (Main.collidedWith(stone6_1,"rectangle") and Main.bottom < stone6_1.top + 15 and Main.right > stone6_1.left and Main.left< stone6_1.right)  or 
       (Main.collidedWith(stone6_2,"rectangle") and Main.bottom < stone6_2.top + 15 and Main.right > stone6_2.left and Main.left< stone6_2.right)  or 
       (Main.collidedWith(stone6_3,"rectangle") and Main.bottom < stone6_3.top + 15 and Main.right > stone6_3.left and Main.left< stone6_3.right)  or 
       (Main.collidedWith(stone7_1,"rectangle") and Main.bottom < stone7_1.top + 15 and Main.right > stone7_1.left and Main.left< stone7_1.right)  or 
       (Main.collidedWith(stone7_2,"rectangle") and Main.bottom < stone7_2.top + 15 and Main.right > stone7_2.left and Main.left< stone7_2.right)  or 
       (Main.collidedWith(stone7_3,"rectangle") and Main.bottom < stone7_3.top + 15 and Main.right > stone7_3.left and Main.left< stone7_3.right)):
        landed = True
    else:
        landed = False
        
def waterfallCollisions1():
    global landed
    if (Main.collidedWith(waterfallcollisionbox1_1, "rectangle")) and (Main.collidedWith(waterfallcollisionbox1_2, "rectangle")):
        Main.moveTo(waterfallcollisionbox1_2.x, waterfallcollisionbox1_2.y + 30)

def waterfallCollisions2():
    global landed
    if (Main.collidedWith(waterfallcollisionbox2_1, "rectangle")) and (Main.collidedWith(waterfallcollisionbox2_2, "rectangle")):
        Main.moveTo(waterfallcollisionbox2_2.x, waterfallcollisionbox2_2.y + 50)

def jumpingCollision3():
    global landed
    if not landed and not (Main.collidedWith(lava1,"rectangle") and
                           Main.collidedWith(lava2,"rectangle") and
                           Main.collidedWith(lava4,"rectangle") and
                           Main.collidedWith(lava6_2,"rectangle") and
                           Main.collidedWith(lava6,"rectangle") and
                           Main.collidedWith(lava9_2,"rectangle") and
                           Main.collidedWith(lava9,"rectangle") and
                           Main.collidedWith(lava10_2,"rectangle") and
                           Main.collidedWith(lava10,"rectangle") and
                           Main.collidedWith(lava11_2,"rectangle") and
                           Main.collidedWith(lava11,"rectangle")):
        Main.y += 2
    if((Main.collidedWith(lava1,"rectangle") and Main.bottom < lava1.top + 15 and Main.right > lava1.left and Main.left< lava1.right)  or 
       (Main.collidedWith(lava2,"rectangle") and Main.bottom < lava2.top + 15 and Main.right > lava2.left and Main.left< lava2.right)  or 
       (Main.collidedWith(lava4,"rectangle") and Main.bottom < lava4.top + 15 and Main.right > lava4.left and Main.left< lava4.right)  or 
       (Main.collidedWith(lava6_2,"rectangle") and Main.bottom < lava6_2.top + 15 and Main.right > lava6_2.left and Main.left< lava6_2.right)  or 
       (Main.collidedWith(lava6,"rectangle") and Main.bottom < lava6.top + 15 and Main.right > lava6.left and Main.left< lava6.right)  or 
       (Main.collidedWith(lava9_2,"rectangle") and Main.bottom < lava9_2.top + 15 and Main.right > lava9_2.left and Main.left< lava9_2.right)  or 
       (Main.collidedWith(lava9,"rectangle") and Main.bottom < lava9.top + 15 and Main.right > lava9.left and Main.left< lava9.right)  or 
       (Main.collidedWith(lava10_2,"rectangle") and Main.bottom < lava10_2.top + 15 and Main.right > lava10_2.left and Main.left< lava10_2.right)  or 
       (Main.collidedWith(lava10,"rectangle") and Main.bottom < lava10.top + 15 and Main.right > lava10.left and Main.left< lava10.right)  or 
       (Main.collidedWith(lava11_2,"rectangle") and Main.bottom < lava11_2.top + 15 and Main.right > lava11_2.left and Main.left< lava11_2.right)  or 
       (Main.collidedWith(lava11,"rectangle") and Main.bottom < lava11.top + 15 and Main.right > lava11.left and Main.left< lava11.right)):
        landed = True
    else:
        landed = False

def flame_collision():
    if Main.collidedWith(flame):
        Main.health -= 1
    if Main.collidedWith(flame2):
        Main.health -= 1
    if Main.collidedWith(flame3):
        Main.health -= 1
    if Main.collidedWith(flame4):
        Main.health -= 1
    if Main.collidedWith(flame5):
        Main.health -= 1
        
#start screen image
title = Image("images/seekawayout.png", game)
title.y = 100

story = Image("images/story.png", game)
story.y = 350
story_off = Image("images/story.png", game)
story_on = Image("images/story2.png", game)

storyText = Image("images/storytext.png", game)
storyText.visible = False
storyText.resizeTo(game.width, game.height)

play = Image("images/play.png", game)
play.y = 650
play_off = Image("images/play.png", game)
play_on = Image("images/play2.png", game)

howtoplay = Image("images/howtoplay.png", game)
howtoplay.y = 500
howtoplay_off = Image("images/howtoplay.png", game)
howtoplay_on = Image("images/howtoplay2.png", game)

howtoText = Image("images/howtotext.png", game)
howtoText.visible = False
howtoText.resizeTo(game.width, game.height) 


#end screen image
gameover = Image ("images/gameover.png", game)
gameover.resizeBy(50)
gameover.y = 100

youdied = Image ("images/youdied.png", game)
youdied.resizeBy(40)
youdied.y = 400

gameexit = Image ("images/exit.png", game)
gameexit.resizeBy(-50)
gameexit.y = 600

gameexit2 = Image ("images/exit2.png", game)
gameexit2.resizeBy(-50)
gameexit2.y = 600


youwon = Image ("images/youwon.png", game)
youwon.resizeBy(50)
youwon.y = 100

gameplay = Image ("images/gameplay.png", game)
gameplay.resizeBy(-20)
gameplay.y = 400

 
#stone platforms
stone1 = Image("images/stoneplat1.png", game)
stone1.collisionBorder = "rectangle"
stone1.moveTo(400, 250)
stone1_1 = Image("images/stoneplat1/stoneplat1-1.png", game)
#stone1_1.collisionBorder = "rectangle"
stone1_1.moveTo(270, 272)
stone1_2 = Image("images/stoneplat1/stoneplat1-2.png", game)
#stone1_2.collisionBorder = "rectangle"
stone1_2.moveTo(350, 256)
stone1_3 = Image("images/stoneplat1/stoneplat1-3.png", game)
#stone1_3.collisionBorder = "rectangle"
stone1_3.resizeBy(5)
stone1_3.moveTo(420, 272)
stone1_4 = Image("images/stoneplat1/stoneplat1-4.png", game)
#stone1_4.collisionBorder = "rectangle"
stone1_4.resizeBy(5)
stone1_4.moveTo(523, 262)

stone2 = Image("images/stoneplat2.png", game)
stone2.collisionBorder = "rectangle"
stone2.moveTo(750, 410)
stone2_1 = Image("images/stoneplat2/stoneplat2-1.png", game)
#stone2_1.collisionBorder = "rectangle"
stone2_1.moveTo(662, 410)
stone2_2 = Image("images/stoneplat2/stoneplat2-2.png", game)
#stone2_2.collisionBorder = "rectangle"
stone2_2.moveTo(768, 424)
stone2_3 = Image("images/stoneplat2/stoneplat2-3.png", game)
#stone2_3.collisionBorder = "rectangle"
stone2_3.resizeBy(5)
stone2_3.moveTo(850, 418)


stone3 = Image("images/stoneplat3.png", game)
stone3.collisionBorder = "rectangle"
stone3.moveTo(500, 550)
stone3_1 = Image("images/stoneplat3/stoneplat3-1.png", game)
stone3_1.collisionBorder = "rectangle"
stone3_1.resizeBy(7.5)
stone3_1.moveTo(410, 542)
stone3_2 = Image("images/stoneplat3/stoneplat3-2.png", game)
stone3_2.collisionBorder = "rectangle"
stone3_2.moveTo(500, 557)
stone3_2_2 = Image("images/stoneplat3/stoneplat3-2-2.png", game)
#stone3_2_2.collisionBorder = "rectangle"
stone3_2_2.moveTo(547, 557)
stone3_3 = Image("images/stoneplat3/stoneplat3-3.png", game)
#stone3_3.collisionBorder = "rectangle"
stone3_3.resizeBy(5)
stone3_3.moveTo(590, 541)

stone4 = Image("images/stoneplat4.png", game)
stone4.collisionBorder = "rectangle"
stone4.moveTo(800, 650)
stone4_1 = Image("images/stoneplat4/stoneplat4-1.png", game)
#stone4_1.collisionBorder = "rectangle"
stone4_1.moveTo(773, 674)
stone4_2 = Image("images/stoneplat4/stoneplat4-2.png", game)
#stone4_2.collisionBorder = "rectangle"
stone4_2.resizeBy(5)
stone4_2.moveTo(865, 659)

stone5 = Image("images/stoneplat5.png", game)
stone5.collisionBorder = "rectangle"
stone5.moveTo(500, 410)
stone5_1 = Image("images/stoneplat5/stoneplat5-1.png", game)
#stone5_1.collisionBorder = "rectangle"
stone5_1.moveTo(493, 422)
stone5_2 = Image("images/stoneplat5/stoneplat5-2.png", game)
#stone5_2.collisionBorder = "rectangle"
stone5_2.resizeBy(6.5)
stone5_2.moveTo(565, 417)

stone6 = Image("images/stoneplat6.png", game)
stone6.collisionBorder = "rectangle"
stone6.moveTo(200, 400)
stone6_1 = Image("images/stoneplat6/stoneplat6-1.png", game)
#stone6_1.collisionBorder = "rectangle"
#stone6_1.resizeBy(7.5)
stone6_1.moveTo(121, 405)
stone6_2 = Image("images/stoneplat6/stoneplat6-2.png", game)
#stone6_2.collisionBorder = "rectangle"
stone6_2.moveTo(228, 418)
stone6_3 = Image("images/stoneplat6/stoneplat6-3.png", game)
#stone6_3.collisionBorder = "rectangle"
stone6_3.resizeBy(5)
stone6_3.moveTo(302, 423)

stone7 = Image("images/stoneplat6.png", game)
stone7.collisionBorder = "rectangle"
stone7.moveTo(760, 155)
stone7_1 = Image("images/stoneplat6/stoneplat6-1.png", game)
#stone7_1.collisionBorder = "rectangle"
#stone7_1.resizeBy(7.5)
stone7_1.moveTo(691, 160)
stone7_2 = Image("images/stoneplat6/stoneplat6-2.png", game)
#stone7_2.collisionBorder = "rectangle"
stone7_2.moveTo(798, 173)
stone7_3 = Image("images/stoneplat6/stoneplat6-3.png", game)
#stone7_3.collisionBorder = "rectangle"
stone7_3.resizeBy(5)
stone7_3.moveTo(872, 178)

#level 2 gif
waterfall = Animation("images/waterfall1.png", 8, game, 2055/5, 1024/2, 2)
waterfall.resizeBy(-50)
#waterfall.collisionBorder = "rectangle"
waterfall.moveTo(400, 470)

waterfallcollisionbox1_1 = Image("images/stoneplat4/stoneplat4-2.png", game)
#waterfallcollisionbox1_1.collisionBorder = "rectangle"
waterfallcollisionbox1_1.resizeBy(60)
waterfallcollisionbox1_1.moveTo(400, 450)
waterfallcollisionbox1_2 = Image("images/stoneplat4/stoneplat4-2.png", game)
#waterfallcollisionbox1_2.collisionBorder = "rectangle"
waterfallcollisionbox1_2.resizeBy(60)
waterfallcollisionbox1_2.moveTo(400, 530)

waterfall2 = Animation("images/waterfall2.png", 8, game, 1345/5, 1024/2, 2)
waterfall2.resizeBy(-55)
#waterfall2.collisionBorder = "rectangle"
waterfall2.moveTo(600, 200)

waterfallcollisionbox2_1 = Image("images/stoneplat4/stoneplat4-2.png", game)
#waterfallcollisionbox2_1.collisionBorder = "rectangle"
waterfallcollisionbox2_1.resizeBy(-28)
waterfallcollisionbox2_1.moveTo(597, 210)
waterfallcollisionbox2_2 = Image("images/stoneplat4/stoneplat4-2.png", game)
#waterfallcollisionbox2_2.collisionBorder = "rectangle"
waterfallcollisionbox2_2.resizeBy(-28)
waterfallcollisionbox2_2.moveTo(597, 240)

#platforms
platform1 = Image("images/platform(1).png", game)
platform1.resizeBy(-50)
#platform1.collisionBorder = "rectangle"
platform1.moveTo(125, 240)

platform2 = Image("images/platform(2).png", game)
platform2.resizeBy(-50)
#platform2.collisionBorder = "rectangle"
platform2.moveTo(365, 355)

platform3 = Image("images/platform(3).png", game)
platform3.resizeBy(-50)
#platform3.collisionBorder = "rectangle"
platform3.moveTo(145, 350)

platform4 = Image("images/platform(4).png", game)
platform4.resizeBy(-50)
#platform4.collisionBorder = "rectangle"
platform4.moveTo(400, 150)

platform5 = Image("images/platform(5).png", game)
platform5.resizeBy(-50)
#platform5.collisionBorder = "rectangle"
platform5.moveTo(550, 350)

platform6 = Image("images/platform(6).png", game)
platform6.resizeBy(-50)
#platform6.collisionBorder = "rectangle"
platform6.moveTo(700, 415)

platform7 = Image("images/platform(7).png", game)
platform7.resizeBy(-50)
#platform7.collisionBorder = "rectangle"
platform7.moveTo(795, 525)

platform8 = Image("images/platform(8).png", game)
platform8.resizeBy(-50)
platform8.moveTo(470, 605)

#crystal
crystal1 = Image("images/crystal1.png", game)
crystal1.moveTo(340, 550)
crystal1.resizeBy(-20)

crystal2 = Image("images/crystal2.png", game)
crystal2.moveTo(850, 480)
crystal2.resizeBy(-20)

crystal3 = Image("images/crystal3.png", game)
crystal3.moveTo(125, 310)
crystal3.resizeBy(-20)

crystal4 = Image("images/crystal4.png", game)
crystal4.moveTo(600, 310)
crystal4.resizeBy(-20)

#lava platforms

#short lava tile 
lava1 = Image("images/lavaplat1.png", game)
lava1.resizeBy(50)
lava1.moveTo(150, 650)

lava2 = Image("images/lavaplat2.png", game)
lava2.resizeBy(50)
lava2.moveTo(150, 250)

#lava3 = Image("images/lavaplat3.png", game)
#lava3.resizeBy(50)
#lava3.moveTo(700, 250)

lava4 = Image("images/lavaplat4.png", game)
lava4.resizeBy(50)
lava4.moveTo(850, 450)

#lava5 = Image("images/lavaplat5.png", game)
#lava5.resizeBy(50)
#lava5.moveTo(400, 250)

#long lava tile 
lava6 = Image("images/lavaplat6.png", game)
lava6.resizeBy(80)
lava6.moveTo(400, 750)

lava6_2 = Image("images/lavaplat6 - 2.png", game)
lava6_2.resizeBy(80)
lava6_2.moveTo(600, 750)
#long lava tile 

#lava7 = Image("images/lavaplat7.png", game)
#lava7.resizeBy(50)
#lava7.moveTo(700, 550)

#lava8 = Image("images/lavaplat8.png", game)
#lava8.resizeBy(50)
#lava8.moveTo(700, 550)

#long lava tile 
lava9 = Image("images/lavaplat9.png", game)
lava9.resizeBy(80)
lava9.moveTo(400, 550)

lava9_2 = Image("images/lavaplat9 - 2.png", game)
lava9_2.resizeBy(80)
lava9_2.moveTo(600, 550)

lava10 = Image("images/lavaplat10.png", game)
lava10.resizeBy(80)
lava10.moveTo(400, 350)

lava10_2 = Image("images/lavaplat10 - 2.png", game)
lava10_2.resizeBy(80)
lava10_2.moveTo(600, 350)

lava11 = Image("images/lavaplat11.png", game)
lava11.resizeBy(80)
lava11.moveTo(400, 150)

lava11_2 = Image("images/lavaplat11 - 2.png", game)
lava11_2.resizeBy(80)
lava11_2.moveTo(600, 150)

#level 3 gif
risinglava = Animation("images/lava.png", 3, game, 2723/3, 564, 3)
risinglava.resizeBy(15)
#risinglava.collisionBorder = "rectangle"
risinglava.y = 1200
risinglava.setSpeed(.49, 360)

flame = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
#flame.collisionBorder = "rectangle"
flame.resizeBy(-40)
flame.moveTo(550, 700)

flame2 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
#flame2.collisionBorder = "rectangle"
flame2.resizeBy(-40)
flame2.moveTo(300, 500)

flame3 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
#flame3.collisionBorder = "rectangle"
flame3.resizeBy(-40)
flame3.moveTo(600, 305)

flame4 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
#flame4.collisionBorder = "rectangle"
flame4.resizeBy(-40)
flame4.moveTo(370, 305)

flame5 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
#flame5.collisionBorder = "rectangle"
flame5.resizeBy(-40)
flame5.moveTo(700, 500)

ladder = Image("images/ladder.png", game)
ladder.resizeBy(-20)
ladder.moveTo(lava11_2.x + 65, lava11_2.y - 120)

#player sprites
Main = Animation("images/Pink_Monster_Idle_4.png", 4, game, 128/4, 32, 3)
Main.resizeBy(100)
#Main.collisionBorder = "rectangle"
Main.moveTo(platform8.x, platform8.y - 50)
Main_idle = Animation("images/Pink_Monster_Idle_4.png", 4, game, 128/4, 32, 3)
Main_idle.resizeBy(100)
#Main_idle.collisionBorder = "rectangle"
Main_walk = Animation("images/Pink_Monster_Walk_6.png", 6, game, 192/6, 32, 5)
Main_walk.resizeBy(100)
Main_hurt = Animation("images/Pink_Monster_Hurt_4.png", 4, game, 128/4, 32, 3)
Main_hurt.resizeBy(100)
Main_jump = Animation("images/Pink_Monster_Jump_8.png", 8, game, 256/8, 32, 3)
Main_jump.resizeBy(100)
Main_death = Animation("images/Pink_Monster_Death_8.png", 8, game, 256/8, 32, 3)
Main_death.resizeBy(100)

Friend1 = Animation("images/Owlet_Monster_Idle_4.png", 4, game, 128/4, 32, 3)
Friend1.resizeBy(100)
#Friend1.collisionBorder = "rectangle"
Friend1.moveTo(platform4.x + 83, platform4.y - 53)

#lists
stalactites = []
for i in range(55):
    stalactite = Image("images/stalactites.png", game)
    stalactite.resizeBy(-90)
    stalactites.append(stalactite)
positionObjects(stalactites)

jumping = False
landed = False
factor = 1

startbk = Image("images/startscreenbk.webp", game)
startbk.resizeTo(game.width, game.height)
game.setBackground(startbk)

#start screen
while not game.over:
    game.processInput()
    
    startbk.draw()
    title.draw()
    story.draw()
    play.draw()
    howtoplay.draw()
    storyText.draw()
    howtoText.draw()


    if mouse.collidedWith(story, "rectangle"):
        story.setImage(story_on.image)
    else:
        story.setImage(story_off.image)


    if mouse.collidedWith(play, "rectangle"):
        play.setImage(play_on.image)
    else:
        play.setImage(play_off.image)

    if mouse.collidedWith(howtoplay, "rectangle"):
        howtoplay.setImage(howtoplay_on.image)
    else:
        howtoplay.setImage(howtoplay_off.image)


    if mouse.collidedWith(story,"rectangle") and mouse.LeftClick:
        storyText.visible = True

    if mouse.collidedWith(howtoplay,"rectangle") and mouse.LeftClick:
        howtoText.visible = True

    if keys.Pressed[K_SPACE]:
        storyText.visible = False
        howtoText.visible = False


    if mouse.collidedWith(play, "rectangle") and mouse.LeftClick:
       game.over = True

    game.update(30)
game.over = False


healthbar = Shape("bar", game, Main.health, 10, green)

Main.health = 100

#level 1
while not game.over:
    game.processInput()

    bk.draw()
    crystal1.draw()
    crystal2.draw()
    crystal3.draw()
    crystal4.draw()
    platform1.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    platform5.draw()
    platform6.draw()
    platform7.draw()
    platform8.draw()
    Main.draw()
    Friend1.draw()
    Friend1.flipV = True
    
    if keys.Pressed[K_d]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main = Main_walk
        Main.x += 2
        #Main.offsetX = -25
        Main.flipV = False
        Main_idle.flipV = False
    elif keys.Pressed[K_a]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main.flipV = True
        Main_idle.flipV = True
        Main = Main_walk
        Main.x -= 2
        #Main.offsetX = -75
    else:
        Main_idle.visible = True
        Main = Main_idle
        '''
        if Main.flipV:
            Main.offsetX = -100
        else:
            Main.offsetX = 0
        '''
    #print(landed, jumping, keys.Pressed[K_w])
    
    if keys.Pressed[K_w] and landed and not jumping:
        #Main.images = Main_jump.images
        jumping = True
        
    if jumping:
        jumping = True
        landed = False
        Main.y -= 10 * factor
        factor *= .96
        if factor < 0.1:
            jumping = False
            factor = 1


    jumpingCollision1()
    
    for i in range(len(stalactites)):
        stalactites[i].move()
        if Main.collidedWith(stalactites[i]):
            Main.health -= 5
            stalactites[i].visible = False
    if stalactites[i].y > game.height + 100 and stalactites[i].visible == True:
        stalactites[i].visible = False

    if Main.health <= 0:
        game.over = True
        
    if Main.collidedWith(Friend1):
        game.over = True

    if Main.y > game.height + 100:
        Main.health = 0
        
    healthbar.width = Main.health / 2
    healthbar.moveTo( Main.x - 25, Main.y - 40)
    
    game.drawText("level 1", 10, 5)
    #game.drawText("player health" +str(Main.health), 10, 10)
    game.update(30)
    
game.over = False

while not game.over and Main.health > 0:
    Main.health += 30
    game.over = True
    game.update(30)

stalactites = []
for i in range(45):
    stalactite = Image("images/stalactites.png", game)
    stalactite.resizeBy(-90)
    stalactites.append(stalactite)
positionObjects(stalactites)

bk2 = Image("images/level2.png", game)
bk2.resizeTo(game.width, game.height)
game.setBackground(bk2)

Main.moveTo(stone4_1.x, stone4_1.y - 50)

Friend2 = Animation("images/Dude_Monster_Idle_4.png", 4, game, 128/4, 32, 3)
Friend2.resizeBy(100)
#Friend2.collisionBorder = "rectangle"
Friend2.moveTo(stone7_2.x, stone7_2.y - 43)
                    
game.over = False

#level 2 
while not game.over and Main.health > 0:
    game.processInput()
    bk2.draw()
    Main.draw()
    Friend2.draw()
    Friend2.flipV = True
    
    if keys.Pressed[K_d]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main = Main_walk
        Main.x += 2
        #Main.offsetX = -25
        Main.flipV = False
        Main_idle.flipV = False
    elif keys.Pressed[K_a]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main.flipV = True
        Main_idle.flipV = True
        Main = Main_walk
        Main.x -= 2
        #Main.offsetX = -75
    else:
        Main_idle.visible = True
        Main = Main_idle
    #print(landed, jumping, keys.Pressed[K_w])
    
    if keys.Pressed[K_w] and landed and not jumping:
        #Main.images = Main_jump.images
        jumping = True
        
    if jumping:
        jumping = True
        landed = False
        Main.y -= 10 * factor
        factor *= .96
        if factor < 0.1:
            jumping = False
            factor = 1


    jumpingCollision2()
    
    #stone1.draw()
    stone1_2.draw()
    stone1_1.draw()
    stone1_4.draw()
    stone1_3.draw()

    #stone2.draw()
    stone2_1.draw()
    stone2_3.draw()
    stone2_2.draw()

    #stone3.draw()
    #stone3_1.draw()
    stone3_3.draw()
    #stone3_2.draw()
    stone3_2_2.draw()
    
    #stone4.draw()
    stone4_2.draw()
    stone4_1.draw()
    
    #stone5.draw()
    #stone5_2.draw()
    stone5_1.draw()

    #stone6.draw()
    stone6_1.draw()
    stone6_3.draw()
    stone6_2.draw()
    
    #stone7.draw()
    stone7_1.draw()
    stone7_3.draw()
    stone7_2.draw()
    
    waterfallcollisionbox1_1.draw()
    waterfallcollisionbox1_2.draw()
    waterfall.draw()
    
    waterfallcollisionbox2_1.draw()
    waterfallcollisionbox2_2.draw()
    waterfall2.draw()

    waterfallCollisions1()
    waterfallCollisions2()
    for i in range(len(stalactites)):
      stalactites[i].move()

    for i in range(len(stalactites)):
        stalactites[i].move()
        if Main.collidedWith(stalactites[i]):
            Main.health -= 5
            stalactites[i].visible = False
    if stalactites[i].y > game.height + 100 and stalactites[i].visible == True:
        stalactites[i].visible = False
    
    if Main.health <= 0:
        game.over = True
        
    if Main.collidedWith(Friend2):
        game.over = True

    if Main.y > game.height + 100:
        Main.health = 0
        
    healthbar.width = Main.health / 2
    healthbar.moveTo( Main.x - 25, Main.y - 40)

    game.drawText("level 2", 10, 5)
    game.update(30)
game.over = False

while not game.over and Main.health > 0:
    Main.health += 30
    game.over = True
    game.update(30)

game.over = False

Main.moveTo(lava6_2.x + 100, lava6_2.y - 50)

bk3 = Image("images/level3.png", game)
bk3.resizeTo(game.width, game.height)
game.setBackground(bk3)

#level 3
while not game.over and Main.health > 0:
    game.processInput()
    bk3.draw()

    lava1.draw()
    lava2.draw()
    #lava3.draw()
    lava4.draw()
    #lava5.draw()
    lava6_2.draw()
    lava6.draw()
    #lava7.draw()
    lava9_2.draw()
    lava9.draw()
    lava10_2.draw()
    lava10.draw()
    lava11_2.draw()
    lava11.draw()
    Main.draw()

    flame.draw()
    flame2.draw()
    flame3.draw()
    flame4.draw()
    flame5.draw()

    flame_collision()

    if keys.Pressed[K_d]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main = Main_walk
        Main.x += 2
        #Main.offsetX = -25
        Main.flipV = False
        Main_idle.flipV = False
    elif keys.Pressed[K_a]:
        Main_walk.moveTo(Main.x,Main.y)
        Main_idle.moveTo(Main.x,Main.y)
        Main_idle.visible = False
        Main.flipV = True
        Main_idle.flipV = True
        Main = Main_walk
        Main.x -= 2
        #Main.offsetX = -75
    else:
        Main_idle.visible = True
        Main = Main_idle
    #print(landed, jumping, keys.Pressed[K_w])
    
    if keys.Pressed[K_w] and landed and not jumping:
        #Main.images = Main_jump.images
        jumping = True
        
    if jumping:
        jumping = True
        landed = False
        Main.y -= 10 * factor
        factor *= .96
        if factor < 0.1:
            jumping = False
            factor = 1

    jumpingCollision3()

    risinglava.move()

    #print(risinglava.collidedWith(Main,"rectangle"))

    if risinglava.top < lava11.bottom:
        risinglava.setSpeed(0, 360)

        ladder.draw()
        if Main.collidedWith(ladder,"rectangle"):
            game.over = True

    if risinglava.collidedWith(Main,"rectangle"):
        Main.health -= 2.5

    if Main.health <= 0:
        game.over = True

    if Main.y > game.height + 100:
        Main.health = 0

    healthbar.width = Main.health / 2
    healthbar.moveTo( Main.x - 25, Main.y - 40)

    game.drawText("level 3", 10, 5)
    game.update(30)
game.over = False

endbk = Image("images/endscreenbk.webp", game)
endbk.resizeTo(game.width, game.height)
game.setBackground(endbk)

while not game.over and Main.health > 0:
    game.processInput()
    endbk.draw()
    youwon.draw()
    gameplay.draw()
    gameexit2.draw()

    
    if keys.Pressed[K_SPACE]:
        game.over = True 
    
    game.update(30)
game.over = False


endbk2 = Image("images/endscreenbk2.png", game)
endbk2.resizeTo(game.width, game.height)
game.setBackground(endbk2)


while not game.over and Main.health <= 0:
    game.processInput()
    endbk2.draw()
    gameover.draw()
    youdied.draw()
    gameexit.draw()

    if keys.Pressed[K_SPACE]:
        game.over = True 

    game.update(30)
game.quit()
