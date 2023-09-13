with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")
    input = [int(number) for number in input]

for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i] * input[j])

