# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'takim_python.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1210, 560)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 100, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 230, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 270, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_takimadi = QtWidgets.QLineEdit(Form)
        self.lineEdit_takimadi.setGeometry(QtCore.QRect(180, 110, 113, 22))
        self.lineEdit_takimadi.setObjectName("lineEdit_takimadi")
        self.lineEdit_stadyum = QtWidgets.QLineEdit(Form)
        self.lineEdit_stadyum.setGeometry(QtCore.QRect(180, 150, 113, 22))
        self.lineEdit_stadyum.setObjectName("lineEdit_stadyum")
        self.lineEdit_kupasayisi = QtWidgets.QLineEdit(Form)
        self.lineEdit_kupasayisi.setGeometry(QtCore.QRect(180, 190, 113, 22))
        self.lineEdit_kupasayisi.setObjectName("lineEdit_kupasayisi")
        self.lineEdit_sehri = QtWidgets.QLineEdit(Form)
        self.lineEdit_sehri.setGeometry(QtCore.QRect(180, 230, 113, 22))
        self.lineEdit_sehri.setObjectName("lineEdit_sehri")
        self.lineEdit_puan = QtWidgets.QLineEdit(Form)
        self.lineEdit_puan.setGeometry(QtCore.QRect(180, 270, 113, 22))
        self.lineEdit_puan.setObjectName("lineEdit_puan")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(350, 60, 781, 281))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.pushButton_takimEkle = QtWidgets.QPushButton(Form)
        self.pushButton_takimEkle.setGeometry(QtCore.QRect(380, 370, 151, 31))
        self.pushButton_takimEkle.setObjectName("pushButton_takimEkle")
        self.pushButton_takimsil = QtWidgets.QPushButton(Form)
        self.pushButton_takimsil.setGeometry(QtCore.QRect(590, 370, 151, 31))
        self.pushButton_takimsil.setObjectName("pushButton_takimsil")
        self.pushButton_takimduzenle = QtWidgets.QPushButton(Form)
        self.pushButton_takimduzenle.setGeometry(QtCore.QRect(970, 370, 151, 31))
        self.pushButton_takimduzenle.setObjectName("pushButton_takimduzenle")
        self.pushButton_takimlistele = QtWidgets.QPushButton(Form)
        self.pushButton_takimlistele.setGeometry(QtCore.QRect(780, 370, 151, 31))
        self.pushButton_takimlistele.setObjectName("pushButton_takimlistele")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 430, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 430, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_duzenlenenId = QtWidgets.QLineEdit(Form)
        self.lineEdit_duzenlenenId.setGeometry(QtCore.QRect(200, 460, 141, 22))
        self.lineEdit_duzenlenenId.setObjectName("lineEdit_duzenlenenId")
        self.comboBox_duzenleme = QtWidgets.QComboBox(Form)
        self.comboBox_duzenleme.setGeometry(QtCore.QRect(390, 460, 111, 22))
        self.comboBox_duzenleme.setObjectName("comboBox_duzenleme")
        self.comboBox_duzenleme.addItem("")
        self.comboBox_duzenleme.addItem("")
        self.comboBox_duzenleme.addItem("")
        self.comboBox_duzenleme.addItem("")
        self.comboBox_duzenleme.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(370, 430, 161, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_duzenleme = QtWidgets.QLineEdit(Form)
        self.lineEdit_duzenleme.setGeometry(QtCore.QRect(570, 460, 113, 22))
        self.lineEdit_duzenleme.setObjectName("lineEdit_duzenleme")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(590, 430, 71, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_back = QtWidgets.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 30, 151, 51))
        self.pushButton_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/back/back.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon)
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Form)
        self.comboBox_duzenleme.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Takım Adı"))
        self.label_2.setText(_translate("Form", "Stadyum"))
        self.label_3.setText(_translate("Form", " Kupa Sayısı"))
        self.label_4.setText(_translate("Form", "Şehri"))
        self.label_5.setText(_translate("Form", "Puan"))
        self.pushButton_takimEkle.setText(_translate("Form", "Takım Ekle"))
        self.pushButton_takimsil.setText(_translate("Form", "Takım Sil"))
        self.pushButton_takimduzenle.setText(_translate("Form", "Takım Düzenle"))
        self.pushButton_takimlistele.setText(_translate("Form", "Takım Listele"))
        self.label_6.setText(_translate("Form", "Düzenelenecek ID değeri"))
        self.label_7.setText(_translate("Form", "Düzenleme"))
        self.comboBox_duzenleme.setItemText(0, _translate("Form", "Takım Adı"))
        self.comboBox_duzenleme.setItemText(1, _translate("Form", "Stadyum"))
        self.comboBox_duzenleme.setItemText(2, _translate("Form", "Kupa Sayısı"))
        self.comboBox_duzenleme.setItemText(3, _translate("Form", "Şehri"))
        self.comboBox_duzenleme.setItemText(4, _translate("Form", "Puan"))
        self.label_8.setText(_translate("Form", "Düzenelenecek kolon ismi"))
        self.label_9.setText(_translate("Form", "Yeni Değer"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
