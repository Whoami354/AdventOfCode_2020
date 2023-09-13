with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

countPwd = 0

def valid_pwd(letters, first_pos, second_pos, main_letter):
    return bool(letters[first_pos] == main_letter) ^ bool(letters[second_pos] == main_letter)

for password in input:
    password = password.split()
    common = [int(number) for number in password[0].split('-')]
    first_pos, second_pos = common[0], common[1]
    main_letter = password[1][:-1]
    letters = password[-1]

    if valid_pwd(letters, first_pos - 1, second_pos - 1, main_letter):
        countPwd += 1

print(countPwd)