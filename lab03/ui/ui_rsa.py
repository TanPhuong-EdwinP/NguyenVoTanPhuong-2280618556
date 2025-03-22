# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os  
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"  

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 0, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 410, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 200, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 410, 55, 16))
        self.label_5.setObjectName("label_5")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(700, 70, 93, 28))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(120, 550, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(450, 540, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(640, 540, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(910, 540, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(110, 180, 411, 81))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(120, 400, 401, 71))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(620, 180, 421, 81))
        self.txt_info.setObjectName("txt_info")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(620, 400, 421, 81))
        self.txt_sign.setObjectName("txt_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIpher"))
        self.label_2.setText(_translate("MainWindow", "Plain text"))
        self.label_3.setText(_translate("MainWindow", "Cipher text"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Gen  key"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
