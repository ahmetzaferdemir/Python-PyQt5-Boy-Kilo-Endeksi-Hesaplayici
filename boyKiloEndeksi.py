from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import *

uyg=QApplication([])

class boyKiloEndeks(QWidget):
    def __init__(self,parent=None):
        super(boyKiloEndeks,self).__init__(parent)

        self.resize(100,300)
        self.setWindowTitle("Boy Kilo Endeksi Hesaplayıcısı")
         
        baslik=QLabel("<center><font color='red' size='5'>BOY KİLO ENDEKSİ</center></font>")
        boyLabel=QLabel("Boy: ")
        self.boy=QLineEdit()
        self.boy.setInputMask("0.00")
        kiloLabel=QLabel("Kilo: ")
        self.kilo=QLineEdit()
        self.kilo.setInputMask("000")
        sonucLabel=QLabel("Sonuç:")
        self.sonuc=QLabel("")
        endeksLabel=QLabel("Endeks: ")
        self.endeks=QLabel("")
        self.hesaplaButton=QPushButton("HESAPLA")
        self.temizleButton=QPushButton("TEMİZLE")

        izgara=QGridLayout()
        self.setLayout(izgara)
        izgara.addWidget(baslik,0,0)
        izgara.addWidget(boyLabel,1,0)
        izgara.addWidget(self.boy,1,1)
        izgara.addWidget(kiloLabel,2,0)
        izgara.addWidget(self.kilo,2,1)
        izgara.addWidget(endeksLabel,3,0)
        izgara.addWidget(self.endeks,3,1)
        izgara.addWidget(sonucLabel,4,0)
        izgara.addWidget(self.sonuc,4,1)
        izgara.addWidget(self.hesaplaButton,5,0)
        izgara.addWidget(self.temizleButton,5,1)
        
        self.temizleButton.clicked.connect(self.temizle)
        self.hesaplaButton.clicked.connect(self.hesapla)

    def temizle(self):
        self.boy.setText("")
        self.kilo.setText("")
        self.endeks.setText("")
        self.sonuc.setText("")


    def hesapla(self):
        gecici=int(self.kilo.text())/(float(self.boy.text())**2)
        result=float(gecici)

        if gecici<18.5:
            self.endeks.setText(str(result))
            self.sonuc.setText("<center><font color='red' size='3'>Zayıfsınız</center></font>")
        
        elif gecici>18.5 and gecici<=25:
            self.endeks.setText(str(result))
            self.sonuc.setText("<center><font color='red' size='3'>Normalsiniz</center></font>")

        elif gecici>25 and gecici<=30:
            self.endeks.setText(str(result))
            self.sonuc.setText("<center><font color='red' size='3'>Kilolusunuz</center></font>")

        elif gecici>30:
            self.endeks.setText(str(result))
            self.sonuc.setText("<center><font color='red' size='3'>Yediklerine biraz dikkat etmelisin, obezsin</center></font>")

pencere=boyKiloEndeks()
pencere.show()
uyg.exec_()