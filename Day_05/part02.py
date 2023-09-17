from math import ceil

with open("input", "r") as file:
    # Führe hier deine gewünschten Operationen mit der geöffneten Datei durch
    # Zum Beispiel: Daten lesen, schreiben oder verarbeiten
    input = file.read().split("\n")

seat_ID = []

for ticket in input:
    row_distance = [0, 127]
    row = ticket[:7]

    for r in row:
        tmp = int(ceil((row_distance[1] - row_distance[0]) / 2))
        if r == 'F':
            row_distance[1] -= tmp
        else:
            row_distance[0] += tmp
    min_row = min(row_distance)
    seat_distance = [0, 7]
    seat_anweisung = ticket[-3:]

    for seat in seat_anweisung:
        tmp = int(ceil((seat_distance[1] - seat_distance[0]) / 2))
        if seat == 'R':
            seat_distance[0] += tmp
        else:
            seat_distance[1] -= tmp
    max_seat = max(seat_distance)
    seat_ID.append(min_row * 8 + max_seat)

seat_ID = sorted(seat_ID)

start = seat_ID[0]
end = seat_ID[-1]
missing_seats = []

for seat in range(start, end):
    if not seat in seat_ID:
        missing_seats.append(seat)

my_seat = missing_seats[0]
print(my_seat)