with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

answers_field = []
sum_answers = 0

def check_formular(answers):
    letters = ''.join(answers)
    unique_yes = set()

    for letter in letters:
        isIn = True
        for group in answers:
            if not letter in group:
                isIn = False

        if isIn:
            unique_yes.add(letter)
    return len(unique_yes)

for questions in input:
    if questions != '':
        answers_field.append(questions)
    else:
        sum_answers += check_formular(answers_field)
        answers_field.clear()

print(sum_answers)