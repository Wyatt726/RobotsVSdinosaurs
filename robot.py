class Robot:
    def __init__(self, robot_name, robot_health, robot_weapon):
        self.robot_name = robot_name
        self.robot_health = robot_health 
        self.robot_weapon = robot_weapon 

    def attack(self, robot_to_attack):
        robot_to_attack.robot_health -= self.dino_weapon.attack_power