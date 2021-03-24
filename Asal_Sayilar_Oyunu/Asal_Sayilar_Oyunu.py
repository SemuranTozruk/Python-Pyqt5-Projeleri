import sys
from PyQt5.QtWidgets import *
from random import randint, choice
from math import sqrt
from Asal_Sayilar_Oyunu_python import Ui_MainWindow

class AsalSayiOyun(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.skor = 0 # Skor başlangıç değeri
        self.sayac = 1 # sayaç başlangıç değeri
        self.primeNumberDensity = ["prime","nonPrime"]
        self.primeNumberFromZerotoAhundred = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        self.ui.label_oyunEkran.setText(str(self.generateRandomNumbers()))
        self.uiActions()
        self.show()

    def uiActions(self):
        self.ui.pushButton_dogru.clicked.connect(lambda: self.mainActionBoard("Right"))
        self.ui.pushButton_yanlis.clicked.connect(lambda: self.mainActionBoard("Wrong"))

    def mainActionBoard(self,buttonPushValue):
        theNumberOnTheGameLabel =  int(self.ui.label_oyunEkran.text())
        rightChosen = ((buttonPushValue == "Right") and (self.primeNumberTest(theNumberOnTheGameLabel)==True)) or ((buttonPushValue == "Wrong") and (self.primeNumberTest(theNumberOnTheGameLabel) == False))

        if rightChosen :
            self.skor += 10
            self.ui.label_skor.setText(f"{self.skor}")
            self.counter()
        else:
            self.counter()

    def generateRandomNumbers(self):
        self.densityChoiser = choice(self.primeNumberDensity)
        if self.densityChoiser == "prime" :
            self.primeNumberChosen = choice(self.primeNumberFromZerotoAhundred)
        else:
            self.primeNumberChosen = randint(0,100)

        return self.primeNumberChosen

    def primeNumberTest(self,onGameLabelNumber):

        n = onGameLabelNumber

        def asal(n):
            kok = round(sqrt(n)) + 1
            kontol = 0
            for deneme in range(2, kok):
                if n % deneme == 0:
                    kontol += 1
            return True if kontol == 0 else False

        return asal(n)

    def counter(self):
        if self.sayac < 10:
            self.sayac += 1
            self.ui.label_oyunEkran.setText(str(self.generateRandomNumbers()))

        elif self.sayac == 10:
            m_box=QMessageBox.question(self, "SKOR SONUCU",
                                    "Oyun bitti! Skorunuz: " f"{self.skor}/100"
                                    "\nTekrar Oynamak ister misiniz?", QMessageBox.Yes | QMessageBox.No )

            if m_box == QMessageBox.Yes:
                self.resetUi()
            else:
                window.close()


    def resetUi(self):
        self.ui.label_oyunEkran.setText(str(self.generateRandomNumbers()))
        self.ui.label_skor.setText("")
        self.skor = 0
        self.sayac = 1





app = QApplication(sys.argv)
window = AsalSayiOyun()
sys.exit(app.exec())
