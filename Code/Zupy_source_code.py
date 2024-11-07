from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from random import randint

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
time = 0
font = pygame.font.Font(None, 36)
 
# Couleurs
purple = (128, 0, 128)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 242, 0)
black = (0, 0, 0)

# Variables de jeu
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
monster_pos = pygame.Vector2(randint(0, 200), randint(0, 200))
etat = 0
best_score = 0
etat_diff = 1
etat_speed = 1
player_speed = 320
velo_m1 = 0
velo_m2 = 80

def mov_1():
    global time
    global dt
    global monster_pos
    global player_pos
    global velo_m1
    global etat_diff
    if etat_diff == 3:
        velo_m1 = 120
    if etat_diff == 1:
        velo_m1 = 180
    if etat_diff == 2:
        velo_m1 = 230
        # Mouvement du monstre vers le joueur après 2 secondes
    if time >= 120:
        if monster_pos.y > player_pos.y:
            monster_pos.y -= velo_m1 * dt
        if monster_pos.y < player_pos.y:
            monster_pos.y += velo_m1 * dt
        if monster_pos.x > player_pos.x:
            monster_pos.x -= velo_m1 * dt
        if monster_pos.x < player_pos.x:
            monster_pos.x += velo_m1 * dt

def mov_2():
    global time
    global dt
    global monster2_pos
    global player_pos
    global velo_m2
    global etat_diff
    global tp_mo2
    if etat_diff == 2:
        velo_m2 = 130
        # Mouvement du monstre 2 vers le joueur
    if time >= 600:
        if monster2_pos.y > player_pos.y:
            monster2_pos.y -= velo_m2 * dt
        if monster2_pos.y < player_pos.y:
            monster2_pos.y += velo_m2 * dt
        if monster2_pos.x > player_pos.x:
            monster2_pos.x -= velo_m2 * dt
        if monster2_pos.x < player_pos.x:
            monster2_pos.x += velo_m2 * dt
        if etat_diff == 3:
            tp_mo2 = randint(1, 400)
            if tp_mo2 == 400:
                v_pos()
                monster2_pos = pygame.Vector2(verif1, verif2)
        if etat_diff == 1:
            tp_mo2 = randint(1, 200)
            if tp_mo2 == 200:
                v_pos()
                monster2_pos = pygame.Vector2(verif1, verif2)
        if etat_diff == 2:
            tp_mo2 = randint(1, 100)
            if tp_mo2 == 100:
                v_pos()
                monster2_pos = pygame.Vector2(verif1, verif2)


# Zone hors de l'écran où le monstre 2 va spawn
random = randint(1, 4)
if random == 1:
    pos1 = -100
    pos2 = randint (0, 720)
if random == 2:
    pos1 = randint(0, 1280)
    pos2 = 820
if random == 3:
    pos1 = 1380
    pos2 = randint(0, 720)
if random == 4:
    pos1 = randint(0, 1280)
    pos2 = -100

# Système de Tp + patch anti tp-kill (sauf pour impossible)
monster2_pos = pygame.Vector2(pos1, pos2)
verif1 = 0
verif2 = 0

def v_pos():
    global verif1
    global verif2
    global etat_diff
    verif1 = randint(0, 1280)
    verif2 = randint(0, 720)
    if player_pos.x - 150 < verif1 < player_pos.x + 150:
        v_pos()
    if player_pos.y - 150 < verif2 < player_pos.y + 150:
        v_pos()

def stop_game():
    global etat
    global score
    global best_score
    etat = 0
    if score > best_score:
        best_score = score

score = 0
score2 = 0
bonus_r = 3  # Nombre de dash disponibles
bonus_val = 1  # Variable de contrôle du bonus
bonus = 0
bonus_pos = pygame.Vector2(randint(0, 1280), randint(0, 720))

# Cooldown pour le dash
dash_cooldown = 0.5  # Délai de 0,5 seconde entre chaque dash
last_dash_time = 0  # Temps du dernier dash utilisé

def set_difficulty(value, difficulty):
    global etat_diff
    print(value)
    print(difficulty)
    etat_diff = difficulty
 
def set_speed(value, speed):
    global etat_speed
    global player_speed
    print(value)
    print(speed)
    etat_speed = speed
    if etat_speed == 1:
        player_speed = 320
    if etat_speed == 2:
        player_speed = 480
    if etat_speed == 3:
        player_speed = 265

