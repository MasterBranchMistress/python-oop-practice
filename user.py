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
wizard1 = Wizard("Merlin", 50)
# wizard1.sign_in()
wizard1.attack()
wizard1.attack()