from src.database.database import products

class ProductRegisterController:
    def __init__(self):
        pass


    def register_product(self, name:str, price:float, initial_storage:int):
        """Register a new product in system"""
        self.validate_product(name, price, initial_storage)
        product = {
            "name": name,
            "price": price,
            "storage": initial_storage
        }
        products.append(product)


    @staticmethod
    def validate_product(name:str, price:float, initial_storage:int):
        """Check if all requirements have been met."""

        if not name:
            raise Exception('Name cannot be empty')

        for product in products:
            if product["name"].lower() == name.lower():
                raise Exception('Product name already exists')

        if not price > 0:
            raise Exception("Price cannot be negative or zero")

        if not initial_storage >= 0:
            raise Exception("Initial Storage cannot be negative")


