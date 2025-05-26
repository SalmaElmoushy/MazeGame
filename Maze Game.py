import sys
import time

class MazeGame:
    EMPTY = 0
    WALL = 1
    PLAYER = 5
    DESTINATION = 9

    def __init__(self):
        self.maze = [[self.WALL, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                     [self.EMPTY, self.WALL, self.WALL, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.WALL, self.EMPTY, self.EMPTY],
                     [self.EMPTY, self.EMPTY, self.EMPTY, self.WALL, self.WALL, self.WALL, self.EMPTY, self.WALL, self.WALL, self.WALL],
                     [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.WALL, self.WALL, self.EMPTY],
                     [self.WALL, self.EMPTY, self.WALL, self.EMPTY, self.EMPTY, self.WALL, self.WALL, self.WALL, self.EMPTY, self.EMPTY],
                     [self.EMPTY, self.EMPTY, self.WALL, self.EMPTY, self.EMPTY, self.WALL, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                     [self.EMPTY, self.WALL, self.EMPTY, self.WALL, self.WALL, self.WALL, self.WALL, self.EMPTY, self.EMPTY, self.EMPTY],
                     [self.WALL, self.WALL, self.WALL, self.EMPTY, self.EMPTY, self.WALL, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY],
                     [self.WALL, self.WALL, self.EMPTY, self.WALL, self.EMPTY, self.WALL, self.EMPTY, self.WALL, self.WALL, self.EMPTY],
                     [self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.WALL, self.WALL, self.WALL, self.DESTINATION, self.EMPTY]]

        self.row = 0
        self.col = 0
        self.lives = 3
        self.again = True

    def displayMaze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == self.PLAYER:
                    print("x", end="")
                elif self.maze[i][j] == self.WALL:
                    print(" ", end="")
                elif self.maze[i][j] == self.EMPTY:
                    print("-", end="")
                elif self.maze[i][j] == self.DESTINATION:
                    print("*", end="")
            print()

    def playGame(self):
        while self.maze[9][9] != self.PLAYER:
            d = input("Enter direction (w/a/s/d) or 'x' to exit: ").lower()
            if d == "w":
                self.moveUp()
            elif d == "s":
                self.moveDown()
            elif d == "a":
                self.moveLeft()
            elif d == "d":
                self.moveRight()
            elif d == "x":
                print("End of the program")
                self.again = False
                break
            else:
                print("Wrong input")
            self.displayMaze()
        
        if self.again:
            print("Congratulations! You won.")
    
    def moveUp(self):
        if self.row == 0 or self.maze[self.row - 1][self.col] == self.WALL:
            print("Invalid command! Try again.")
            self.lives -= 1
            print("You have", self.lives, "lives left.")
        else:
            self.maze[self.row][self.col] = self.EMPTY
            self.row -= 1
            self.maze[self.row][self.col] = self.PLAYER
        
        if self.lives == 0:
            print("Sorry, you lost all your lives.")
            self.again = input("Do you want to play again? (yes/no): ").lower() == "yes"
            if not self.again:
                sys.exit(0)
            else:
                self.lives = 3

    def moveDown(self):
        if self.row == 9 or self.maze[self.row + 1][self.col] == self.WALL:
            print("Invalid command! Try again.")
            self.lives -= 1
            print("You have", self.lives, "lives left.")
        else:
            self.maze[self.row][self.col] = self.EMPTY
            self.row += 1
            self.maze[self.row][self.col] = self.PLAYER
        
        if self.lives == 0:
            print("Sorry, you lost all your lives.")
            self.again = input("Do you want to play again? (yes/no): ").lower() == "yes"
            if not self.again:
                sys.exit(0)
            else:
                self.lives = 3

    def moveLeft(self):
        if self.col == 0 or self.maze[self.row][self.col - 1] == self.WALL:
            print("Invalid command! Try again.")
            self.lives -= 1
            print("You have", self.lives, "lives left.")
        else:
            self.maze[self.row][self.col] = self.EMPTY
            self.col -= 1
            self.maze[self.row][self.col] = self.PLAYER
        
        if self.lives == 0:
            print("Sorry, you lost all your lives.")
            self.again = input("Do you want to play again? (yes/no): ").lower() == "yes"
            if not self.again:
                sys.exit(0)
            else:
                self.lives = 3

    def moveRight(self):
        if self.col == 9 or self.maze[self.row][self.col + 1] == self.WALL:
            print("Invalid command! Try again.")
            self.lives -= 1
            print("You have", self.lives, "lives left.")
        else:
            self.maze[self.row][self.col] = self.EMPTY
            self.col += 1
            self.maze[self.row][self.col] = self.PLAYER
        
        if self.lives == 0:
            print("Sorry, you lost all your lives.")
            self.again = input("Do you want to play again? (yes/no): ").lower() == "yes"
            if not self.again:
                sys.exit(0)
            else:
                self.lives = 3


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 10:
        print("Sorry, you are too young for the game.")
        sys.exit(1)
    else:
        print("Hi", name + "! Let's start! The rules are simple:")
        time.sleep(2)
        print("Your task is to reach the star (*)")
        time.sleep(2)
        print("Use 'w' (move up), 's' (move down), 'd' (move right), and 'a' (move left).")
        time.sleep(2)
        print("Note: You have only 3 lives.")
        time.sleep(2)

    game = MazeGame()
    game.displayMaze()
    game.playGame()
