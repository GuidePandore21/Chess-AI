class Board:
    def __init__(self):
        self.board = [0] * 128
        self.FILES = "abcdefgh"
        self.RANKS = "12345678"
        P, N, B, R, Q, K = 1, 2, 3, 4, 5, 6
        WHITE, BLACK = 1, -1
    
    def coords_to_index(self, file_index, rank_index):
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
    
    def index_to_coords(self, board_index):
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

    def set_piece(self, index, piece):
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