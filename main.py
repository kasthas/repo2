from sqlite3 import connect
from sys import argv, exit
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        db = connect("coffee.sqlite")
        cur = db.cursor()
        #cur.execute("create table if not exists info (id int primary key, type string, roast string, сonv string, desc string, price int, volume int)")
        #cur.execute("insert into info values(?, ?, ?, ?, ?, ?, ?)", (1, "Арабика", "Средняя", "Молотый", "Интенсивный, кислотный", 500, 100))
        data = cur.execute("select * from info").fetchall()
        uic.loadUi("main.ui", self)
        self.table.setRowCount(len(data))
        for i in range(len(data)):
            self.table.setItem(i, 0, QTableWidgetItem(str(data[i][0])))
            self.table.setItem(i, 1, QTableWidgetItem(data[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(data[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(data[i][3]))
            self.table.setItem(i, 4, QTableWidgetItem(data[i][4]))
            self.table.setItem(i, 5, QTableWidgetItem(str(data[i][5])))
            self.table.setItem(i, 6, QTableWidgetItem(str(data[i][6])))
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

def main():
    app = QApplication(argv)
    window = App()
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()