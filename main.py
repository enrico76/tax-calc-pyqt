from logic import Logic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QSpinBox

import sys


class MainWindow(QMainWindow, Logic):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("First window")
        self.setGeometry(0,0,399,382)
        self.price_box = QLineEdit("", self)
        self.price_box.setGeometry(220, 100, 113, 22)
        self.price_label = QLabel("Price", self)
        self.price_label.setGeometry(100,100,49,16)
        self.box_taxrate = QSpinBox(self)
        self.box_taxrate.setGeometry(290,160,42,22)
        self.box_taxrate.setValue(22)
        self.label_taxrate = QLabel("Tax Rate", self)
        self.label_taxrate.setGeometry(100,160,49,16)
        self.button_calc = QPushButton("Calculate", self)
        self.button_calc.setGeometry(250,230,75,24)
        self.label_result = QLabel("", self)
        self.label_result.setGeometry(120,280,201,41)

        self.button_calc.clicked.connect(self.calculate_tax)
        self.button_calc.clicked.connect(self.show_new_window)

    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()
        total_price_string = self.label_result.text()
        print(total_price_string)
        self.w.label_2nd_win.setText(total_price_string)


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(500, 150, 300, 200)
        self.label_2nd_win = QLabel('TEST', self)
        self.label_2nd_win.setGeometry(50,50,201,41)
        self.button_2nd_win = QPushButton("Hola", self)
        self.button_2nd_win.setGeometry(100,100,75,24)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
