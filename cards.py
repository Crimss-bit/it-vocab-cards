import csv
import random
def load_terms(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

terms = load_terms("terms.csv")
random.shuffle(terms)
score = 0

for card in terms:
    print()
    print(card["jp"], f"({card['reading']})")
    answer = input("English")
    if answer.strip().lower() == card ["en"].lower():
       print("correct!")
       score = score + 1
    else:
       print("Wrong. Answer", card["en"])

print()
print(f"Score: {score}/{len(terms)}")

print(card["jp"], f"({card['reading']})")
input("Press Enter to see the answer...")
print("EN:", card["en"])
