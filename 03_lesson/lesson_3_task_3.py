from address import Address
from mailing import Mailing

to_adr = Address("656004", "Барнаул", "Полевая", "4", "1")
from_adr = Address("101000", "Москва", "Стрелецкая", "201", "2")

shipment = Mailing(to_address=to_adr,from_address=from_adr,cost=350.50,track="RU817273172CN")
print(
    f"Отправление {shipment.track} из " 
    f"{shipment.from_address.index}, {shipment.from_address.city}, {shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} в "
    f"{shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, {shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей.")