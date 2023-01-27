from PyQt5.QtWidgets import*
from takim_python import Ui_Form
import mysql.connector
class TakimPage(QWidget):
    def __init__(self):
        super().__init__()
        self.takimform=Ui_Form() 
        self.takimform.setupUi(self)
        # self.islempenceresi=islemPage()
        self.takimform.pushButton_takimEkle.clicked.connect(self.takimEkle)
        self.takimform.pushButton_takimlistele.clicked.connect(self.takimListele)
        self.takimform.pushButton_takimsil.clicked.connect(self.takimSil)
        self.takimform.pushButton_takimduzenle.clicked.connect(self.takimDuzenle)
        self.takimform.pushButton_back.clicked.connect(self.back)
        
    def back(self):
        pass


    def takimDuzenle(self):
        istenilenKolon=self.takimform.comboBox_duzenleme.currentText()
        if istenilenKolon=="Takım Adı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE takimlar SET takim_adi=%s WHERE takim_id=%s"
            takim_adi=self.takimform.lineEdit_duzenleme.text()
            id=self.takimform.lineEdit_duzenlenenId.text()
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
            
                self.takimListele()
        
        if istenilenKolon=="Stadyum":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE takimlar SET stadyum=%s WHERE takim_id=%s"
            stadyum=self.takimform.lineEdit_duzenleme.text()
            id=self.takimform.lineEdit_duzenlenenId.text()
            values=(stadyum,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.takimListele()


        if istenilenKolon=="Kupa Sayısı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
        )
            mycursor=connection.cursor()
            sql="UPDATE takimlar SET kazandigi_kupa_sayisi=%s WHERE takim_id=%s"
            kupa_sayisi=int(self.takimform.lineEdit_duzenleme.text())
            id=self.takimform.lineEdit_duzenlenenId.text()
            values=(kupa_sayisi,id)
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.takimListele()


        if istenilenKolon=="Şehri":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            sehri=self.takimform.lineEdit_duzenleme.text()
            id=self.takimform.lineEdit_duzenlenenId.text()
            mycursor=connection.cursor()
            sql="UPDATE takimlar SET sehri=%s WHERE takim_id=%s"
            values=(sehri,id)
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.takimListele()

        

        if istenilenKolon=="Puan":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
        )
            mycursor=connection.cursor()
            sql="UPDATE takimlar SET mevcut_puani=%s WHERE takim_id=%s"
            puan=int(self.takimform.lineEdit_duzenleme.text())
            id=self.takimform.lineEdit_duzenlenenId.text()
            values=(puan,id)
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.takimListele()
            
    def takimSil(self):
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
            secilisatir=self.takimform.tableWidget.currentRow()
            id=self.takimform.tableWidget.item(secilisatir,0).text()
            sql="DELETE FROM takimlar where takim_id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.takimListele()
        
    def takimListele(self):
        self.takimform.tableWidget.clear()
        self.takimform.tableWidget.setHorizontalHeaderLabels(("Takım ID","Takım Adı","Stadyum","Kupa Sayısı","Şehri","Puan"))
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT * FROM takimlar"
        mycursor.execute(sql)
        try:
            results=mycursor.fetchall()
            self.takimform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.takimform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.takimform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(result[1])))
                self.takimform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(result[2])))
                self.takimform.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(result[3])))
                self.takimform.tableWidget.setItem(int(satir),4,QTableWidgetItem(str(result[4])))
                self.takimform.tableWidget.setItem(int(satir),5,QTableWidgetItem(str(result[5])))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)

        finally:
            connection.close()

    def takimEkle(self):
        takimAdi=self.takimform.lineEdit_takimadi.text()
        stadyum=self.takimform.lineEdit_stadyum.text()
        kupaSayisi=int(self.takimform.lineEdit_kupasayisi.text())
        sehri=self.takimform.lineEdit_sehri.text()
        puan=int(self.takimform.lineEdit_puan.text())

        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="INSERT INTO takimlar(takim_adi,stadyum,kazandigi_kupa_sayisi,sehri,mevcut_puani) VALUES(%s,%s,%s,%s,%s)"
        values=(takimAdi,stadyum,kupaSayisi,sehri,puan)

        mycursor.execute(sql,values)
        try:
            connection.commit()
            QMessageBox.warning(self,"Bilgi","Takım başarıyla Eklendi",QMessageBox.Close)
            takimAdi=self.takimform.lineEdit_takimadi.setText(str(""))
            stadyum=self.takimform.lineEdit_stadyum.setText(str(""))
            kupaSayisi=self.takimform.lineEdit_kupasayisi.setText(str(""))
            sehri=self.takimform.lineEdit_sehri.setText(str(""))
            puan=self.takimform.lineEdit_puan.setText(str(""))
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            self.takimListele()