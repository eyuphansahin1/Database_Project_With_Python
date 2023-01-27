from PyQt5.QtWidgets import*
from sponsor_python import Ui_Form
import mysql.connector

class SponsorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.sponsorform=Ui_Form() 
        self.sponsorform.setupUi(self)
        self.sponsorform.pushButton.clicked.connect(self.sponsorEkle)
        self.sponsorform.pushButton_2.clicked.connect(self.sponsorSil)
        self.sponsorform.pushButton_3.clicked.connect(self.sponsorDuzenle)
        self.sponsorform.pushButton_4.clicked.connect(self.sponsorListele)

    def sponsorDuzenle(self):
        istenilenKolon=self.sponsorform.comboBox.currentText()
        if istenilenKolon=="Sponsor Adı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE sponsor SET sponsor_adi=%s WHERE sponsor_id=%s"
            sponsor_adi=self.sponsorform.lineEdit_4.text()
            id=self.sponsorform.lineEdit_3.text()
            values=(sponsor_adi,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                
        if istenilenKolon=="Bağış Miktarı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE sponsor SET bagis_miktari=%s WHERE sponsor_id=%s"
            bagis_miktari=int(self.sponsorform.lineEdit_4.text())
            id=self.sponsorform.lineEdit_3.text()
            values=(bagis_miktari,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                
        self.sponsorListele()

    def sponsorSil(self):
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sure=QMessageBox.critical(self,"Silme","Silmek istediğinizden emin misiniz ?",QMessageBox.Yes,QMessageBox.No)
        if sure==QMessageBox.Yes:
            mycursor=connection.cursor()
            secilisatir=self.sponsorform.tableWidget.currentRow()
            id=self.sponsorform.tableWidget.item(secilisatir,0).text()
            sql="DELETE FROM sponsor where sponsor_id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.sponsorListele()

    def sponsorEkle(self):
        sponsor_adi=self.sponsorform.lineEdit.text()
        miktar=int(self.sponsorform.lineEdit_2.text())
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
        )
        mycursor=connection.cursor()
        sql="INSERT INTO sponsor(sponsor_adi,bagis_miktari) VALUES(%s,%s)"
        values=(sponsor_adi,miktar)
        mycursor.execute(sql,values)
        try:
            connection.commit()
            QMessageBox.warning(self,"Bilgi","Sponsor başarıyla Eklendi",QMessageBox.Close)
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            self.sponsorListele()
            
    def sponsorListele(self):
        self.sponsorform.tableWidget.clear()
        self.sponsorform.tableWidget.setHorizontalHeaderLabels(("sponsor id","sponsor adı","Bağış Miktarı"))
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT * FROM sponsor"
        mycursor.execute(sql)
        try:
            results=mycursor.fetchall()
            self.sponsorform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.sponsorform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.sponsorform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(result[1])))
                self.sponsorform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(result[2])))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            connection.close()