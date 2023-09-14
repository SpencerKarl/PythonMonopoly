# Import statements
import os

# Class to be used for each individual player object
class Player:
    playerNumber = 0
    playerName = "Not Set"
    playerCash = 1500

    def __init__(self,playerNumber,playerName):
        self.playerNumber = playerNumber
        self.playerName = playerName
    
    # Used for debugging
    def DisplayDetails(self):
        print("Player Number:", self.playerNumber)
        print("Player Name:", self.playerName)
        print("Player Cash:", self.playerCash)

# Function to display initial splash screen
def SplashScreen(playerOne):
    os.system('cls')
    print("Welcome to Python Monopoly,",playerOne.playerName + "!\n"
          "This is a new line.")
    
# Main function
if __name__ == "__main__":
    playerOne = Player(1, input("Enter your player name: "))
    SplashScreen(playerOne)
    playerOne.DisplayDetails()
