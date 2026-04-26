from src.database.database import products,reports
from src.report.report_controller import ReportController


class SalesController:
    def __init__(self):
        self.products = products
        self.report_core = ReportController()

    def sale(self, name_customer:str, quantity_sales:int, product_index:int):
        self.sales_validate(name_customer, quantity_sales, product_index)
        product = self.products[product_index]

        total_amount = quantity_sales * product["price"]
        discount = self.calculate_discount(quantity_sales, total_amount)
        final_price = total_amount - discount

        sale_report = self.report_core.create_sale_report(name_customer, product["name"], quantity_sales, total_amount, discount, final_price)

        product["storage"] -= quantity_sales
        self.products[product_index] = product

        return sale_report



    @staticmethod
    def calculate_discount(quantity_sales:int, price:float):
        if quantity_sales > 10:
            discount = price * 0.05
            return discount
        return 0



    def sales_validate(self, name_customer:str, quantity_sales:int, product_index:int):
        if not name_customer:
            raise Exception('Name cannot be empty!')

        if not quantity_sales >= 0:
            raise Exception('Quantity cannot be empty!')

        if not len(self.products) > product_index-1:
            raise Exception('Product index invalid!')

        if not self.products[product_index]["storage"] > quantity_sales:
            raise Exception('Quantity cannot be greater than product quantity!')


# /*
#         > pegar produto (*)
#         > validar produto (*)
#         > quantidade vendida (*)
#         > nome cliente (*)