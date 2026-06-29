# to_address  (тип данных Address);
# from_address  (тип данных Address);
# cost  ( стоимость - тип данных число);
# track  (трек-номером - тип данных строка).
from address import Address

class Mailing:
    to_address: Address
    from_address: Address
    cost: float
    track: str
    
    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track


