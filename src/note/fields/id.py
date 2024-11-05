from src.address_book import Field


class Id(Field):

    """
    Class for note's ID field
    """

    def __init__(self, id: int):
        super().__init__(id)

    def __str__(self) -> str:
        return super().__str__()
