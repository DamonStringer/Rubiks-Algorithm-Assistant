import json
def load_library():
    try:
        with open("algs.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Save file missing or corrupted. Initializing OLL/PLL categories...")
        return {"oll": {}, "pll": {}}

def save_library(library_data):
    with open("algs.json", "w") as file:
        json.dump(library_data, file)
    print("Library saved permanently")
    
library = load_library()
while True:
    print("\n--- New Solve ---")
    oll_query = input("Enter OLL Case (or 'exit' to quit): ").lower()
    if oll_query == "exit":
        save_library(library)
        break  
    if oll_query in library["oll"]:
        print(f"OLL Moves: {library['oll'][oll_query]}")
    else:
        print("OLL case not found. Check your JSON spelling.")
        continue     
    pll_query = input("Enter PLL Case: ").lower()
    if pll_query in library["pll"]:
        print(f"PLL Moves: {library['pll'][pll_query]}")
    else:
        print("PLL case not found. Check your JSON spelling.")