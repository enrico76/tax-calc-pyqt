from decimal import Decimal


class Logic:

    def calculate_tax(self):
        price = Decimal(self.price_box.text())
        tax = Decimal(self.box_taxrate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: {:.2f}".format(total_price)
        total_2nd_window = "I Soldi totale sono: {:.2f}".format(total_price)
        self.label_result.setText(total_price_string)










