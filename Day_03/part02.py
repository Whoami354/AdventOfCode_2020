with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

going_different_way = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product_trees = 1
count_trees = 0

len_row = len(input[0])

for coor in going_different_way:
    x, y = 0, 0
    count_trees = 0

    while y < len(input):

        if input[y][x % len_row] == '#':
            count_trees += 1

        x += coor[0]
        y += coor[1]

    product_trees *= count_trees

print(product_trees)