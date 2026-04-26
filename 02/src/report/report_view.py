from src.report.report_controller import ReportController


class ReportView:
    def __init__(self):
        self.core = ReportController()
        pass

    def show(self):
        print("1 - Show all reports")
        print("2 - Save report")
        print("3 - exit")

        option = input("Enter your choice: ")
        match option:
            case "1":
                self.show_report()
                input("Press Enter to continue...")

            case "2":
                self.core.save_all_reports_in_text_file()

            case "3":
                return

            case _:
                print("Invalid option")


    def show_report(self):
        for report in self.core.reports:
            print(" ")
            print("----------------------------------------------")
            print(f"{"Cutomer:": <14} {report["customer_name"]}")
            print(f"{"Product:": <14} {report["product"]}")
            print(f"{"Quantity Sale:": <14} {report["quantity_sales"]}")
            print(f"{"Total Amount:": <14} R${report["total_amount"]}")
            print(f"{"Discount:": <14} R${report["discounted_price"]}")
            print(f"{"Final Price:": <14} R${report["final_price"]}")

