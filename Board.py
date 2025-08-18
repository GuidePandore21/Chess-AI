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