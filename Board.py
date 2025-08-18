class Board:
    def __init__(self):
        self.board = [0] * 128
        self.FILES = "abcdefgh"
        self.RANKS = "12345678"
    
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
        file_index = board_index & 0x0F
        rank_index = board_index >> 4
        return f"{self.FILES[file_index]}{self.RANKS[rank_index]}" 