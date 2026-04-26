import os

from src.database.database import products
from src.register.register_controller import ProductRegisterController
from src.register.register_view import RegisterView
from src.sales.sales_controller import SalesController


class SalesView:
    def __init__(self):
        self.products = products
        self.core = SalesController()

    def sale(self):
        try:
            print("======== SALES PRODUCTS ========")
            for product in self.products:
                print(f"{self.products.index(product)} - {product["name"]:<20} | QTD:{product["storage"]:<10} | R${product["price"]:.2f}")

            print(" ")
            product_index = int(input("Enter product index: "))
            customer_name = input("Enter customer name: ")
            quantity_sales = int(input("Enter quantity of products: "))

            report = self.core.sale(customer_name, quantity_sales, product_index)

            os.system('cls')
            print("Sale executed successfully")
            print("")
            self.show_report(report)
            input("Press Enter to continue...")

        except ValueError:
            print("Invalid input")

        except Exception as e:
            print(e)


    @staticmethod
    def show_report(report):
        print("======== REPORT SALE ========")
        print(f"{"Cutomer:": <14} {report["customer_name"]}")
        print(f"{"Product:": <14} {report["product"]}")
        print(f"{"Quantity Sale:": <14} {report["quantity_sales"]}")
        print(f"{"Total Amount:": <14} R${report["total_amount"]}")
        print(f"{"Discount:": <14} R${report["discounted_price"]}")
        print(f"{"Final Price:": <14} R${report["final_price"]}")


if __name__ == "__main__":
    register = ProductRegisterController()
    register.register_product("Camiseta preta", 39.90, 100)
    register.register_product("Calça jeans", 89.90, 60)
    register.register_product("Tênis esportivo", 199.99, 30)
    register.register_product("Boné", 25.00, 80)
    register.register_product("Jaqueta", 149.90, 20)
    register.register_product("Meia", 9.99, 200)
    register.register_product("Relógio", 250.00, 15)
    register.register_product("Mochila", 120.50, 40)
    register.register_product("Cinto", 35.75, 70)
    register.register_product("Óculos de sol", 99.90, 25)

    view = SalesView()
    view.sale()