def start_the_game():
 global score
 global score2
 global bonus_r
 global bonus_val
 global bonus
 global bonus_pos
 global last_dash_time
 global dash_cooldown
 global current_time
 global monster2_pos
 global player_pos
 global monster_pos
 global purple
 global yellow
 global red
 global green
 global blue
 global black
 global screen
 global time
 global dt
 global clock
 global verif1
 global verif2
 global etat
 global etat_diff
 global player_speed
 global etat_speed

 etat = 1
 dt = 0
 time = 0
 score = 0
 score2 = 0
 bonus_r = 3  # Nombre de dash disponibles
 bonus_val = 1  # Variable de contrôle du bonus
 bonus = 0
 bonus_pos = pygame.Vector2(randint(0, 1280), randint(0, 720))

 player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
 monster_pos = pygame.Vector2(randint(0, 200), randint(0, 200))
 monster2_pos = pygame.Vector2(pos1, pos2)

 # Cooldown pour le dash
 dash_cooldown = 0.5  # Délai de 0,5 seconde entre chaque dash
 last_dash_time = 0  # Temps du dernier dash utilisé

 while etat == 1:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game()

    # Effacer l'écran pour dessiner une nouvelle image
    if etat_diff == 1 and etat_speed == 1:
        screen.fill("white")
    else:
        screen.fill("purple")

    # Dessiner le joueur et le monstre
    pygame.draw.circle(screen, red, player_pos, 40)
    pygame.draw.circle(screen, blue, monster_pos, 40)
    pygame.draw.circle(screen, yellow, monster2_pos, 50)

    # Incrémentation du score (augmente chaque frame)
    time += 1
    score = time // 6 + score2 # Le score augmente toutes les dixième de seconde

    # Génération aléatoire du bonus
    if bonus_val == 1:
        bonus = randint(1, 180)
        if bonus == 180:
            bonus_val = 0
            bonus_pos = pygame.Vector2(randint(0, 1280), randint(0, 720))

    # Afficher le bonus et vérifier sa collision avec le joueur
    if bonus == 180:
        pygame.draw.circle(screen, green, bonus_pos, 10)
        distance_bonus = player_pos.distance_to(bonus_pos)

        if distance_bonus <= 80:
            bonus_r += 1
            score2 += 50
            bonus_val = 1

    mov_1()

    mov_2()

    # Vérifier la distance entre le monstre et le joueur pour mettre fin au jeu
    distance = player_pos.distance_to(monster_pos)
    if distance <= 40:
        stop_game()  # Arrêter la boucle de jeu au lieu d'appeler pygame.quit()


    # Vérifier la distance entre le monstre 2 et le joueur pour mettre fin au jeu
    distance2 = player_pos.distance_to(monster2_pos)
    if distance2 <= 40:
        stop_game()  # Arrêter la boucle de jeu au lieu d'appeler pygame.quit()

    # Déplacement du joueur et utilisation du dash
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks() / 1000  # Obtenir le temps en secondes

    if keys[pygame.K_z]:  # Haut
        player_pos.y -= player_speed * dt
        if keys[pygame.K_SPACE] and bonus_r > 0 and (current_time - last_dash_time) >= dash_cooldown:
            player_pos.y -= 10000 * dt
            bonus_r -= 1
            last_dash_time = current_time  # Mettre à jour le temps du dernier dash

    if keys[pygame.K_s]:  # Bas
        player_pos.y += player_speed * dt
        if keys[pygame.K_SPACE] and bonus_r > 0 and (current_time - last_dash_time) >= dash_cooldown:
            player_pos.y += 10000 * dt
            bonus_r -= 1
            last_dash_time = current_time

    if keys[pygame.K_q]:  # Gauche
        player_pos.x -= player_speed * dt
        if keys[pygame.K_SPACE] and bonus_r > 0 and (current_time - last_dash_time) >= dash_cooldown:
            player_pos.x -= 10000 * dt
            bonus_r -= 1
            last_dash_time = current_time

    if keys[pygame.K_d]:  # Droite
        player_pos.x += player_speed * dt
        if keys[pygame.K_SPACE] and bonus_r > 0 and (current_time - last_dash_time) >= dash_cooldown:
            player_pos.x += 10000 * dt
            bonus_r -= 1
            last_dash_time = current_time

    # Garder le joueur dans les limites de l'écran
    player_pos.x = max(0, min(player_pos.x, 1280))
    player_pos.y = max(0, min(player_pos.y, 720))

    # Afficher le score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Afficher le nombre de dash restants
    dash_text = font.render(f"Nombre de Dash: {bonus_r}", True, black)
    screen.blit(dash_text, (10, 50))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre d'images par seconde et calculer le temps écoulé
    dt = clock.tick(60) / 1000  # 60 FPS
 
def level_menu():
    mainmenu._open(settings)
 
# Menu principal
if etat == 0:
    mainmenu = pygame_menu.Menu('Zupy', 1280, 720, theme=themes.THEME_SOLARIZED)
    
    # Ajouter le label du meilleur score et mettre à jour la valeur à chaque fois que vous entrez dans le menu
    best_score_label = mainmenu.add.label(f"Meilleur score : {best_score}")
    
    # Ajouter les boutons de menu
    mainmenu.add.button('Play', start_the_game)
    mainmenu.add.button('Settings', level_menu)
    mainmenu.add.button('Quit Game', pygame_menu.events.EXIT)
    mainmenu.add.label('Alpha V3.1')

    # Sous-menu pour la sélection du niveau
    settings = pygame_menu.Menu('Settings', 1280, 720, theme=themes.THEME_BLUE)
    settings.add.selector('Difficulty :', [('Normal', 1), ('Hard', 2), ('Easy', 3)], onchange=set_difficulty)
    settings.add.selector('Speed :', [('Normal', 1), ('High', 2), ('Low', 3)], onchange=set_speed)

    # Boucle de gestion du menu principal
    while etat == 0:
        # Récupérer tous les événements
        events = pygame.event.get()
        
        # Gérer la fermeture de la fenêtre avec la croix
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Mettre à jour le menu en passant les événements
        mainmenu.update(events)

        # Mettre à jour le meilleur score dans le label
        best_score_label.set_title(f"Meilleur score : {best_score}")

        # Dessiner le menu
        mainmenu.draw(screen)
        
        # Rafraîchir l'écran
        pygame.display.flip()

pygame.quit()