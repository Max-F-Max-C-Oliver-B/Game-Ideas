import pyxel, random

pyxel.init(128, 128, title="Vesky")

vaisseau_x = 60
vaisseau_y = 60

vies = 2

ennemi = []
ennemi2 = []
explosions = []  

def vaisseau_deplacement(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 2.5
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 2.5
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 2.5
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 2.5
    return x, y

def creation_ennemis(ennemi):

    if (pyxel.frame_count % 30 == 0):
        ennemi.append([random.randint(0, 120), 0])
    return ennemi
    
def creation_ennemis(ennemi2):

    if (pyxel.frame_count % 30 == 0):
        ennemi2([random.randint(0, 120), 0])
    return ennemi2
def ennemis_deplacement(ennemi):
    
    for ennemi in ennemi:
        ennemi[1] += 2
        if  ennemi[1]>128:
            ennemi.remove(ennemi)
    return ennemi
for ennemi2 in ennemi2:
        ennemi2[0] += 2
        if  ennemi2[0]>128:
            ennemi2.remove(ennemi2)
    return ennemi2

def vaisseau_suppression(vies):
    """disparition du vaisseau et d'un ennemi si contact"""

    for ennemi in ennemi:
        if ennemi[0] <= vaisseau_x+8 and ennemi[1] <= vaisseau_y+8 and ennemi[0]+8 >= vaisseau_x and ennemi[1]+8 >= vaisseau_y:
            ennemi.remove(ennemi)
            vies -= 1
            # on ajoute l'explosion
            explosions_creation(vaisseau_x, vaisseau_y)
    return vies


def ennemis_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)
                # on ajoute l'explosion
                explosions_creation(ennemi[0], ennemi[1])


def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 0])


def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)                

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, explosions_liste

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_liste = ennemis_deplacement(ennemis_liste)

    # suppression des ennemis et tirs si contact
    ennemis_suppression()

    # suppression du vaisseau et ennemi si contact
    vies = vaisseau_suppression(vies)

    # evolution de l'animation des explosions
    explosions_animation()    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # si le vaisseau possede des vies le jeu continue
    if vies > 0:

        # affichage des vies            
        pyxel.text(5,5, 'VIES:'+ str(vies), 7)

        # vaisseau (carre 8x8)
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

        # ennemis
        for ennemi in ennemis_liste:
            pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

        # explosions (cercles de plus en plus grands)
        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)            

    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)




                                                                VERSION 2

    
    
    
import pyxel, random, time
"""Tu as pour mission de sauver la Terre d'une pluie de météorites en la guidant hors de danger en évitant chacune d'entre-elles"""
pyxel.init(128, 128, title="Astroide reign")


#coin haut gauche
Terre_x = 60
Terre_y = 60

vies = 3

météorites_liste = []
météorites_liste_left = []

explosions_liste = []  
start_time = time.time()

def Terre_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1.5
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1.5
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 1.5
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 1.5
    return x, y


def météorites_creation(météorites_liste, météorites_liste_left):
    """création aléatoire des météorites"""

    # un météorite par seconde
    if (pyxel.frame_count % 30 == 0):
        météorites_liste.append([random.randint(0, 120), 0])
        météorites_liste_left.append([random.randint(0, 120), 0])
    return météorites_liste, météorites_liste_left


def météorites_deplacement(météorites_liste, météorites_liste_left):
    """déplacement des météorites vers le haut et suppression s'ils sortent du cadre"""

    for météorite in météorites_liste:
        météorite[1] += 2
        if  météorite[1]>128:
            météorites_liste.remove(météorite)
    for météorite_left in météorites_liste_left:
        météorite_left[0] -= 2
        if  météorite_left[0]>128:
            météorites_liste_left.remove(météorite)
    return météorites_liste, météorites_liste_left

def Terre_suppression(vies, météorites_liste, météorites_liste_left):
    """disparition du Terre et d'un météorite si contact"""

    for météorite in météorites_liste:
        if météorite[0] <= Terre_x+8 and météorite[1] <= Terre_y+8 and météorite[0]+8 >= Terre_x and météorite[1]+8 >= Terre_y:
            météorites_liste.remove(météorite)
            vies -= 1
            explosions_creation(Terre_x, Terre_y)
    for météorite in météorites_liste_left:
        if météorite[0] <= Terre_x+8 and météorite[1] <= Terre_y+8 and météorite[0]+8 >= Terre_x and météorite[1]+8 >= Terre_y:
            météorites_liste_left.remove(météorite)
        vies -= 1
        explosions_creation(Terre_x, Terre_y)
    return vies
def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 0])


def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)              
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global Terre_x, Terre_y, météorites_liste, vies, explosions_liste

    Terre_x, Terre_y = Terre_deplacement(Terre_x, Terre_y)

    météorites_liste = météorites_creation(météorites_liste)

    météorites_liste = météorites_deplacement(météorites_liste)

    vies = Terre_suppression(vies)

    explosions_animation()    

def draw():
    """création des objets (30 fois par seconde)"""

    pyxel.cls(0)

    if vies > 0:

        pyxel.text(5,5, 'VIES:'+ str(vies), 7)
        
        pyxel.text(90,5, 'TIMER:',7)

        pyxel.rect(Terre_x, Terre_y, 8, 8, 1)


        for météorite in météorites_liste:
            pyxel.rect(météorite[0], météorite[1], 8, 8, 8)

        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)            

    else:

        pyxel.text(50,64, 'GAME OVER', 7)

pyxel.run(update, draw)
