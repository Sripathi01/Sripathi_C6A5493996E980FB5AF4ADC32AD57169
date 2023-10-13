class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
batsman_obj = Batsman()
bowler_obj = Bowler()
batsman_obj.play()
bowler_obj.play()