# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startpage2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 583)
        Dialog.setStyleSheet("background-color: #000")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(260, 190, 281, 61))
        self.login_button.setStyleSheet("QPushButton {background-color: #1db954; color: #f7fdf9; border-radius: 30px;}")
        self.login_button.setObjectName("login_button")
        self.registration_button = QtWidgets.QPushButton(Dialog)
        self.registration_button.setGeometry(QtCore.QRect(260, 270, 281, 61))
        self.registration_button.setStyleSheet("QPushButton {background-color: #1db954; color: #f7fdf9; border-radius: 30px;}")
        self.registration_button.setObjectName("registration_button")
        self.role_up_2 = QtWidgets.QPushButton(Dialog)
        self.role_up_2.setGeometry(QtCore.QRect(700, 10, 41, 31))
        self.role_up_2.setStyleSheet("QPushButton:!hover {background-color: #000;} QPushButton:hover {background-color: #d71526;}")
        self.role_up_2.setText("")
        self.role_up_2.setObjectName("role_up_2")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(750, 10, 41, 31))
        self.exit.setStyleSheet("QPushButton:!hover {background-color: #000;} QPushButton:hover {background-color: #d71526;}")
        self.exit.setText("")
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_button.setText(_translate("Dialog", "ВХОД"))
        self.registration_button.setText(_translate("Dialog", "РЕГИСТРАЦИЯ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())