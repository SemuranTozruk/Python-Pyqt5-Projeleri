import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *


class Window(QWidget):# Qwidget class-ından inherance ediliyor.

    def __init__(self):
        super().__init__() # Qwidget (parent class) sınıfındaki niteliklere erişmek için constructor'ı çağırılıyor.

        self.setGeometry(1250, 50, 600, 600)  # ilk iki parametre ekranın neresinde görüneceğini - son iki pramaetre piksel cinsinden genişlik ve yükseklik
        self.setWindowTitle("Kesir Genişletme-Sadeleştirme")  # Pencerede görünecek başlık
        self.UIComponents()
        self.show()  # Oluşturulan Pencerenin Gösterilmesini sağlar.

    def UIComponents(self):

        # label: Uygulama başlık
        self.uyg_sunum = QLabel("GENİŞLET - SADELEŞTİR",self)
        self.uyg_sunum.setFont(QFont("Arial",15,QFont.Bold))
        self.uyg_sunum.move(170,50)

        # RadioButton: Genişlet
        self.genislet = QRadioButton("Genişlet",self)
        self.genislet.setFont(QFont("Arial",15))
        self.genislet.move(120,120)

        # RadioButton: Sadeleştir
        self.sadelestir = QRadioButton("Sadeleştir", self)
        self.sadelestir.setFont(QFont("Arial", 15))
        self.sadelestir.move(400, 120)

        # QlineEdit: pay
        self.pay = QLineEdit(self)
        self.pay.setPlaceholderText("Pay")
        self.pay.setAlignment(QtCore.Qt.AlignCenter)
        self.pay.setFont(QFont("Arial", 15))
        self.pay.resize(80,50)
        self.pay.move(200,200)

        #Label:Kesir çizgisi
        self.kesirCizgisi = QLabel(self)
        self.kesirCizgisi.setPixmap(QPixmap("kesir_cizgisi.png"))
        self.kesirCizgisi.resize(100,7)
        self.kesirCizgisi.move(190,260)


        #QlineEdit: payda
        self.payda = QLineEdit(self)
        self.payda.setPlaceholderText("Payda")
        self.payda.setAlignment(QtCore.Qt.AlignCenter)
        self.payda.setFont(QFont("Arial", 15))
        self.payda.resize(80, 50)
        self.payda.move(200, 280)

        # Label:Eşittir
        self.esittir = QLabel("=",self)
        self.esittir.setFont(QFont("Arial", 25))
        self.esittir.move(310, 240)

        # Label: Pay çıktı
        self.pay_cikti = QLabel(" ", self)
        self.pay_cikti.setAlignment(QtCore.Qt.AlignCenter)
        self.pay_cikti.resize(100,40)
        self.pay_cikti.setFont(QFont("Arial", 20))
        self.pay_cikti.move(350, 210)

        # Label: Payda çıktı
        self.payda_cikti = QLabel(" ", self)
        self.payda_cikti.setAlignment(QtCore.Qt.AlignCenter)
        self.payda_cikti.resize(100, 40)
        self.payda_cikti.setFont(QFont("Arial", 20))
        self.payda_cikti.move(350, 280)

        #Label: sonuç çıktısının kesir çizgisi
        self.kesirCizgisi = QLabel(self)
        self.kesirCizgisi.setPixmap(QPixmap("kesir_cizgisi.png"))
        self.kesirCizgisi.resize(100, 7)
        self.kesirCizgisi.move(350, 260)

        # Label: Hangi sayıyı ile işlem yapılsın.
        self.islemSayisi = QLabel("Hangi sayı ile işlem yapılsın:", self)
        self.islemSayisi.setFont(QFont("Arial", 15))
        self.islemSayisi.move(100, 400)

        # Entry: Sadeleşme/Genişleme Sayısı girdisi
        self.islemGirdisi = QLineEdit(self)
        self.islemGirdisi.setAlignment(QtCore.Qt.AlignCenter)
        self.islemGirdisi.setFont(QFont("Arial", 15))
        self.islemGirdisi.resize(80, 50)
        self.islemGirdisi.move(430, 390)

        # Buton: İşlem Butonu
        self.button = QPushButton("GİRİŞ",self)
        self.button.setFont(QFont("Arial", 15))
        self.button.resize(100, 50)
        self.button.move(250,470)
        self.button.clicked.connect(self.DegerBul)

    def DegerBul(self):
        self.pay_deger = int(self.pay.text())
        self.payda_deger = int(self.payda.text())
        self. islem_sayi = int(self.islemGirdisi.text())

        self.pay_genislesmis = self.pay_deger * self.islem_sayi
        self.payda_genislesmis = self.payda_deger * self.islem_sayi

        if self.genislet.isChecked():
            self.pay_cikti.setText(f"{self.pay_genislesmis}")
            self.payda_cikti.setText(f"{self.payda_genislesmis}")

        elif self.sadelestir.isChecked():
            if (self.pay_deger % self.islem_sayi == 0) and (self.payda_deger % self.islem_sayi == 0):
                self.pay_sadelesmis = int(self.pay_deger / self.islem_sayi)
                self.payda_sadelesmis = int(self.payda_deger / self.islem_sayi)

                self.pay_cikti.setText(f"{self.pay_sadelesmis}")
                self.payda_cikti.setText(f"{self.payda_sadelesmis}")

            elif (self.pay_deger % self.islem_sayi != 0) or (self.payda_deger % self.islem_sayi != 0):
                QMessageBox.critical(self, "HATA", "Pay veya Payda Girdiğiniz Sayı ile Bölünmemektedir!")



app = QApplication(sys.argv) #Dikkat!!! bu satır -window = Window()- satırından önce gelecek!!
window = Window()
sys.exit(app.exec())