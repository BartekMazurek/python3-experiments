# SET TRANSFORMATION

names = {"bart", "thomas", "aNDREW"}

capitalized_names = {
    name.capitalize()
    for name in names
}

print('Capitalized & sorted names: ', sorted(capitalized_names))
