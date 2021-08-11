class Fleet:
    def __init__(self):
        new_weapon = weapon("Sword", 25)
        my_robot = Robot("Wall-E", 100, new_weapon)
        my_robot1 = Robot("T-800", 100, new_weapon)
        my_robot2 = Robot("Bob", 100, new_weapon)
        robot_list = my_robot, my_robot1, my_robot2