# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet("QPushButton {\n"
"background-color: #42e6ec;\n"
"    width: 2px;\n"
"    radius: 10px;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font: bold, Arial;\n"
"}\n"
"QMainWindow {\n"
"background-color: #cdeaff;\n"
"font: bold, Arial, 15px;\n"
"}\n"
"QLineEdit {\n"
"    border-radius: 10px;\n"
"font: bord, Arial, 15px;\n"
"}\n"
"QLabel {font: bold, Arial, 15px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #42d4da;\n"
"    border-style: inset;\n"
"}\n"
"QMainWindow {\n"
"background-color: #cdeaff;\n"
"}\n"
"QTextBrowser {\n"
"font: bold, Arial, 12px;\n"
"background-color: #e0f5ff;\n"
"border-color: black;\n"
"border-radius: 10px;}\n"
"QStatusBar {\n"
"font: font: bold, Arial, 8px;\n"
"color: red;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(301, 21, 200, 28))
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(301, 55, 200, 28))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(301, 89, 200, 28))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(301, 123, 200, 28))
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(301, 157, 200, 28))
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(301, 191, 200, 28))
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 21, 75, 199))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 240, 271, 331))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(301, 476, 200, 28))
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(301, 374, 200, 28))
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(301, 442, 200, 28))
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(301, 408, 200, 28))
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(16777215, 28))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 306, 75, 199))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(301, 306, 200, 28))
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(301, 340, 200, 28))
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_18.setObjectName("lineEdit_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменение-редактирование"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Молотый/В зернах"))
        self.label_3.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки"))
        self.pushButton.setText(_translate("MainWindow", "Создать"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
