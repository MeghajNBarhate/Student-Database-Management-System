from PyQt5 import QtCore, QtGui, QtWidgets
from adminoptions import Ui_MainWindow4

class Ui_MainWindow1(object):

    def auth(self):
        i_d = self.lineEdit.text()
        pswd = self.lineEdit_2.text()
        if(pswd == "password" and i_d == "Administrator"):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow4()
                self.ui.setupUi(self.window)
                self.window.show()
        else:
                pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow1")
        MainWindow.resize(404, 207)
        MainWindow.setStyleSheet(" background-color:qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.971591, y2:0.494, stop:0.375 rgba(170, 170, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 60, 121, 20))
        self.lineEdit_2.setStyleSheet(" background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(64, 100, 281, 31))
        self.loginbutton.setStyleSheet("background-color: rgb(200, 198, 200);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.loginbutton.setCheckable(False)
        self.loginbutton.setChecked(False)
        self.loginbutton.setAutoDefault(False)
        self.loginbutton.setDefault(False)
        self.loginbutton.setFlat(False)
        self.loginbutton.setObjectName("loginbutton")
        self.loginbutton.clicked.connect(self.auth)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(60, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(60, 60, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 121, 20))
        self.lineEdit.setStyleSheet(" background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Login"))
        self.loginbutton.setText(_translate("MainWindow", "LOGIN"))
        self.l1.setText(_translate("MainWindow", "Username:"))
        self.l2.setText(_translate("MainWindow", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
