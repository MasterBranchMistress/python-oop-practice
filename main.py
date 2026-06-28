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
    
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2  # Static method to add two numbers
    
player1 = PlayerCharacter("Alice", 5)
player1.display_info()
player1.run()
player2addingstuff = PlayerCharacter.add_things(3, 4)  # 
# Using the class method without creating an instance
print(f"Sum of numbers using class method: {player2addingstuff}")

#Creates an instance of PlayerCharacter with name "jimmie" and level as the sum of num1 and num2
print(PlayerCharacter.add_things(6, 4))  # Using the class method without creating an instance