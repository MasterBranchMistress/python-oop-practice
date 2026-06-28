# OOP
class PlayerCharacter:
    membership = True  # Class attribute
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display_info(self):
        print(f"Player Name: {self.name}, Level: {self.level}")

    def run(self):
        print(f"{self.name} is running at level {self.level}.")
    
player1 = PlayerCharacter("Alice", 5)
player1.display_info()
player1.run()
print(player1.name)