class Robot:
    def __init__(self, robot_name, robot_health, robot_weapon):
        self.robot_name = robot_name
        self.robot_health = robot_health #100pts or full?
        self.robot_weapon = robot_weapon #robo_blaster

    def attack(self, dino_to_attack):
        dino_to_attack.dino_health -= self.robot_weapon.attack_power


dino = dino()
fleet = Fleet()
fleet.robot_list[0].attack(dino)
fleet.my_robot

herd.dino_list[0].attack(fleet.robot_list[0])





my_robot1.attack(dino)




class dino:
        def __init__ (self):
            self.dino_name = ''
            self.dino_health = ''
            self.dino_weapon = ''
         
        

        def dino_details(self, dino_name, dino_health, dino_weapon):
            self.dino_name = dino_man
            self.dino_health = full
            self.dino_weapon = flinstone_cannon()
        
class flinstone_cannon:
     def __inint__ (self):
            self.wpn_type = 'cannon_pistol'
            self.round_count = ''
            self.hit_points = ''

