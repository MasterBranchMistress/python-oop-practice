class User():
    logged_in = False
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        if not self.logged_in:
            self.logged_in = True
            print(f"{self.name} signed in")
        else:
            self.logged_in = False
        
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        if self.logged_in:
            print(f"Attacking with power of {self.power}")
            self.power -= 20
        else:
            print("Need to sign in first")

class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def attack(self):
        if self.logged_in:
            print(f"Attacking with arrows: {self.arrows}")
            self.arrows -= 1
        else:
            print("Need to sign in first")
wizard1 = Wizard("Merlin", 50, "merlin@example.com")
wizard1.sign_in()
archer1 = Archer("Robin", 10, "robin@example.com")
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

# multiple_inheritance_example = dont even think about it
# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows, email):
#         Wizard.__init__(self, name, power, email)
#         Archer.__init__(self, name, arrows, email)

# zdborg = HybridBorg("Ziodborg", 100, 50, "hybrid@gmail.com")
