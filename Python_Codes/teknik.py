from PyQt5.QtWidgets import*
from teknik_python import Ui_Form
import mysql.connector

class TeknikPage(QWidget):
    def __init__(self):
        super().__init__()
        self.teknikform=Ui_Form() 
        self.teknikform.setupUi(self)
        self.teknikform.pushButton.clicked.connect(self.teknikAdamEkle)
        self.teknikform.pushButton_2.clicked.connect(self.teknikAdamSil)
        self.teknikform.pushButton_3.clicked.connect(self.teknikAdamListele)
        self.teknikform.pushButton_4.clicked.connect(self.teknikAdamDuzenle)

    def teknikAdamDuzenle(self):
        istenilenKolon=self.teknikform.comboBox.currentText()
        if istenilenKolon=="Adı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE teknikdirektor SET teknikDirektör_adı=%s WHERE teknikDirektör_id=%s"
            takim_adi=self.teknikform.lineEdit_yenideger.text()
            id=self.teknikform.lineEdit_teknikid.text()
            values=(takim_adi,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
            
                self.teknikAdamListele()

        if istenilenKolon=="Kazandığı Kupa Sayısı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE teknikdirektor SET kazandığı_kupa_sayısı=%s WHERE teknikDirektör_id=%s"
            kupa=int(self.teknikform.lineEdit_yenideger.text())
            id=self.teknikform.lineEdit_teknikid.text()
            values=(kupa,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
            
                self.teknikAdamListele()

        if istenilenKolon=="Takım id":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE teknikdirektor SET takımlar_takım_id=%s WHERE teknikDirektör_id=%s"
            takimid=int(self.teknikform.lineEdit_yenideger.text())
            id=self.teknikform.lineEdit_teknikid.text()
            values=(takimid,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
            
                self.teknikAdamListele()

    def takimIsmi(self,id):
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="select takim_adi from takimlar where takim_id=%s"
        value=(id,)
        mycursor.execute(sql,value)
        try:
            result=mycursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print("err")
        finally:
            connection.close()

    def teknikAdamListele(self):
        self.teknikform.tableWidget.clear()
        self.teknikform.tableWidget.setHorizontalHeaderLabels(("Teknik Direktör ID","Teknik Direktör Adı","Kupa Sayısı","Takım ID"))
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT * FROM teknikdirektor"
        mycursor.execute(sql)
        try:
            results=mycursor.fetchall()
            self.teknikform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.teknikform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.teknikform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(result[1])))
                self.teknikform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(result[2])))
                self.teknikform.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(self.takimIsmi(int(result[3])))))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)

        finally:
            connection.close()

    def teknikAdamSil(self):
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
            secilisatir=self.teknikform.tableWidget.currentRow()
            id=self.teknikform.tableWidget.item(secilisatir,0).text()
            sql="DELETE FROM teknikdirektor where teknikDirektör_id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.teknikAdamListele()
        

    def teknikAdamEkle(self):
        adi=self.teknikform.lineEdit_adi.text()
        kupa=int(self.teknikform.lineEdit_kupasayisi.text())
        takim_id=int(self.teknikform.lineEdit_takimid.text())
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="INSERT INTO teknikdirektor(teknikDirektör_adı,kazandığı_kupa_sayısı,takımlar_takım_id) VALUES(%s,%s,%s)"
        values=(adi,kupa,takim_id)
        mycursor.execute(sql,values)
        try:
            connection.commit()
            QMessageBox.warning(self,"Bilgi","Teknik Adam başarıyla Eklendi",QMessageBox.Close)
            adi=self.teknikform.lineEdit_adi.setText(str(""))
            kupa=self.teknikform.lineEdit_kupasayisi.setText(str(""))
            takim_id=self.teknikform.lineEdit_takimid.setText(str(""))
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            self.teknikAdamListele()
            