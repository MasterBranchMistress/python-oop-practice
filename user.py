class User():
    logged_in = False
    def sign_in(self):
        if not self.logged_in:
            self.logged_in = True
            print(f"{self.name} signed in")
        else:
            self.logged_in = False
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        if self.logged_in:
            print(f"Attacking with power of {self.power}")
            self.power -= 20
        else:
            print("Need to sign in first")

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        if self.logged_in:
            print(f"Attacking with arrows: {self.arrows}")
            self.arrows -= 1
        else:
            print("Need to sign in first")
wizard1 = Wizard("Merlin", 50)
wizard1.sign_in()
archer1 = Archer("Robin", 10)
archer1.sign_in()
archer1.attack()
archer1.attack()
wizard1.attack()
wizard1.attack()

print(isinstance(wizard1, User))  # True
print(isinstance(archer1, User))  # True
print(isinstance(wizard1, Archer))  # False

def player_attack(player):
    player.attack()

player_attack(wizard1)  # Attacking with power of 30
player_attack(archer1)  # Attacking with arrows: 8

for char in [wizard1, archer1]:
    char.attack()  # Attacking with power of 10, Attacking with arrows: 7