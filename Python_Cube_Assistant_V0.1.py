import json

def load_library():
    try:
        with open("algs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No save file found. Initializing OLL/PLL categories...")
        return {"oll": {}, "pll": {}}

def save_library(library_data):
  with open("algs.json", "w") as file:
        json.dump(library_data, file)
  print("Library saved permanently")
      
def count_moves(alg):
  move_list = alg.split()
  return len(move_list)

oll_library = load_library()
save_library(oll_library)

while True:
    print("\n--- New Solve ---")
   
    oll_query = input("Enter Command (list/add/exit) or OLL Case: ").lower()
    
    if oll_query == "exit":
        save_library(oll_library)
        break 
    if oll_query == "list":
        print("\n--- Current OLL Library ---")
        for case_name in oll_library["oll"].keys():
            print(f"- {case_name}")
        print("\n--- Current PLL Library ---")
        for case_name in oll_library["pll"].keys():
            print(f"- {case_name}")
        print("----------------------")
        continue
    elif oll_query == "add":
        drawer = input("Is this OLL or PLL? ").lower()
        if drawer in ["oll", "pll"]:
            new_case = input("Enter the case name: ").lower()
            new_alg = input("Enter the algorithm: ")
            oll_library[drawer][new_case] = new_alg
            save_library(oll_library)
            print(f"Successfully added {new_case}!")
        else:
            print("Invalid category.")
    if oll_query in oll_library["oll"]:
        alg = oll_library["oll"][oll_query]
        moves = count_moves(alg)
        print(f"OLL Moves: {alg} (Move Count: {moves})")
    else:
        print("OLL case not found. Check your JSON spelling.")
        continue     
    pll_query = input("Enter PLL Case: ").lower()
    if pll_query in oll_library["pll"]:
        alg = oll_library['pll'][pll_query]
        moves = count_moves(alg)
        print(f"PLL Moves: {alg} (Move Count: {moves})")
    else:
        print("PLL case not found. Check your JSON spelling.")
    
   