
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def displayTeam(self):
        print("Team Name:", self.teamName)
        print("\nPlayers:")

        for player in self.playerList:
            print(player.playerName, "-", player.playerPosition)


# Create 4 player objects
player1 = Player("Joe Montana", "Quarterback")
player2 = Player("Barry Sanders", "Running Back")
player3 = Player("Jerry Rice", "Wide Receiver")
player4 = Player("Graham Gano", "Kicker")

# Add players to a list
playerList = [player1, player2, player3, player4]

# Create an NFL team
team = NFLTeam("San Francisco 49ers", playerList)

# Display team and players
team.displayTeam()
