#super and sub classes

class Player:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class NewPlayer(Player):

    def __init__(self, firstName, lastName, total):
        Player.__init__(self, firstName, lastName)
        self.total = total

        def getDetails(self):
            return "%s %s has spent %s in total" %(self.firstName, self.lastName, self.total)

player1 = NewPlayer("Leo", "Messi", 1000)

print(player1.getDetails())