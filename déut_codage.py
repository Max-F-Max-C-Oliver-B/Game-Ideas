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
