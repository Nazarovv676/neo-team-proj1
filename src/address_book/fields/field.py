class Field:
    """
    Base class for record fields
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)
