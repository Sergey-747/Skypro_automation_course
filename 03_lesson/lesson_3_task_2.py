from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Xiaomi 15 Pro", "+79132334567" ), 
    Smartphone("Asus", "Asus ROG Phone 9 Pro", "+79912345678"),
    Smartphone("Appole", "Appole 12", "+79132334567" ), 
    Smartphone("Xiaomi", "Xiaomi Redmi 10C", "+79138544567"),
    Smartphone("OPPO", "OPPO Find X9 Pro", "+79912348756"),
    Smartphone("CMF Phone", "CMF Phone 2 Pro", "+79036812345")
]

for infa in catalog:
    print(f"{infa.brand} - {infa.model}. {infa.namber}")
   