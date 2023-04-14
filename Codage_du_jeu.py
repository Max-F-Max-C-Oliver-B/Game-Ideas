import pyxel, random, time
"""Tu as pour mission de sauver la monkey d'une pluie de banana en la guidant hors de danger en évitant chacune d'entre-elles"""
taille_fenetre=256
pyxel.init(taille_fenetre, taille_fenetre, title="Astroide reign")
pyxel.load("res2.pyxres")
points2 = 0
points = 0
i = 1

#coin haut gauche
monkey_x = 60
monkey_y = 60

monkey_width=16
monkey_height=16

banana_height=16
banana_width=16

powerup_width=16
powerup_height=16

#30=1seconde
Ticks = 100000
Ticks2 = 100000 
timer = 30

banana_liste_up = []

banana_liste_left = []

powerup_liste= []

explosions_liste = []  

def monkey_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if timer > 20 :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+monkey_width < taille_fenetre) :
                x = x + 2
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 2
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+monkey_height < taille_fenetre) :
                y = y + 2
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 2
    if timer > 10 :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+monkey_width < taille_fenetre) :
                x = x + 1.5
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 1.5
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+monkey_height < taille_fenetre) :
                y = y + 1.5
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 1.5
    else :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+monkey_width < taille_fenetre) :
                x = x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+monkey_height < taille_fenetre) :
                y = y + 1
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 1
    return x, y


def banana_et_powerup_creation(banana_liste_up, banana_liste_left, powerup_liste):
    """création aléatoire des  et des powerup"""

    # une banana par seconde
    if (pyxel.frame_count % 30 == 0):
        banana_liste_up.append([random.randint(0, taille_fenetre-8), 0])
        banana_liste_left.append([0,random.randint(0, taille_fenetre-8)])
    # un powerup chaque 5 seconde
    if timer < 20:
        if (pyxel.frame_count % 150 == 0):
            powerup_liste.append([random.randint(0, taille_fenetre-8), 0])



def banana_et_powerup_deplacement(banana_liste_up, banana_liste_left):
    """déplacement des banana vers le haut et suppression s'ils sortent du cadre"""
    if timer > 20 :
        for banana in banana_liste_up:
            banana[1] += 2
            if  banana[1]>taille_fenetre:
                banana_liste_up.remove(banana)
        for banana_left in banana_liste_left:
            banana_left[0] += 2
            if  banana_left[0]>taille_fenetre:
                banana_liste_left.remove(banana_left)
    else:
        for banana in banana_liste_up:
            banana[1] += 4
            if  banana[1]>taille_fenetre:
                banana_liste_up.remove(banana)
        for banana_left in banana_liste_left:
            banana_left[0] += 4
            if  banana_left[0]>taille_fenetre:
                banana_liste_left.remove(banana_left)
                
    for powerup in powerup_liste:
        powerup[0] += random.randint(-5,5)
        if  powerup[0]>taille_fenetre:
            powerup_liste.remove(powerup)
    for powerup in powerup_liste:
        powerup[1] += random.randint(0,3)
        if  powerup[1]>taille_fenetre:
            powerup_liste.remove(powerup)

def monkey_suppression(Ticks, banana_liste_up, banana_liste_left):
    """disparition du monkey et d'un banana si contact"""
    global points, timer

    for banana in banana_liste_up:
        if banana[0] <= monkey_x+monkey_width and banana[1] <= monkey_y+monkey_height and banana[0]+8 >= monkey_x and banana[1]+8 >= monkey_y:
            banana_liste_up.remove(banana)
            Ticks -= 1
            points += 1
            explosions_creation(monkey_x, monkey_y)
    for banana in banana_liste_left:
        if banana[0] <= monkey_x+monkey_width and banana[1] <= monkey_y+monkey_height and banana[0]+8 >= monkey_x and banana[1]+8 >= monkey_y:
            banana_liste_left.remove(banana)
            points += 1
        Ticks -= 1
        explosions_creation(monkey_x, monkey_y)
    if timer < 20:
        for powerup in powerup_liste:
            if powerup[0] <= monkey_x+monkey_width and powerup[1] <= monkey_y+monkey_height and powerup[0]+8 >= monkey_x and powerup[1]+8 >= monkey_y:
                powerup_liste.remove(powerup)
                timer += 5
    return Ticks
    
def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 1])
    
    

def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)  
            


def clock():
    """40 ticks vaut une seconde, donc on défini timer grâce à ça"""
    global timer,Ticks2
    if Ticks2%30 == 0 :
        timer -= 1
        

def endpoints():
    global timer,points,points2
    if timer == 1 :
        points2 = points
    
    

def update():
    """mise à jour des variables (30 fois par seconde)"""
    
    global monkey_x, monkey_y, banana_liste_up, Ticks, explosions_liste, timer, Ticks2, points, i, points2

    monkey_x, monkey_y = monkey_deplacement(monkey_x, monkey_y)

    banana_et_powerup_creation(banana_liste_up, banana_liste_left, powerup_liste)
    banana_et_powerup_deplacement(banana_liste_up, banana_liste_left)

    Ticks = monkey_suppression(Ticks, banana_liste_up, banana_liste_left)

    explosions_animation()   
    
    endpoints()

    clock()
    Ticks2-=1

def draw():
    """création des objets (30 fois par seconde)"""
    
    global Ticks2 , i
    pyxel.cls(0)
      
    if i < 16:
        if Ticks2%7 == 0 :
            i = i + 1
            if i == 15:
                i=1
    pyxel.bltm(0,0,0,0,0,256,256)
    if timer < 20 and timer > 0:
        pyxel.text(90,8,"POWERUPS ARE ACTIVE",i)
    if timer > 0:

        pyxel.text(5,5, 'Points: '+ str(points), 4)
        
        pyxel.text(taille_fenetre-30,5, 'Time:' + str(timer),4)
        
        pyxel.blt(monkey_x, monkey_y,0,32,0,monkey_width,monkey_height,12)

        for banana in banana_liste_up:
            #pyxel.rect(banana[0], banana[1], 8, 8, 8)
            pyxel.blt(banana[0], banana[1],0,0,0,banana_width,banana_height,12)
        for banana in banana_liste_left:
            #pyxel.rect(banana[0], banana[1], 8, 8, 8)
            pyxel.blt(banana[0], banana[1],0,0,0,banana_width,banana_height,12)
        for powerup in powerup_liste:
            #pyxel.rect(powerup[0], powerup[1], 8, 8, 4)
            pyxel.blt(powerup[0], powerup[1],0,16,0,powerup_width,powerup_height,12)
        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+8, explosion[1]+16, 2*(explosion[2]//3),8)     
                

    else:
        if i < 16:
            if Ticks2%7 == 0 :
                i = i + 1
                if i == 15:
                    i=1
            pyxel.text(110,110, 'GAME OVER', i)
        pyxel.text(105,120, 'Vos Points:' + str(points2),4)

pyxel.run(update, draw)
