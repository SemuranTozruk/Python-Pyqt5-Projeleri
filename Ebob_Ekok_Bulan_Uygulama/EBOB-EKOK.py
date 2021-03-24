import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(1300, 50, 500, 640)
        self.setWindowTitle("EBOB-EKOK BULMA PROGRAM")
        self.UIComponents()
        self.show()

    def UIComponents(self):

        # label: Uygulama başlık
        self.uyg_sunum = QLabel("EBOB - EKOK",self)
        self.uyg_sunum.setFont(QFont("Arial",15,QFont.Bold))
        self.uyg_sunum.move(170,50)

        # Label: "İşlem yapılacak sayılar neler?"
        self.girdiSayilarLabel = QLabel("İşlem yapılacak sayılar neler?", self)
        self.girdiSayilarLabel.setFont(QFont("Arial", 15))
        self.girdiSayilarLabel.move(100, 150)

        # Entry: ilk değer
        self.ilkDeger = QLineEdit(self)
        self.ilkDeger.setAlignment(QtCore.Qt.AlignCenter)
        self.ilkDeger.setFont(QFont("Arial", 15))
        self.ilkDeger.resize(80, 50)
        self.ilkDeger.move(130, 230)

        #Label: tire

        self.tire = QLabel(" — ", self)
        self.tire.setFont(QFont("Arial", 20, QFont.Bold))
        self.tire.move(230, 230)

        # Entry: ikinci değer
        self.ikinciDeger = QLineEdit(self)
        self.ikinciDeger.setAlignment(QtCore.Qt.AlignCenter)
        self.ikinciDeger.setFont(QFont("Arial", 15))
        self.ikinciDeger.resize(80, 50)
        self.ikinciDeger.move(300, 230)

        # Buton: EBOB Butonu
        self.button_Ebob = QPushButton("EBOB", self)
        self.button_Ebob.setFont(QFont("Arial", 15))
        self.button_Ebob.resize(100, 50)
        self.button_Ebob.move(120, 350)
        self.button_Ebob.clicked.connect(lambda: self.DegerBul("Ebob"))

        # Buton: EKOK Butonu
        self.button_Ekok = QPushButton("EKOK", self)
        self.button_Ekok.setFont(QFont("Arial", 15))
        self.button_Ekok.resize(100, 50)
        self.button_Ekok.move(300, 350)
        self.button_Ekok.clicked.connect(lambda: self.DegerBul("Ekok"))

        # Label: "Girdiğiniz Sayının EBOB'u / EKOK'u "
        self.girdiSayilarLabel = QLabel(self)
        self.girdiSayilarLabel.resize(320,50)
        self.girdiSayilarLabel.setFont(QFont("Arial", 15))
        self.girdiSayilarLabel.move(100, 450)

        # Label: Sonuç çıktısı
        self.sonuc_Cikti = QLabel(self)
        self.sonuc_Cikti.setAlignment(QtCore.Qt.AlignCenter)
        self.sonuc_Cikti.resize(100, 50)
        self.sonuc_Cikti.setFont(QFont("Arial", 15,QFont.Bold))
        self.sonuc_Cikti.move(200, 530)


    def DegerBul(self,secim):
        try:
            self.ilk_sayi = int(self.ilkDeger.text())
            self.ikinci_sayi = int(self.ikinciDeger.text())

            if secim == "Ebob":
                self.girdiSayilarLabel.setText("Girdiğiniz Sayıların EBOB'u")
                self.sonuc_Cikti.setText(f"{self.EbobBul()}")
            elif secim == "Ekok":
                self.girdiSayilarLabel.setText("Girdiğiniz Sayıların EKOK'u")
                self.sonuc_Cikti.setText(f"{self.EkokBul()}")
        except:
            QMessageBox.critical(self, "HATA", "Lütfen yukarıdaki kutulara pozitif tamsayılar\n girdiğinize emin olunuz!")



    def EbobBul(self):
        global sayi_1, sayi_2
        sayi_1= self.ilk_sayi
        sayi_2= self.ikinci_sayi

        def ilkSayiBolenler():
            global sayi1_bolenler
            sayi1_bolenler =[]
            for i in range(1,sayi_1 + 1):
                if sayi_1 % i == 0:
                    sayi1_bolenler.append(i)
                else:
                    pass
            return sayi1_bolenler

        def ikinciSayiBolenler():
            sayi2_bolenler =[]
            for i in range(1,sayi_2 + 1):
                if sayi_2 % i == 0:
                    sayi2_bolenler.append(i)
                else:
                    pass
            return sayi2_bolenler

        def ortakBolenler():
            ortakBolenListe = []
            for i in ilkSayiBolenler():
                for j in ikinciSayiBolenler():
                    if i==j:
                        ortakBolenListe.append(i)
                        break
                    else:
                        continue
            return ortakBolenListe
        return max(ortakBolenler())


    def EkokBul(self):
        global sayi_1, sayi_2
        sayi_1 = self.ilk_sayi
        sayi_2 = self.ikinci_sayi
        ortakKatlar = []
        for i in [sayi_1 * x for x in range(1,sayi_2 + 1)]:
            for j in [sayi_2 * y for y in range(1,sayi_1 + 1)]:
                if i==j:
                    ortakKatlar.append(i)
                    break
                else:
                    continue

        return min(ortakKatlar)




app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())