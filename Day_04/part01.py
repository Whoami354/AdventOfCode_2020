with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

def check_validate(passport):
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in passport_fields:
        if not field in passport:
            return False

    return True

for_passport = ""
count_valid_passport = 0

for values in input:
    if values == "":
        if check_validate(for_passport):
            count_valid_passport += 1
        for_passport = ""
    else:
        for_passport += values

print(count_valid_passport)