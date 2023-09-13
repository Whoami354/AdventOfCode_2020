with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

x,y = 0, 0
count_trees = 0
len_row = len(input[0])

while y < len(input):

    if input[y][x % len_row] == '#':
        count_trees += 1

    y += 1
    x += 3

print(count_trees)