with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

answers = set()
sum_answers = 0

for questions in input:
    if questions != '':
        for question in questions:
            answers.add(question)
    else:
        sum_answers += len(answers)
        answers.clear()

print(sum_answers)