import csv
import random
def load_terms(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

terms = load_terms("terms.csv")
card = random.choice(terms)

print(card["jp"], f"({card['reading']})")
input("Press Enter to see the answer...")
print("EN:", card["en"])
