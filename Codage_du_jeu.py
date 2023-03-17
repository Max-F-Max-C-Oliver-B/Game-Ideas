import pyxel, random, time
"""Tu as pour mission de sauver la Terre d'une pluie de météorites en la guidant hors de danger en évitant chacune d'entre-elles"""

taille_fenetre=256
pyxel.init(taille_fenetre, taille_fenetre, title="Astroide reign")
pyxel.load("res (1).pyxres")
points2 = 0
points = 0
i = 1

#coin haut gauche
Terre_x = 60
Terre_y = 60

terre_width=16
terre_height=16

#30=1seconde
Ticks = 100000
Ticks2 = 100000 
timer = 20

météorites_liste_up = []

météorites_liste_left = []

explosions_liste = []  

def Terre_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if timer > 20 :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+terre_width< taille_fenetre) :
                x = x + 2
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 2
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+terre_height< taille_fenetre) :
                y = y + 2
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 2
    if timer > 10 :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+terre_width< taille_fenetre) :
                x = x + 1.5
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 1.5
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+terre_height< taille_fenetre) :
                y = y + 1.5
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 1.5
    else :
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x+terre_width< taille_fenetre) :
                x = x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y+terre_height< taille_fenetre) :
                y = y + 1
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 1
    return x, y


def météorites_creation(météorites_liste_up, météorites_liste_left):
    """création aléatoire des météorites"""

    # un météorite par seconde
    if (pyxel.frame_count % 30 == 0):
        météorites_liste_up.append([random.randint(0, taille_fenetre-8), 0])
        météorites_liste_left.append([0,random.randint(0, taille_fenetre-8)])


def météorites_deplacement(météorites_liste_up, météorites_liste_left):
    """déplacement des météorites vers le haut et suppression s'ils sortent du cadre"""
    if timer > 20 :
        for météorite in météorites_liste_up:
            météorite[1] += 2
            if  météorite[1]>taille_fenetre:
                météorites_liste_up.remove(météorite)
        for météorite_left in météorites_liste_left:
            météorite_left[0] += 2
            if  météorite_left[0]>taille_fenetre:
                météorites_liste_left.remove(météorite_left)
    else:
        for météorite in météorites_liste_up:
            météorite[1] += 4
            if  météorite[1]>taille_fenetre:
                météorites_liste_up.remove(météorite)
        for météorite_left in météorites_liste_left:
            météorite_left[0] += 4
            if  météorite_left[0]>taille_fenetre:
                météorites_liste_left.remove(météorite_left)
        

def Terre_suppression(Ticks, météorites_liste_up, météorites_liste_left):
    """disparition du Terre et d'un météorite si contact"""
    global points

    for météorite in météorites_liste_up:
        if météorite[0] <= Terre_x+terre_width and météorite[1] <= Terre_y+terre_height and météorite[0]+8 >= Terre_x and météorite[1]+8 >= Terre_y:
            météorites_liste_up.remove(météorite)
            Ticks -= 1
            points += 1
            explosions_creation(Terre_x, Terre_y)
    for météorite in météorites_liste_left:
        if météorite[0] <= Terre_x+terre_width and météorite[1] <= Terre_y+terre_height and météorite[0]+8 >= Terre_x and météorite[1]+8 >= Terre_y:
            météorites_liste_left.remove(météorite)
            points += 1
        Ticks -= 1
        explosions_creation(Terre_x, Terre_y)
    return Ticks
    
def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 0])



def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)  
            
def pointsystem():
    global timer, points, points2
    if timer == 1:
        points2 = points


def clock():
    """40 ticks vaut une seconde, donc on défini timer grâce à ça"""
    global timer,Ticks2
    if Ticks2%30 == 0 :
        timer -= 1
        
def endpoints():
    global timer, points , points2
    if timer > 1 :
        points2 = points
    return points


def update():
    """mise à jour des variables (30 fois par seconde)"""
    
    global Terre_x, Terre_y, météorites_liste_up, Ticks, explosions_liste, timer, Ticks2, points, i, points2

    Terre_x, Terre_y = Terre_deplacement(Terre_x, Terre_y)

    météorites_creation(météorites_liste_up, météorites_liste_left)
    météorites_deplacement(météorites_liste_up, météorites_liste_left)

    Ticks = Terre_suppression(Ticks, météorites_liste_up, météorites_liste_left)

    explosions_animation()

    endpoints()

    clock()
    Ticks2-=1

def draw():
    """création des objets (30 fois par seconde)"""
    
    global Ticks2 , i
    pyxel.cls(0)
    if timer > 0:

        pyxel.text(5,5, 'Points: '+ str(points), 7)
        
        pyxel.text(taille_fenetre-30,5, 'Time:' + str(timer),7)
        
        #pyxel.rect(Terre_x, Terre_y, 8, 8, 1)
        pyxel.blt(Terre_x, Terre_y,0,48,112,terre_width,terre_height)

        for météorite in météorites_liste_up:
            pyxel.rect(météorite[0], météorite[1], 8, 8, 8)
        for météorite in météorites_liste_left:
            pyxel.rect(météorite[0], météorite[1], 8, 8, 8)
        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)            

    else:
        if i < 16:
            if Ticks2%7 == 0 :
                i = i + 1
                if i == 15:
                    i=1
            pyxel.text(110,110, 'GAME OVER', i)
        pyxel.text(105,120, 'Vos Points:' + str(points),7)

pyxel.run(update, draw)
