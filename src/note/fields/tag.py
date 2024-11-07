from src.fields.field import Field


class Tag(Field):

    """
    Class for note's Tag field
    """

    def __init__(self, tag: str):
        super().__init__(tag)

    def __str__(self) -> str:
        return super().__str__()
