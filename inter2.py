# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from coder_faces import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1073, 806)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 100, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 80, 250, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(760, 100, 211, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 181, 41))
        self.label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 20, 181, 41))
        self.label_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 40, 331, 41))
        self.label_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 510, 201, 51))
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 490, 221, 51))
        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(390, 480, 311, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 281, 311))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 120, 291, 341))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(740, 130, 311, 341))
        self.label_6.setObjectName("label_6")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        ##add items to combobox
        self.comboBox.addItems(get_pics())
        self.comboBox_2.addItems(get_barcodes())
        self.comboBox_3.addItems(get_encrypted_pics())

        pixmap = QtGui.QPixmap(self.comboBox.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(pixmap2)

        pixmap = QtGui.QPixmap(self.comboBox_2.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(pixmap2)

        pixmap = QtGui.QPixmap(self.comboBox_3.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_6.setPixmap(pixmap2)

        ##Вывод изображение из выпадающего окна
        self.comboBox_2.currentIndexChanged.connect(self.on_combobox_changed_2)

        self.comboBox_3.currentIndexChanged.connect(self.on_combobox_changed_3)
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)

        self.pushButton.clicked.connect(self.showPicts)
    def on_combobox_changed(self):
        pixmap = QtGui.QPixmap(self.comboBox.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(pixmap2)

    def on_combobox_changed_2(self):
        pixmap = QtGui.QPixmap(self.comboBox_2.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(pixmap2)

    def on_combobox_changed_3(self):
        pixmap = QtGui.QPixmap(self.comboBox_3.currentText())
        pixmap2 = pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
        self.label_6.setPixmap(pixmap2)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Формироывние скрытого зашифрованного изображения"))
        self.label.setText(_translate("mainWindow", "Выбрать изображение"))
        self.label_2.setText(_translate("mainWindow", "Выбрать штрих-код"))
        self.label_3.setText(_translate("mainWindow", "Выбрать скрытое зашифрованное изображение"))
        self.pushButton.setText(_translate("mainWindow", "Сформировать штрих-код"))
        self.pushButton_3.setText(_translate("mainWindow", "Расшифровать изображение "))
        self.label_4.setText(_translate("mainWindow", "TextLabel"))
        self.label_5.setText(_translate("mainWindow", "TextLabel"))
        self.label_6.setText(_translate("mainWindow", "TextLabel"))

        ##Показать темлейт метод

    def showPicts(self):
        self.comboBox_2.addItem(BarCodeimage(self.comboBox.currentText()))




