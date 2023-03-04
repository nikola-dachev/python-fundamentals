budget= float(input())
flour_price_per_kg = float(input())
colored_eggs = 0
number_of_loaves = 0

eggs_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_litre = flour_price_per_kg * 1.25
milk_price_for_recipe = milk_price_per_litre / 4

price_per_bread = flour_price_per_kg +eggs_price_per_pack + milk_price_for_recipe

while budget > price_per_bread:
    colored_eggs += 3
    number_of_loaves += 1
    budget -= price_per_bread

    if number_of_loaves>0 and number_of_loaves % 3 ==0:
        colored_eggs -=(number_of_loaves -2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")