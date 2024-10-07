# 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the     value from the second dictionary should be used.

colours = {
    "Derek": "Red",
    "Michael": "Purple",
    "Marianne": "Green"
}

snacks = {
    "Daniel": "Peanuts",
    "Michael": "Crisps",
    "Joanne": "Raisins"
}


favourites = {}

for key, value in colours.items():
    favourites[key] = value

for key, value in snacks.items():
    favourites[key] = value

print(favourites)