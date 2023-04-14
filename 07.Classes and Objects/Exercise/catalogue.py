class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [prod for prod in self.products if prod.startswith(first_letter)]

    def __repr__(self):
        item_to_return = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{item_to_return}"

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.products)
print(catalogue.get_by_letter("C"))
print(catalogue)

