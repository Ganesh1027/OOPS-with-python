class Character:
    def __init__(self , name , health):
        self.name = name
        self.health = health
    def take_damage(self,damage):
        self.health -= damage
    def attack(self, target , damage):
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name}")
    def display(self):
        print(f'Player Name : {self.name}')
        print(f'Player Health : {self.health}')
player = Character("Ganesh",100)
enemy = Character("gani",100)
player.attack(enemy , 20)
enemy.display()
        
