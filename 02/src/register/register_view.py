import os

from src.register.register_controller import ProductRegisterController


class RegisterView:
    def __init__(self):
        self.core = ProductRegisterController()

    def register_product(self):
        try:
            os.system('cls')
            print("======== REGISTERS PRODUCTS ========")
            name = input("Name of product: ")
            price = float(input("Price: "))
            initial_storage = int(input("Initial Storage: "))

            self.core.register_product(name, price, initial_storage)
            print("Product registered successfully!")

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print(e)



if __name__ == "__main__":
    view = RegisterView()
    view.register_product()