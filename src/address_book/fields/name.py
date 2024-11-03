from src.address_book import Field


class Name(Field):
    """
    Class for record's Name field
    """

    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self) -> str:
        return super().__str__()
