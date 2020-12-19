import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from converter import Ui_MainWindow
from pprint import pprint
import requests

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.converter = Ui_MainWindow()
        self.converter.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QIcon('icon.png'))

        self.converter.input_currency.setPlaceholderText('Из валюты:')
        self.converter.input_amount.setPlaceholderText('У меня есть:')
        self.converter.output_currency.setPlaceholderText('В валюту:')
        self.converter.output_amount.setPlaceholderText('Я получу:')
        self.converter.pushButton.clicked.connect(self.convert)

    def convert(self):
        input_currency = self.converter.input_currency.text()
        output_currency = self.converter.output_currency.text()

        url = 'https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=0f15d88c2b2525145c0b'.format(input_currency, output_currency)
        res = requests.get(url)
        data = res.json()

        input_amount = int(self.converter.input_amount.text())
        output_amount = round(input_amount * data[input_currency + '_' + output_currency], 2)

        self.converter.output_amount.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())