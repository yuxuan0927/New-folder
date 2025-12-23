import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current game board"""
        print("\n    1   2   3")
        print(f"a  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("  ___|___|___")
        print(f"b  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("  ___|___|___")
        print(f"c  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")
        print()
    
    def make_move(self, row, col):
        """Make a move on the board"""
        if self.board[row][col] != ' ':
            return False
        self.board[row][col] = self.current_player
        return True
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_game(self):
        """Reset the game board and start with player X"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def get_position_input(self):
        """Get valid position input from the player using coordinates (a-c, 1-3)"""
        while True:
            position = input(f"Player {self.current_player}, enter position (e.g., a1, b2, c3) or 'z' to restart: ").strip().lower()
            
            # Check for restart command
            if position == 'z':
                return 'restart'
            
            if len(position) != 2:
                print("Please enter a coordinate in the format: letter (a-c) and number (1-3), e.g., 'a1' or 'b2', or 'z' to restart")
                continue
            
            row_letter = position[0]
            col_str = position[1]
            
            # Validate row letter (a, b, c)
            if row_letter not in ['a', 'b', 'c']:
                print("Row must be 'a', 'b', or 'c'")
                continue
            
            # Validate column number (1, 2, 3)
            try:
                col_num = int(col_str)
                if col_num < 1 or col_num > 3:
                    print("Column must be 1, 2, or 3")
                    continue
            except ValueError:
                print("Column must be a number (1, 2, or 3)")
                continue
            
            # Convert to indices
            row = ord(row_letter) - ord('a')  # a=0, b=1, c=2
            col = col_num - 1  # 1=0, 2=1, 3=2
            
            return row, col
    
    def play(self):
        """Main game loop"""
        print("Welcome to Tic-Tac-Toe!")
        print("Use coordinates: letter (a-c) for row, number (1-3) for column")
        print("Example: a1, b2, c3")
        print("Press 'z' at any time to restart the game")
        print("\n    1   2   3")
        print("     |   |   ")
        print("a    |   |   ")
        print("  ___|___|___")
        print("     |   |   ")
        print("b    |   |   ")
        print("  ___|___|___")
        print("     |   |   ")
        print("c    |   |   ")
        print("\nLet's start!\n")
        
        while True:
            self.display_board()
            
            # Get player move
            result = self.get_position_input()
            
            # Check if player wants to restart
            if result == 'restart':
                clear_screen()
                print("🔄 Restarting game...\n")
                print("Welcome to Tic-Tac-Toe!")
                print("Use coordinates: letter (a-c) for row, number (1-3) for column")
                print("Example: a1, b2, c3")
                print("Press 'z' at any time to restart the game")
                print("\n    1   2   3")
                print("     |   |   ")
                print("a    |   |   ")
                print("  ___|___|___")
                print("     |   |   ")
                print("b    |   |   ")
                print("  ___|___|___")
                print("     |   |   ")
                print("c    |   |   ")
                print("\nLet's start!\n")
                self.reset_game()
                continue
            
            row, col = result
            
            # Try to make the move
            if not self.make_move(row, col):
                print("That position is already taken! Try again.")
                continue
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"🎉 Player {winner} wins! 🎉")
                break
            
            # Check for tie
            if self.is_board_full():
                self.display_board()
                print("It's a tie! 🤝")
                break
            
            # Switch player
            self.switch_player()


def main():
    """Main function to run the game"""
    while True:
        game = TicTacToe()
        game.play()
        
        # Ask if players want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
