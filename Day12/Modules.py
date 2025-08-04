#Exercices: Level1
#1
import random
import string
def random_user_id():
    characteres = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characteres) for _ in range (6))
    return user_id
print(random_user_id())


#2
import random
import string

def user_id_gen_by_user():
    char_count = int(input("Combien de caractères par ID ? "))
    id_count = int(input("Combien d'IDs à générer ? "))

    characters = string.ascii_letters + string.digits  # Lettres + chiffres

    for _ in range(id_count):
        user_id = ''.join(random.choice(characters) for _ in range(char_count))
        print(user_id)



#3
import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"



#Exercices: Level2
#1
import random

def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(color)
    return hex_colors


#2
import random
def list_of_rgb(n):
    rgb_colors = []
    for j in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r}, {g}, {b})"
        rgb_colors.append(color)
    return rgb_colors
print(list_of_rgb(5))


#3
import random

def generate_colors(color_type, count):
    colors = []
    
    if color_type == 'hexa':
        for _ in range(count):
            color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
            colors.append(color)
    
    elif color_type == 'rgb':
        for _ in range(count):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r},{g},{b})")
    
    else:
        return "Type de couleur non reconnu. Utilisez 'hexa' ou 'rgb'."
    
    return colors


#Exercices :Level3
#1
import random

def shuffle_list(lst):
    shuffled = lst[:]             # On fait une copie de la liste pour ne pas modifier l’originale
    random.shuffle(shuffled)      # On mélange les éléments
    return shuffled

#2
import random

def unique_random_numbers():
    return random.sample(range(10), 7)  # 7 nombres uniques entre 0 et 9
