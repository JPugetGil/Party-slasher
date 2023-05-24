import sys
import os
import json
import random

def assert_exists(file_path):
    if not os.path.exists(file_path):
        print(f'{file_path} could not be found.')
        exit(1)

# read config json from file path
def read_config(file_path):
    if (file_path == None):
        file_path = "./config.json"
    assert_exists(file_path)
    with open(file_path, 'r') as f:
        return json.load(f)
    
def has_one_matched_with_himself(victims, killers):
    for i in range(len(victims)):
        if (victims[i] == killers[i]):
            return True
    return False
    
# shuffle all the elements inside an array and match them with another one
def shuffle(victims):
    killers = victims.copy()
    random.shuffle(killers)
    while has_one_matched_with_himself(victims, killers):
        print("Bad shuffle:")
        print(killers)
        print(victims)
        print("a person cannot be matched with himself. Shuffling again.")
        random.shuffle(killers)
    print("Good shuffle:")
    print(killers)
    print(victims)
    return killers, victims

# assign a symbol to each killer
def assign_symbol(killers, victims, symbols):
    random.shuffle(symbols)
    story = []
    for i in range(len(killers)):
        print(f'{killers[i]} kills {victims[i]} with {symbols[i]}')
        story.append({
            "killer": killers[i],
            "victim": victims[i],
            "weapon": symbols[i]
        })
    return story

# send emails to each killer and victim
def send_emails(story):
    for i in range(len(story)):
        print(f"Sending email to {story[i]['killer']['name']} ({story[i]['killer']['email']}) : you will kill {story[i]['victim']['name']} with {story[i]['weapon']}")
        print(f"Sending email to {story[i]['victim']['name']} ({story[i]['victim']['email']}) : {story[i]['weapon']} will kill you")
        print("\n")

def main():
    # read config
    config = read_config(sys.argv[1] if len(sys.argv) > 1 else None)
    print(config["users"][1])
    killers, victims = shuffle(config["users"])
    story = assign_symbol(killers, victims, config["symbols"])
    print(story)
    send_emails(story)

if __name__ == "__main__":
    main()