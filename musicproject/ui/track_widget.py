# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'track_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_track(object):
    def setupUi(self, track):
        track.setObjectName("track")
        track.resize(410, 74)
        self.record = QtWidgets.QPushButton(track)
        self.record.setEnabled(True)
        self.record.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.record.setStyleSheet("background-color: #1db954; border-radius: 10px;\n"
"")
        self.record.setText("")
        self.record.setObjectName("record")
        self.title_label = QtWidgets.QLabel(track)
        self.title_label.setGeometry(QtCore.QRect(70, 10, 191, 16))
        self.title_label.setStyleSheet("font-family: Montserrat-Black; color: #fff;")
        self.title_label.setText("")
        self.title_label.setObjectName("title_label")
        self.author_label = QtWidgets.QLabel(track)
        self.author_label.setGeometry(QtCore.QRect(70, 40, 181, 16))
        self.author_label.setStyleSheet("font-family: Montserrat-Black; color: #fff;")
        self.author_label.setText("")
        self.author_label.setObjectName("author_label")
        self.duration_label = QtWidgets.QLabel(track)
        self.duration_label.setGeometry(QtCore.QRect(310, 20, 51, 31))
        self.duration_label.setStyleSheet("font-family: Montserrat-Black; color: #fff;")
        self.duration_label.setText("")
        self.duration_label.setObjectName("duration_label")
        self.like_btn = QtWidgets.QPushButton(track)
        self.like_btn.setGeometry(QtCore.QRect(360, 10, 41, 41))
        self.like_btn.setText("")
        self.like_btn.setObjectName("like_btn")
        self.line = QtWidgets.QFrame(track)
        self.line.setGeometry(QtCore.QRect(10, 60, 391, 16))
        self.line.setStyleSheet("color: #fff;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(track)
        QtCore.QMetaObject.connectSlotsByName(track)

    def retranslateUi(self, track):
        _translate = QtCore.QCoreApplication.translate
        track.setWindowTitle(_translate("track", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    track = QtWidgets.QWidget()
    ui = Ui_track()
    ui.setupUi(track)
    track.show()
    sys.exit(app.exec_())
