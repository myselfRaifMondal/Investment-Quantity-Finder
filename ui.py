import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox

class StockCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        self.stock_layout = QGridLayout()
        result_layout = QVBoxLayout()

        # Number of stocks input
        self.num_stocks_label = QLabel('Enter the number of stocks:')
        self.num_stocks_entry = QLineEdit()
        self.create_entries_button = QPushButton('Create Stock Entries')
        self.create_entries_button.clicked.connect(self.create_stock_entries)

        form_layout.addWidget(self.num_stocks_label)
        form_layout.addWidget(self.num_stocks_entry)
        form_layout.addWidget(self.create_entries_button)

        # Results display
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)

        result_layout.addWidget(self.results_text)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(self.stock_layout)
        main_layout.addLayout(result_layout)

        self.setLayout(main_layout)

        self.setWindowTitle('Stock Shares Calculator')
        self.show()

    def create_stock_entries(self):
        try:
            num_stocks = int(self.num_stocks_entry.text())

            # Clear previous entries
            for i in reversed(range(self.stock_layout.count())):
                widget = self.stock_layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

            self.stock_cmp_entries = []
            self.investment_entries = []

            for i in range(num_stocks):
                stock_cmp_label = QLabel(f'Stock {i+1} CMP:')
                stock_cmp_entry = QLineEdit()
                self.stock_cmp_entries.append(stock_cmp_entry)

                investment_label = QLabel(f'Stock {i+1} Investment:')
                investment_entry = QLineEdit()
                self.investment_entries.append(investment_entry)

                self.stock_layout.addWidget(stock_cmp_label, i, 0)
                self.stock_layout.addWidget(stock_cmp_entry, i, 1)
                self.stock_layout.addWidget(investment_label, i, 2)
                self.stock_layout.addWidget(investment_entry, i, 3)

            self.calculate_button = QPushButton('Calculate Shares')
            self.calculate_button.clicked.connect(self.calculate_shares)
            self.stock_layout.addWidget(self.calculate_button, num_stocks, 1, 1, 2)

        except ValueError:
            QMessageBox.critical(self, 'Input Error', 'Please enter a valid number')

    def calculate_shares(self):
        try:
            num_stocks = int(self.num_stocks_entry.text())
            self.results_text.clear()

            for i in range(num_stocks):
                stock_cmp = float(self.stock_cmp_entries[i].text())
                inv = float(self.investment_entries[i].text())
                margin = stock_cmp / 5
                num_shares = int(inv / margin)
                self.results_text.append(f'Stock {i+1}: Number of shares = {num_shares}\n')

        except ValueError:
            QMessageBox.critical(self, 'Input Error', 'Please enter valid numbers')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StockCalculator()
    sys.exit(app.exec_())

