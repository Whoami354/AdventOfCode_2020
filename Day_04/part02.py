with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

def check_actual_field(field):
    field_first = field.split(":")[0]
    field_second = field.split(":")[1]

    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if field_second.isdigit() and field_first != "pid" and field_first != "hgt":
        field_second = int(field_second)

    if field_first == "byr":
        return 1920 <= field_second <= 2002
    if field_first == "iyr":
        return 2010 <= field_second <= 2020
    if field_first == "eyr":
        return 2020 <= field_second <= 2030
    if field_first == "hgt":
        if not field_second.endswith("cm") and not field_second.endswith("in"):
            return False
        else:
            height = field_second[-2:]
            val = int(field_second[:-2])
            if height == "cm":
                return 150 <= val <= 193
            else:
                return 59 <= val <= 76
    if field_first == "hcl":
        if len(field_second) < 7:
            return False
    if field_first == "ecl":
        if len(field_second) > 3:
            return False
        else:
            return field_second in eye_colors
    if field_first == "pid":
        if len(field_second) != 9:
            return False
    return True

def check_validate(passport):
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    allFields = ' '.join(passport)

    for field in passport_fields:
        if not field in allFields:
            return False

    passport.pop()

    k = 0
    while k < len(passport):
        if not check_actual_field(passport[k]):
            return False

        k += 1

    return True


for_passport = ""
count_valid_passport = 0

for values in input:
    if values == "":
        if check_validate(for_passport.split(" ")):
            count_valid_passport += 1
        for_passport = ""
    else:
        for_passport += values + " "

print(count_valid_passport)
