#Zadanie 1
shop_list = {
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola']
}
for shop, products in shop_list.items():
    print(f"Idę do {shop} i kupuję tam {products}")

products_amount = len(shop_list.get("Piekarnia")) + len(shop_list.get("Warzywniak"))
print(f"W sumie kupuję {products_amount} produktów.")
