class Address:
    index: str
    city: str
    street: str
    house: str
    apartment: str
    
    def __init__(self, index: str, city: str, street: str, house: str, apartment: str) -> None:
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment