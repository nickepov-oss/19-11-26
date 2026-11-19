import random


def create_pole(pole, size_y, size_x, empty_cell):
    for i in range(size_y):
        pole.append([empty_cell] * size_x)


def show_pole(pole):
    print()
    for row in pole:
        print(" ".join(row))
    print()


def user(pole, size_y, size_x, empty_cell, user_cell):
    while True:
        y = int(input(f"Row (1-{size_y}): ")) - 1
        x = int(input(f"Column (1-{size_x}): ")) - 1
        if 0 <= y < size_y and 0 <= x < size_x and pole[y][x] == empty_cell:
            pole[y][x] = user_cell
            break
        print("Try again")


def bot(pole, size_y, size_x, empty_cell, bot_cell):
    free = [(y, x) for y, row in enumerate(pole) for x, c in enumerate(row) if c == empty_cell]
    if free:
        y, x = random.choice(free)
        pole[y][x] = bot_cell


def win(pole, empty_cell):
    n = len(pole)
    lines = list(pole)
    lines += [[row[i] for row in pole] for i in range(n)]
    lines.append([pole[i][i] for i in range(n)])
    lines.append([pole[i][n - 1 - i] for i in range(n)])

    it = iter(lines)
    for line in it:
        first = next(iter(line))
        if first != empty_cell and all(cell == first for cell in line):
            return first

    if all(cell != empty_cell for row in pole for cell in row):
        return "DRAW"
    return None


size_y = 3
size_x = 3
pole = []

empty_cell = "[_]"
bot_cell = "[0]"
user_cell = "[X]"

create_pole(pole, size_y, size_x, empty_cell)

while True:
    show_pole(pole)
    user(pole, size_y, size_x, empty_cell, user_cell)
    res = win(pole, empty_cell)
    if res:
        break

    bot(pole, size_y, size_x, empty_cell, bot_cell)
    res = win(pole, empty_cell)
    if res:
        break

show_pole(pole)
if res == user_cell:
    print("You win!")
elif res == bot_cell:
    print("Bot wins!")
else:
    print("Draw!")