#!/usr/bin/python3
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()

        # Match required header format (no leading spaces)
        print(' '.join(str(i) for i in range(self.width)))

        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                idx = y * self.width + x

                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        print('.', end=' ')  # mines shown as "."
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    # Hidden cells are blank spaces (not dots)
                    print(' ', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        idx = y * self.width + x

        if idx in self.mines:
            return False

        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def has_won(self):
        # Win when all non-mine cells are revealed
        revealed_cells = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.revealed[y][x]:
                    revealed_cells += 1

        total_cells = self.width * self.height
        safe_cells = total_cells - len(self.mines)
        return revealed_cells == safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Ignore out-of-bounds inputs
                if not (0 <= x < self.width and 0 <= y < self.height):
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()

