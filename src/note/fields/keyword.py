from src.fields.field import Field


class Keyword(Field):

    """
    Class for note's Kayword field
    """

    def __init__(self, keyword: str):
        super().__init__(keyword)

    def __str__(self) -> str:
        return super().__str__()
