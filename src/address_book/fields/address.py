from src.address_book import Field

class Address(Field):
    """
    Class for record's Address field
    """
    def __init__(self, address: str):
        super().__init__(address)
    
