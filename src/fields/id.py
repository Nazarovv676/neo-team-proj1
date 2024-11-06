from src.fields.field import Field


class Id(Field):
    """
    Class for record's Id field
    """

    def __init__(self, value):
        super().__init__(value)
