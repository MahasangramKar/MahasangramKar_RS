coordinates = [(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]
even_coords = []

for x, y in coordinates:
    if x % 2 == 0 and y % 2 == 0:
        even_coords.append((x, y))

print(even_coords)
