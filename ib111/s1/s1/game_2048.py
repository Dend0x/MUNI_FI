from random import choice
import tkinter as tk

# change e_2048 below if your file name is different
import e_2048 as student

# game parameters; feel free to change them
ROW_SIZE = 17
NEW_NUMBERS = [2, 2, 2, 4]  # unwinnable, try [2] instead

BORDER = 32
CELL_SIZE = 64
FONT = ('system', '16')


def draw(canvas: tk.Canvas, row: list[int]) -> None:
    canvas.delete("all")
    for i, tile in enumerate(row):
        left = CELL_SIZE * i + BORDER
        canvas.create_rectangle(left, BORDER,
                                left + CELL_SIZE, BORDER + CELL_SIZE)
        if tile != 0:
            canvas.create_text(left + CELL_SIZE // 2, BORDER + CELL_SIZE // 2,
                               text=str(tile), font=FONT)


def add_random(row: list[int], candidates: list[int]) -> None:
    indices = [i for i, num in enumerate(row) if num == 0]
    if indices:
        row[choice(indices)] = choice(candidates)


def update(row: list[int], to_left: bool) -> None:
    result = student.slide(row, to_left)

    if result:
        add_random(row, NEW_NUMBERS)


def update_and_draw(row: list[int], to_left: bool, canvas: tk.Canvas) -> None:
    update(row, to_left)
    draw(canvas, row)


def reset_and_draw(row: list[int], canvas: tk.Canvas) -> None:
    for i in range(ROW_SIZE):
        row[i] = 0
    add_random(row, NEW_NUMBERS)
    draw(canvas, row)


def main() -> None:
    root = tk.Tk()
    canvas = tk.Canvas(
        width=2 * BORDER + ROW_SIZE * CELL_SIZE,
        height=2 * BORDER + CELL_SIZE,
    )
    row = [0 for _ in range(ROW_SIZE)]
    reset_and_draw(row, canvas)

    canvas.bind_all("<Left>", lambda _: update_and_draw(row, True, canvas))
    canvas.bind_all("<Right>", lambda _: update_and_draw(row, False, canvas))
    canvas.bind_all("r", lambda _: reset_and_draw(row, canvas))
    canvas.bind_all("q", lambda _: root.destroy())

    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
