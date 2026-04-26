from src.database.database import reports
class ReportController:
    def __init__(self):
        self.reports = reports


    def create_sale_report(self, customer_name, product_name, quantity_sale, total_amount, discount, final_price):
        sale_report = {
            "customer_name": customer_name,
            "product": product_name,
            "quantity_sales": quantity_sale,
            "total_amount": total_amount,
            "discounted_price": discount,
            "final_price": final_price,
        }
        self.reports.append(sale_report)
        return  sale_report


    @staticmethod
    def save_in_text_file(report):
        content = (
            f"\n--- REPORT ---\n"
            f"Customer: {report['customer_name']}\n"
            f"Product: {report['product']}\n"
            f"Quantity Sale: {report['quantity_sales']}\n"
            f"Total Amount: {report['total_amount']}\n"
            f"Discount: {report['discounted_price']}\n"
            f"Final Price: {report['final_price']}\n"
        )

        with open("report.txt", "w", encoding="utf-8") as file:
            file.write(content)
            file.close()

    def save_all_reports_in_text_file(self):
        for report in self.reports:
            self.save_in_text_file(report)


