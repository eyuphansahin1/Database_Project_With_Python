from PyQt5.QtWidgets import*
from mac_python import Ui_Form
import mysql.connector

class MacPage(QWidget):
    def __init__(self):
        super().__init__()
        self.macform=Ui_Form() 
        self.macform.setupUi(self) 
        self.macform.pushButton_macEkle.clicked.connect(self.macEkle)
        self.macform.pushButton_macListele.clicked.connect(self.macListele)
        self.macform.pushButton_macSil.clicked.connect(self.macSil)
        self.macform.pushButton_macDuzenle.clicked.connect(self.macDuzenle)
    
    def macDuzenle(self):
        takim1=self.macform.lineEdit_takim1.text()
        takim2=self.macform.lineEdit_takim2.text()
        id=int(self.macform.lineEdit_duzenelencekmacid.text())

        if takim1==""and takim2=="":
            pass
        elif takim1=="":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE mactablosu SET takımlar_takım_id2=%s WHERE mac_id=%s"
            values=(takim2,int(id))
            mycursor.execute(sql,values)
            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
        elif takim2=="":
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE mactablosu SET takımlar_takım_id1=%s WHERE mac_id=%s"
            values=(takim1,int(id))
            mycursor.execute(sql,values)
            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')

        else:
            connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="M9100Eyup1",
            database="superlig"
            )
            mycursor=connection.cursor()
            sql="UPDATE mactablosu SET takımlar_takım_id1=%s,takımlar_takım_id2=%s WHERE mac_id=%s"
            values=(takim1,takim2,int(id))
            mycursor.execute(sql,values)
            try:
                connection.commit()
                print('1 tane kayit etkilendi')
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                print('database baglantisi kapatildi')
        self.macListele()

    def macEkle(self):
        takim1=int(self.macform.lineEdit_takim1.text())
        takim2=int(self.macform.lineEdit_takim2.text())
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="INSERT INTO mactablosu(takımlar_takım_id1,takımlar_takım_id2) VALUES(%s,%s)"
        values=(takim1,takim2)
        mycursor.execute(sql,values)
        try:
            connection.commit()
            QMessageBox.warning(self,"Bilgi","Maç Adam başarıyla Eklendi",QMessageBox.Close)
            takim1=self.macform.lineEdit_takim1.setText(str(""))
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close()
            self.macListele()
    
    def macListele(self):
        self.macform.tableWidget.clear()
        self.macform.tableWidget.setHorizontalHeaderLabels(("maç id","1.takım ismi","2.takım ismi"))
        connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="M9100Eyup1",
        database="superlig"
        )
        mycursor=connection.cursor()
        sql="SELECT * FROM mactablosu"
        mycursor.execute(sql)
        try:
            results=mycursor.fetchall()
            self.macform.tableWidget.setRowCount(len(results))
            satir=0
            for result in results:
                self.macform.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(result[0])))
                self.macform.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(self.takimIsmi(int(result[1])))))
                self.macform.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(self.takimIsmi(int(result[2])))))
                satir+=1
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            connection.close()

    def macSil(self):
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
            secilisatir=self.macform.tableWidget.currentRow()
            id=self.macform.tableWidget.item(secilisatir,0).text()
            sql="DELETE FROM mactablosu where mac_id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            try:
                connection.commit()
            except mysql.connector.Error as err:
                print('hata: ',err)
            finally:
                connection.close()
                self.macListele()

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
