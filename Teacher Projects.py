import json

class AlgorithmLibrary:
    def __init__(self, filename="algs.json"):
        self.filename = filename
        self.data = self.load_library()
    
    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
                    print("No save file found. Initializing OLL/PLL categories...")
                    return {"oll": {}, "pll": {}}
    def save_library(self):
      with open(self.filename, "w") as file:
        json.dump(self.data, file)
      print("Library saved permanently")
      
    def count_moves(self, alg):
      move_list = alg.split()
      return len(move_list)

    def generate_scramble(self, alg):
        clean_alg = alg.replace("(", "").replace(")", "")
        moves = clean_alg.split()
        moves.reverse()
        scramble = []
        for move in moves:
            if "2" in move:
                scramble.append(move)
            elif "'" in move:
                scramble.append(move.replace("'", ""))
            else:
                scramble.append(move + "'")
        return " ".join(scramble)
                 