class Board:
    def __init__(self):
        self.board = [0] * 128
        self.FILES = "abcdefgh"
        self.RANKS = "12345678"
        self.P, self.N, self.B, self.R, self.Q, self.K = 1, 2, 3, 4, 5, 6
        self.WHITE, self.BLACK = 1, -1
    
    def coords_to_index(self, file_index : int, rank_index : int) -> int:
        """Converts file and rank indices to a board index.
        Args:
            file_index (int): Index of the file (0-7).
            rank_index (int): Index of the rank (0-7).
        Returns:
            int: The board index corresponding to the file and rank indices.
        Raises:
            ValueError: If file_index or rank_index are out of bounds (0-7).
        """
        if not (0 <= file_index < 8) or not (0 <= rank_index < 8):
            raise ValueError("File and rank indices must be between 0 and 7")
        return rank_index << 4 | file_index
    
    def index_to_coords(self, board_index : int) -> str:
        """Converts a board index to file and rank indices.
        Args:
            board_index (int): The board index (0-127).
        Returns:
            str: The coordinates in the format "file_rank" (e.g., "a1", "h8").
        Raises:
            ValueError: If board_index is out of bounds (0-127).
        """
        if not 0 <= board_index < 128:
            raise ValueError("Index out of bounds")
        file_index = board_index & 0x0F
        rank_index = board_index >> 4
        return f"{self.FILES[file_index]}{self.RANKS[rank_index]}"

    def set_piece(self, index : int, piece : int) -> None:
        """Sets a piece at the specified board index.
        Args:
            index (int): The board index (0-127).
            piece (int): The piece to place on the board.
        Raises:
            ValueError: If index is out of bounds (0-127).
        """
        if not 0 <= index < 128:
            raise ValueError("Index out of bounds")
        self.board[index] = piece
    
    def set_start_position_pieces(self) -> None:
        """Sets the starting position of pieces on the board.
        This method initializes the board with the standard chess starting position.
        """
        back = [self.R, self.N, self.B, self.Q, self.K, self.B, self.N, self.R]
        for f in range(8):
            self.set_piece(self.coords_to_index(f, 0), back[f] * self.WHITE)
            self.set_piece(self.coords_to_index(f, 1), self.P * self.WHITE)
            self.set_piece(self.coords_to_index(f, 6), self.P * self.BLACK)
            self.set_piece(self.coords_to_index(f, 7), back[f] * self.BLACK)
    
    def display_board(self) -> None:
        """Displays the current state of the board in a human-readable format.
        This method prints the board with ranks and files labeled, showing pieces
        in their respective positions. White pieces are uppercase, black pieces are lowercase.
        """
        rows = []
        for rank in reversed(range(8)):
            line = []
            for file in range(8):
                piece = self.board[self.coords_to_index(file, rank)]
                character_to_display = "."
                if piece != 0:
                    t = abs(piece)
                    character_to_display = {self.P:"P", self.N:"N", self.B:"B", self.R:"R", self.Q:"Q", self.K:"K"}[t]
                    if piece < 0:
                        character_to_display = character_to_display.lower()
                line.append(character_to_display)
            rows.append(f"{rank + 1} " + " ".join(line))
        print("\n".join(rows))
        print("  a b c d e f g h")
    
    # -------------------- Moves --------------------
    
    def get_piece_at(self, file_index : int, rank_index : int) -> int:
        """Gets the piece at the specified file and rank indices.
        Args:
            file_index (int): Index of the file (0-7).
            rank_index (int): Index of the rank (0-7).
        Returns:
            int: The piece at the specified position, or 0 if empty.
        Raises:
            ValueError: If file_index or rank_index are out of bounds (0-7).
        """
        index = self.coords_to_index(file_index, rank_index)
        return self.board[index]
    
    def get_piece_at_index(self, index : int) -> int:
        """Gets the piece at the specified board index.
        Args:
            index (int): The board index (0-127).
        Returns:
            int: The piece at the specified index, or 0 if empty.
        Raises:
            ValueError: If index is out of bounds (0-127).
        """
        if not 0 <= index < 128:
            raise ValueError("Index out of bounds")
        return self.board[index]
    