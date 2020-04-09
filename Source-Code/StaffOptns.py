
from PyQt5 import QtCore, QtGui, QtWidgets
from hwentry import Ui_MainWindow7
import sqlite3


class Ui_MainWindow5(object):

    def hw_entry(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 269)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:0.971591, y2:0.494, stop:0.0738636 rgba(0, 117, 232, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 0, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 221, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 221, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.hw_entry)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 80, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 160, 221, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Staff Options"))
        self.label.setText(_translate("MainWindow", "Staff Options"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Add Student Grades"))
        self.pushButton.setText(_translate("MainWindow", "Add Grades"))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "Add Division-wise Homework"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Homework"))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "Update Student Attendance."))
        self.pushButton_3.setText(_translate("MainWindow", "Update Attendance"))
        self.pushButton_4.setStatusTip(_translate("MainWindow", "Personal Staff Details"))
        self.pushButton_4.setText(_translate("MainWindow", "Details"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow5 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow5)
    MainWindow5.show()
    sys.exit(app.exec_())
