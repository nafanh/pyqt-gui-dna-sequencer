# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'run_desc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi2(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(842, 661)
        MainWindow2.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.BeforeRunLabel = QtWidgets.QLabel(self.centralwidget)
        self.BeforeRunLabel.setGeometry(QtCore.QRect(80, 160, 81, 16))
        self.BeforeRunLabel.setObjectName("BeforeRunLabel")
        self.RunDescLabel = QtWidgets.QLabel(self.centralwidget)
        self.RunDescLabel.setGeometry(QtCore.QRect(150, 160, 441, 16))
        self.RunDescLabel.setText("")
        self.RunDescLabel.setObjectName("RunDescLabel")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 520, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 260, 171, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 320, 111, 31))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 320, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 320, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 380, 151, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(260, 380, 211, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 260, 111, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 520, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 80, 691, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NameTxtLabel = QtWidgets.QLabel(self.widget)
        self.NameTxtLabel.setObjectName("NameTxtLabel")
        self.horizontalLayout.addWidget(self.NameTxtLabel)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(80, 210, 373, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TimeULabel = QtWidgets.QLabel(self.widget1)
        self.TimeULabel.setObjectName("TimeULabel")
        self.horizontalLayout_2.addWidget(self.TimeULabel)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Run Description"))
        self.BeforeRunLabel.setText(_translate("MainWindow2", "Run Desc."))
        self.pushButton_3.setText(_translate("MainWindow2", "Back"))
        self.pushButton_4.setText(_translate("MainWindow2", "Show all internal std. peaks"))
        self.label.setText(_translate("MainWindow2", "Min. Hieght Filter"))
        self.pushButton_5.setText(_translate("MainWindow2", "Submit"))
        self.pushButton_6.setText(_translate("MainWindow2", "Show all filtered peaks"))
        self.pushButton_7.setText(_translate("MainWindow2", "Show filtered internal std. peaks"))
        self.pushButton_8.setText(_translate("MainWindow2", "Show All Peaks"))
        self.pushButton_9.setText(_translate("MainWindow2", "Continue"))
        self.NameTxtLabel.setText(_translate("MainWindow2", "Path of .txt"))
        self.pushButton.setText(_translate("MainWindow2", "Browse"))
        self.TimeULabel.setText(_translate("MainWindow2", "Enter time underscore"))
        self.pushButton_2.setText(_translate("MainWindow2", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi2(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
