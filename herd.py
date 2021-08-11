class Herd:
    def __init__(self):
        new_weapon = weapon("laser", 50)
        my_dino = dino("Tiny-Diny", 100, new_weapon)
        my_dino1 = dino("Yellow-Diny", 100, new_weapon)
        my_dino2 = dino("Orange-Diny", 100, new_weapon)
        dino_list = my_dino, my_dino1, my_dino2


