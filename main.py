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
    
    @classmethod
    def add_things(cls, num1, num2):
        return cls("jimmie", num1 + num2)  # Using class method to create an instance
    
player1 = PlayerCharacter("Alice", 5)
player1.display_info()
player1.run()
player2addingstuff = PlayerCharacter.add_things(3, 4)  # 
# Using the class method without creating an instance
print(f"Sum of numbers using class method: {player2addingstuff}")
print(PlayerCharacter.add_things(6, 4))  # Using the class method without creating an instance