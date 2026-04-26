import os

from src.database.database import products
from src.register.register_view import RegisterView
from src.report.report_view import ReportView
from src.sales.sales_view import SalesView


class main:
    def __init__(self):
        self.products = products
        self.register = RegisterView()
        self.sales = SalesView()
        self.report = ReportView()

    @staticmethod
    def show_menu():
        print("============ MENU ============")
        print("1 - Show Products")
        print("2 - Register Product")
        print("3 - Sale Product")
        print("4 - Report Menu")
        print("5 - Exit Program")
        print("==============================")


    def execute(self):
        while True:
            os.system('cls')
            self.show_menu()
            print(" ")
            option = input("Select an option: ")
            match option:
                case "1":
                    os.system('cls')
                    self.show_products()


                case "2":
                    os.system('cls')
                    self.register.register_product()


                case "3":
                    os.system('cls')
                    self.sales.sale()


                case "4":
                    os.system('cls')
                    self.report.show()


                case "5":
                    os.system('cls')
                    break

                case _:
                    print("Invalid option")
                    input("Press enter to continue...")
        print("Goodbye")


    def show_products(self):
        if not self.products:
            print("No products selected")

        for product in self.products:
            print(f"{self.products.index(product)} - {product["name"]:<20} | QTD:{product["storage"]:<10} | R${product["price"]:.2f}")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main = main()
    main.execute()