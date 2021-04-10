players =["Messi", "Neymar", "Suarez", "Iniesta"]
numbers = [10, 11, 9, 8]

players[3] = "Xavi"
numbers[3] = 6
players.append("Pique")
numbers.append(3)
numbers.remove(6)
numbers.clear() #clears list


newPlayers = ["Pedri", "Ansu"]
players.extend(newPlayers)
players.remove("Xavi") # could also use .pop to remove item by index
players.pop(1)


print(players)
print(players[0])