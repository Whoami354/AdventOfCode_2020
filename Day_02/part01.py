with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

countPwd = 0

def valid_pwd(letters, min, max, main_letter):
    count = 0
    for letter in letters:
        if letter == main_letter:
            count += 1
    return min <= count <= max

for password in input:
    password = password.split()
    common = [int(number) for number in password[0].split('-')]
    min, max = common[0], common[1]
    main_letter = password[1][:-1]
    letters = password[-1]

    if valid_pwd(letters, min, max, main_letter):
        countPwd += 1

print(countPwd)