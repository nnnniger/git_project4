import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem
import sqlite3


class Espreso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.setWindowTitle("кофе")
        self.setGeometry(100, 100, 800, 600)

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Сорт", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"])

        self.table.move(10, 10)

        self.conn = sqlite3.connect("coffee.sqlite")
        self.cursor = self.conn.cursor()

        self.populate_table()

    def populate_table(self):
        self.cursor.execute("SELECT * FROM coffee")
        coffee_data = self.cursor.fetchall()

        self.table.setRowCount(len(coffee_data))
        for row, coffee in enumerate(coffee_data):
            for col, data in enumerate(coffee):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row, col, item)

    def closeEvent(self, event):
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Espreso()
    window.show()
    sys.exit(app.exec_())
