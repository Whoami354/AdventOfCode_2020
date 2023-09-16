with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

def check_actual_field(field):
    field_form = field.split(":")[0]
    field_value = field.split(":")[1]

    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if field_value.isdigit() and field_form != "pid" and field_form != "hgt":
        field_value = int(field_value)

    if field_form == "byr":
        return 1920 <= field_value <= 2002
    if field_form == "iyr":
        return 2010 <= field_value <= 2020
    if field_form == "eyr":
        return 2020 <= field_value <= 2030
    if field_form == "hgt":
        if not field_value.endswith("cm") and not field_value.endswith("in"):
            return False
        else:
            height = field_value[-2:]
            val = int(field_value[:-2])
            if height == "cm":
                return 150 <= val <= 193
            else:
                return 59 <= val <= 76
    if field_form == "hcl":
        return len(field_value) == 7
    if field_form == "ecl":
        if len(field_value) > 3:
            return False
        else:
            return field_value in eye_colors
    if field_form == "pid":
        return len(field_value) == 9

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