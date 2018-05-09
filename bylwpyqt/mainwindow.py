# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("123")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet("QWidget#centralwidget{background:url(./image/Dueros.jpg)}")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 140, 301, 191))
        self.textEdit.setObjectName("textEdit")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(230, 50, 59, 14))
        self.title.setObjectName("title")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(110, 370, 81, 22))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 370, 81, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 370, 81, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 430, 81, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 430, 81, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 430, 81, 22))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_ding = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ding.setGeometry(QtCore.QRect(110, 100, 30, 30))
        self.pushButton_ding.setObjectName("pushButton_ding")
        self.pushButton_dong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dong.setGeometry(QtCore.QRect(210, 100, 30, 30))
        self.pushButton_dong.setObjectName("pushButton_dong")
        self.pushButton_control = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_control.setGeometry(QtCore.QRect(310, 100, 30, 30))
        self.pushButton_control.setObjectName("pushButton_control")
        
        self.dh11show = QtWidgets.QLabel(self.centralwidget)
        self.dh11show.setGeometry(QtCore.QRect(110, 70, 191, 30))
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.pushButton_1.setStyleSheet("QPushButton:pressed{background-color:green}")
        self.pushButton_2.setStyleSheet("QPushButton:pressed{background-color:green}")
        self.pushButton_3.setStyleSheet("QPushButton:pressed{background-color:green}")
        self.pushButton_4.setStyleSheet("QPushButton:pressed{background-color:green}")
        self.pushButton_5.setStyleSheet("QPushButton:pressed{background-color:green}")
        self.pushButton_6.setStyleSheet("QPushButton:pressed{background-color:green}")
        
        #self.dh11show.setStyleSheet("Color:white")
        #self.title.setStyleSheet("Color:white")
        
        self.pushButton_ding.setStyleSheet("QPushButton{}")
        self.pushButton_dong.setStyleSheet("QPushButton{}")
        self.pushButton_control.setStyleSheet("QPushButton{}")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.hide()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能语音控制系统"))
        self.title.setText(_translate("MainWindow", "主界面"))
        self.pushButton_1.setText(_translate("MainWindow", "文本刷新"))
        self.pushButton_2.setText(_translate("MainWindow", "开启引擎"))
        self.pushButton_3.setText(_translate("MainWindow", "语音识别"))
        self.pushButton_4.setText(_translate("MainWindow", "控制"))
        self.pushButton_5.setText(_translate("MainWindow", "语音合成"))
        self.pushButton_6.setText(_translate("MainWindow", "自动开启"))
        self.dh11show.setText(_translate("MainWindow", "正在读取温湿度，请稍后..."))
        
       

