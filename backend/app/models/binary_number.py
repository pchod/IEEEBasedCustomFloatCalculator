# binary_number.py

class BinaryNumber:
    """Represents a binary number in a scientific notation form"""

    def __init__(
        self,
        binary_whole_part: str = None,
        binary_fraction: str = None,
        is_positive: bool = None,
        
    ):
        self.binary_whole_part = binary_whole_part
        self.binary_fraction = binary_fraction
        self.is_positive = is_positive
