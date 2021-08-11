class dino:
    def dino_details(self, dino_name, dino_health, dino_weapon):
            self.dino_name = dino_name
            self.dino_health = dino_health
            self.dino_weapon = dino_weapon
 
    def attack(self, dino_to_attack):
        dino_to_attack.dino_health -= self.robot_weapon.attack_power