from PyQt5 import QtCore, QtGui, QtWidgets
from viewhwtab import Ui_MainWindow8

class Ui_MainWindow6(object):
    def hwevent(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow8()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 294)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.971591, y2:0.494, stop:0.0738636 rgba(85, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hw_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.hw_pushButton.setGeometry(QtCore.QRect(170, 80, 191, 31))
        self.hw_pushButton.setObjectName("hw_pushButton")
        self.hw_pushButton.clicked.connect(self.hwevent)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-130, 0, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tt_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.tt_pushButton.setGeometry(QtCore.QRect(170, 140, 191, 31))
        self.tt_pushButton.setObjectName("tt_pushButton")
        self.tt_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tt_pushButton_2.setGeometry(QtCore.QRect(170, 200, 191, 31))
        self.tt_pushButton_2.setObjectName("tt_pushButton_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Options"))
        self.hw_pushButton.setStatusTip(_translate("MainWindow", "View Homework"))
        self.hw_pushButton.setText(_translate("MainWindow", "View Homework"))
        self.label.setText(_translate("MainWindow", "Student Options"))
        self.tt_pushButton.setStatusTip(_translate("MainWindow", "View Time-Table"))
        self.tt_pushButton.setText(_translate("MainWindow", "View Time-Table"))
        self.tt_pushButton_2.setStatusTip(_translate("MainWindow", "Add Complain against Anything that bothers you."))
        self.tt_pushButton_2.setText(_translate("MainWindow", "Add Complaint "))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow6 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setupUi(MainWindow6)
    MainWindow6.show()
    sys.exit(app.exec_())
