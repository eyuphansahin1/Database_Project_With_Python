from PyQt5.QtWidgets import*
from giris2 import Ui_Form
from takim import TakimPage
from oyuncu import OyuncuPage
from teknik import TeknikPage
from sponsor import SponsorPage
from mac import MacPage
class islemPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform=Ui_Form() 
        self.loginform.setupUi(self)
        self.loginform.pushButton.clicked.connect(self.takimIslemleriAc)
        self.loginform.pushButton_2.clicked.connect(self.oyuncuIsimleriAc)
        self.loginform.pushButton_3.clicked.connect(self.teknikIslemlerAc)
        self.loginform.pushButton_4.clicked.connect(self.sponsorIslemlerAc)
        self.loginform.pushButton_5.clicked.connect(self.macIslemlerAc)
        self.macpenceresi=MacPage()
        self.takimpenceresi=TakimPage()
        self.oyuncupenceresi=OyuncuPage()
        self.teknikpencere=TeknikPage()
        self.sponsorPencere=SponsorPage()
    def macIslemlerAc(self):
        self.macpenceresi.show()
    def takimIslemleriAc(self):
        self.takimpenceresi.show()
    def oyuncuIsimleriAc(self):
        self.oyuncupenceresi.show()
    def teknikIslemlerAc(self):
        self.teknikpencere.show()
    def sponsorIslemlerAc(self):
        self.sponsorPencere.show()
