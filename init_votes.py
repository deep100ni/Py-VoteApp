import json
import random

# Read the candidates.json file
with open('candidates.json', 'r') as file:
    candidates = json.load(file)

# Initialize votes dictionary
votes = {}

# Generate votes for each position
for position, candidate_list in candidates.items():
    votes[position] = {}

    for candidate in candidate_list:
        candidate_key = candidate
        votes[position][candidate_key] = 0

# Write the votes to votes.json
with open('votes.json', 'w') as file:
    json.dump(votes, file, indent=4)

print("votes.json has been generated.")
