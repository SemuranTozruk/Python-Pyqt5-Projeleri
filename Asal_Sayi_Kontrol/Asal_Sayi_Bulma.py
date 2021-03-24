import sys
from PyQt5.QtWidgets import *
from Asal_Sayi_Kontrol_py import Ui_MainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from math import sqrt

class AsalSayiKontrol(QMainWindow):# Qwidget class-ından inherance ediliyor.

    def __init__(self):
        super().__init__() # Qwidget (parent class) sınıfındaki niteliklere erişmek için constructor'ı çağırılıyor.
        self.timer = QTimer()
        self.ui = Ui_MainWindow()
        self.setWindowTitle("Asal Sayı mı, değil mi?")
        self.ui.setupUi(self)
        self.ComponentSetting()
        self.show()

    def ComponentSetting(self):
        self.ui.label_Baslik.setFont(QFont("Arial", 13))
        self.ui.label_sayiGir.setFont(QFont("Arial", 10))
        self.ui.pushButton.setFont(QFont("Arial", 8,QFont.Bold))
        self.ui.pushButton.resize(120,60)
        self.ui.lineEdit_sayiGir.setFont(QFont("Arial", 10,QFont.Bold))
        self.ui.pushButton.clicked.connect(self.AsalSorgu)
        self.ui.label_Sonuc.setText("")
        self.ui.label_Sonuc.setFont(QFont("Arial", 10,QFont.Bold))
        self.ui.label_Sonuc.resize(200, 50)

    def AsalSorgu(self,args):
        n = int(self.ui.lineEdit_sayiGir.text())

        def asal(n):
            kok = round(sqrt(n)) + 1
            kontol = 0
            for deneme in range(2, kok):
                if n % deneme == 0:
                    kontol += 1
            return True if kontol == 0 else False

        if asal(n):
            self.ui.label_Sonuc.setText("SAYI ASALDIR!")
            self.timer.singleShot(2000,self.LabelDestroy)
        else:
            self.ui.label_Sonuc.setText("SAYI ASAL DEĞİLDİR!")
            self.timer.singleShot(2000, self.LabelDestroy)

    def LabelDestroy(self):
        self.ui.label_Sonuc.setText("")



app = QApplication(sys.argv)
window = AsalSayiKontrol()
sys.exit(app.exec())