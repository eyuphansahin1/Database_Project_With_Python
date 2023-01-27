from PyQt5.QtWidgets import*
from oyuncu_python import Ui_Form
import mysql.connector
class OyuncuPage(QWidget):
    def __init__(self):
        super().__init__()
        self.oyuncuform=Ui_Form() 
        self.oyuncuform.setupUi(self) 
        self.oyuncuform.pushButton_oyuncuekle.clicked.connect(self.oyuncuEkle)
        self.oyuncuform.pushButton_oyunculistele.clicked.connect(self.oyuncuListele)
        self.oyuncuform.pushButton_oyuncusil.clicked.connect(self.oyuncuSil)
        self.oyuncuform.pushButton_mevkiyegoresirala.clicked.connect(self.oyuncuMevki)
        self.oyuncuform.pushButton_oyuncuduzenle.clicked.connect(self.oyuncuDuzenle)

    def oyuncuDuzenle(self):
        istenilenKolon=self.oyuncuform.comboBox.currentText()
        if istenilenKolon=="Oyuncu Adı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET oyuncu_adi=%s WHERE oyuncu_id=%s"
            oyuncu_adi=self.oyuncuform.lineEdit_yenideger.text()
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(oyuncu_adi,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.oyuncuListele()

        if istenilenKolon=="Forma no":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET forma_no=%s WHERE oyuncu_id=%s"
            forma_no=int(self.oyuncuform.lineEdit_yenideger.text())
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(forma_no,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.oyuncuListele()



        if istenilenKolon=="gol sayısı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET oyuncu_gol_sayisi=%s WHERE oyuncu_id=%s"
            gol=int(self.oyuncuform.lineEdit_yenideger.text())
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(gol,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.oyuncuListele()


        if istenilenKolon=="asist sayısı":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET oyuncu_asist_sayisi=%s WHERE oyuncu_id=%s"
            asist=int(self.oyuncuform.lineEdit_yenideger.text())
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(asist,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.oyuncuListele()
        
        if istenilenKolon=="Takım id":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET takimlar_takim_id=%s WHERE oyuncu_id=%s"
            takim=int(self.oyuncuform.lineEdit_yenideger.text())
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(takim,int(id))
            mycursor.execute(sql,values)

            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
                self.oyuncuListele()
            
        istenilenKolon2=self.oyuncuform.comboBox_mevki_duzenle.currentText()
        if istenilenKolon!=None:
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE oyuncu SET oyuncu_mevki=%s WHERE oyuncu_id=%s"
            # takim=int(self.oyuncuform.lineEdit_yenideger.text())
            id=self.oyuncuform.lineEdit_duzenelencekid.text()
            values=(istenilenKolon2,int(id))
            mycursor.execute(sql,values)
           
            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.oyuncuform.comboBox_mevki_duzenle.clear()
                print('database baglantisi kapatildi')
                self.oyuncuListele()
                
    
    def oyuncuMevki(self):
        self.oyuncuform.tableWidget.clear()
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
        )
        mycursor=connection.cursor()
        listelenecek_kategori=self.oyuncuform.comboBox_mevkiyesirala.currentText()

        sql="SELECT * FROM oyuncu where oyuncu_mevki=%s"
        value=(listelenecek_kategori,)

        mycursor.execute(sql,value)
        try:
            results=mycursor.fetchall()
            self.oyuncuform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.oyuncuform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.oyuncuform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(result[1])))
                self.oyuncuform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(result[2])))
                self.oyuncuform.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(result[3])))
                self.oyuncuform.tableWidget.setItem(int(satir),4,QTableWidgetItem(str(result[4])))
                self.oyuncuform.tableWidget.setItem(int(satir),5,QTableWidgetItem(str(result[5])))
                self.oyuncuform.tableWidget.setItem(int(satir),6,QTableWidgetItem(str(result[6])))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)

        finally:
            connection.close()
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

    def oyuncuListele(self):
        self.oyuncuform.tableWidget.clear()
        self.oyuncuform.tableWidget.setHorizontalHeaderLabels(("oyuncu ID","Oyuncu Adı","Forma No","Oyuncu Mevki","Gol Sayısı","Asist Sayısı","Takım ismi"))
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT * FROM oyuncu"
        mycursor.execute(sql)
        try:
            results=mycursor.fetchall()
            self.oyuncuform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.oyuncuform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.oyuncuform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(result[1])))
                self.oyuncuform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(result[2])))
                self.oyuncuform.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(result[3])))
                self.oyuncuform.tableWidget.setItem(int(satir),4,QTableWidgetItem(str(result[4])))
                self.oyuncuform.tableWidget.setItem(int(satir),5,QTableWidgetItem(str(result[5])))
                self.oyuncuform.tableWidget.setItem(int(satir),6,QTableWidgetItem(str(self.takimIsmi(int(result[6])))))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)

        finally:
            connection.close()

    def oyuncuSil(self):
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
            secilisatir=self.oyuncuform.tableWidget.currentRow()
            id=self.oyuncuform.tableWidget.item(secilisatir,0).text()
            sql="DELETE FROM oyuncu where oyuncu_id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.oyuncuListele()

    def oyuncuEkle(self):
        oyuncuadi=self.oyuncuform.lineEdit_oyuncuadi.text()
        forma_no=int(self.oyuncuform.lineEdit_formano.text())
        mevki=self.oyuncuform.comboBox_mevki.currentText()
        gol=int(self.oyuncuform.lineEdit_golsayisi.text())
        asist=int(self.oyuncuform.lineEdit_asistsayisi.text())
        takimid=int(self.oyuncuform.lineEdit_takimid.text())
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
        )
        mycursor=connection.cursor()
        sql="INSERT INTO oyuncu(oyuncu_adi,forma_no,oyuncu_mevki,oyuncu_gol_sayisi,oyuncu_asist_sayisi,takimlar_takim_id) VALUES(%s,%s,%s,%s,%s,%s)"
        values=(oyuncuadi,forma_no,mevki,gol,asist,takimid)
        mycursor.execute(sql,values)
        try:
            connection.commit()
            QMessageBox.warning(self,"Bilgi","Oyuncu başarıyla Eklendi",QMessageBox.Close)
            oyuncuadi=self.oyuncuform.lineEdit_oyuncuadi.setText(str(""))
            gol=self.oyuncuform.lineEdit_golsayisi.setText(str(""))
            asist=self.oyuncuform.lineEdit_asistsayisi.setText(str(""))
            takimid=self.oyuncuform.lineEdit_takimid.setText(str(""))
            forma_no=self.oyuncuform.lineEdit_formano.setText(str(""))

        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            self.oyuncuListele()
            