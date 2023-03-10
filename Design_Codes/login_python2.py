# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login__python2.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 580)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 581))
        self.label.setStyleSheet("border-image: url(:/saha/sahaa.ico);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 421, 351))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/kapı/istockphoto-534456012-612x612.ico);")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.baslik = QtWidgets.QLabel(Form)
        self.baslik.setGeometry(QtCore.QRect(190, 70, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("color:white;")
        self.baslik.setObjectName("baslik")
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setGeometry(QtCore.QRect(240, 200, 161, 41))
        self.lineEdit_username.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(240, 250, 161, 41))
        self.lineEdit_password.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(260, 300, 121, 41))
        self.pushButton_login.setStyleSheet("QPushButton{color:white;background-color:rgb(250, 250, 250);border:none;border-radius:20px:}\n"
"QPushButton::hover{\n"
"color:red;\n"
"}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 250, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.baslik.setText(_translate("Form", "SÜPER LİG GİRİŞ"))
        self.pushButton_login.setText(_translate("Form", "Giriş"))
        self.label_3.setText(_translate("Form", "Kullanıcı Adı"))
        self.label_4.setText(_translate("Form", "Şifre"))
import kapi_rc
import saha_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
