from PyQt5.QtWidgets import*
from login_python2 import Ui_Form
import mysql.connector
from islemler import islemPage
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform=Ui_Form() 
        self.loginform.setupUi(self) 
        self.islempenceresi=islemPage()
        self.loginform.pushButton_login.clicked.connect(self.loginFunc)

    def loginFunc(self):
        username=self.loginform.lineEdit_username.text()
        password=self.loginform.lineEdit_password.text()
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT *FROM users WHERE username=%s and password=%s"
        values=(username,password)
        mycursor.execute(sql,values)
        try:
            result=mycursor.fetchone()
            if result==None:
                QMessageBox.warning(self,"hata","Kullanıcı adı ya da şifre yanlış",QMessageBox.Close)
                username=self.loginform.lineEdit_username.setText(str(""))
                username=self.loginform.lineEdit_password.setText(str(""))
            else:
                self.hide()
                self.islempenceresi.show()
        except mysql.connector.Error as err:
            print('hata: ',err)

        finally:
            connection.close()
        