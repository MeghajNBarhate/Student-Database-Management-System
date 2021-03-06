from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow8(object):

    def seehw(self):
        divhw = str(self.divselect.currentText())
        conn = sqlite3.connect("Databases\HW_"+divhw+".db")
        c = conn.cursor()
        q = "SELECT * FROM hw_data"
        res = conn.execute(q)
        for rno, rdta in enumerate(res):
            self.tableWidget.insertRow(rno)
            for colno, coldata in enumerate(rdta):
                self.tableWidget.setItem(rno, colno, QtWidgets.QTableWidgetItem(str(coldata)))
        conn.close()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 407)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.971591, y2:0.494, stop:0.0738636 rgba(85, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-130, 0, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 491, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,130)
        self.tableWidget.setColumnWidth(1,95)
        self.tableWidget.setColumnWidth(2,230)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.divselect = QtWidgets.QComboBox(self.centralwidget)
        self.divselect.setGeometry(QtCore.QRect(20, 70, 221, 41))
        self.divselect.setObjectName("divselect")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.divselect.addItem("")
        self.viewhw_button = QtWidgets.QPushButton(self.centralwidget)
        self.viewhw_button.setGeometry(QtCore.QRect(290, 70, 221, 41))
        self.viewhw_button.setObjectName("viewhw_button")
        self.viewhw_button.clicked.connect(self.seehw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View HomeWork"))
        self.label.setText(_translate("MainWindow", "View Home Work"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Subject"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Statement"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.divselect.setStatusTip(_translate("MainWindow", "Select division."))
        self.divselect.setItemText(0, _translate("MainWindow", "*Select Division*"))
        self.divselect.setItemText(1, _translate("MainWindow", "A"))
        self.divselect.setItemText(2, _translate("MainWindow", "B"))
        self.divselect.setItemText(3, _translate("MainWindow", "C"))
        self.divselect.setItemText(4, _translate("MainWindow", "D"))
        self.divselect.setItemText(5, _translate("MainWindow", "E"))
        self.divselect.setItemText(6, _translate("MainWindow", "F"))
        self.divselect.setItemText(7, _translate("MainWindow", "G"))
        self.divselect.setItemText(8, _translate("MainWindow", "H"))
        self.divselect.setItemText(9, _translate("MainWindow", "I"))
        self.divselect.setItemText(10, _translate("MainWindow", "J"))
        self.divselect.setItemText(11, _translate("MainWindow", "K"))
        self.divselect.setItemText(12, _translate("MainWindow", "L"))
        self.divselect.setItemText(13, _translate("MainWindow", "M"))
        self.divselect.setItemText(14, _translate("MainWindow", "N"))
        self.divselect.setItemText(15, _translate("MainWindow", "O"))
        self.divselect.setItemText(16, _translate("MainWindow", "P"))
        self.divselect.setItemText(17, _translate("MainWindow", "Q"))
        self.divselect.setItemText(18, _translate("MainWindow", "R"))
        self.divselect.setItemText(19, _translate("MainWindow", "S"))
        self.divselect.setItemText(20, _translate("MainWindow", "T"))
        self.viewhw_button.setStatusTip(_translate("MainWindow", "Press to get HW details"))
        self.viewhw_button.setText(_translate("MainWindow", "View HomeWork"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow8 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow8()
    ui.setupUi(MainWindow8)
    MainWindow8.show()
    sys.exit(app.exec_())
