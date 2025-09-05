#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Mines must be fewer than total cells")
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.safe_cells = width * height - mines
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        ch = '*'
                    else:
                        cnt = self.count_mines_nearby(x, y)
                        ch = str(cnt) if cnt > 0 else ' '
                else:
                    ch = '.'
                print(ch, end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:   # don't count the cell itself
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # bounds + repeated click guard
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # ignore out-of-bounds as a no-op
        if self.revealed[y][x]:
            return True

        # mine?
        if (y * self.width + x) in self.mines:
            return False

        # reveal current
        self.revealed[y][x] = True
        self.revealed_count += 1

        # flood fill for zeros
        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    self.reveal(x + dx, y + dy)
        return True

    def won(self):
        return self.revealed_count == self.safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter…")
                continue

            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Out of bounds. Try again.")
                input("Press Enter…")
                continue

            i

