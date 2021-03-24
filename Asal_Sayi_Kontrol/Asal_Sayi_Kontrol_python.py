# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/hllsy/OneDrive/Masaüstü/Asal Sayı Kontrol/Asal_Sayi_Kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Baslik = QtWidgets.QLabel(self.centralwidget)
        self.label_Baslik.setGeometry(QtCore.QRect(90, 40, 201, 51))
        self.label_Baslik.setTextFormat(QtCore.Qt.AutoText)
        self.label_Baslik.setScaledContents(True)
        self.label_Baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Baslik.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_Baslik.setObjectName("label_Baslik")
        self.label_sayiGir = QtWidgets.QLabel(self.centralwidget)
        self.label_sayiGir.setGeometry(QtCore.QRect(70, 140, 111, 31))
        self.label_sayiGir.setObjectName("label_sayiGir")
        self.lineEdit_sayiGir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sayiGir.setGeometry(QtCore.QRect(190, 140, 131, 31))
        self.lineEdit_sayiGir.setObjectName("lineEdit_sayiGir")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_Sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_Sonuc.setGeometry(QtCore.QRect(100, 310, 191, 61))
        self.label_Sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Sonuc.setObjectName("label_Sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Baslik.setText(_translate("MainWindow", "ASAL SAYI BULMA"))
        self.label_sayiGir.setText(_translate("MainWindow", "Sayınızı giriniz:"))
        self.pushButton.setText(_translate("MainWindow", "ASAL SAYI MI ?"))
        self.label_Sonuc.setText(_translate("MainWindow", "Sayınız Asal Sayı Değildir"))

