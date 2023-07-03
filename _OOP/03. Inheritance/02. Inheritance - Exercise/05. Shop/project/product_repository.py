from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        prod = next(filter(lambda x: x.name if x.name == product_name else None, self.products))
        return prod

    def remove(self, product_name: str):
        try:
            prod = next(filter(lambda x: x.name == product_name, self.products))
            self.products.remove(prod)
        except StopIteration:
            return None

    def __repr__(self):
        return '\n'.join(f'{x.name}: {x.quantity}' for x in self.products)
