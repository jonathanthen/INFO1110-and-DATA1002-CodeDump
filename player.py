class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def best_score(players):
        max_score = players[0].score
        best_player = players[0]
        i = 1
        while i < len(players):
            if players[i].score > max_score:
                max_score = players[i].score
                best_player = players[i]
            i += 1
        return best_player

# Some sample code that uses the Player class. 
p1 = Player('Candy', 50)
p2 = Player('Ferb', 250)
p3 = Player('Phineas', 150)

ls = [p1, p2, p3]
best = Player.best_score(ls)
msg = '{} has the best score, with {} points!'.format(best.name, best.score)
print(msg)  # Ferb has the best score, with 250 points!