# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctvd_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(170, 170)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 140, 150, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 150, 20))
        self.label.setObjectName("label")
        self.lineEdit_file_save_path = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_file_save_path.setGeometry(QtCore.QRect(10, 30, 130, 20))
        self.lineEdit_file_save_path.setObjectName("lineEdit_file_save_path")
        self.pushButton_open = QtWidgets.QPushButton(Dialog)
        self.pushButton_open.setGeometry(QtCore.QRect(140, 30, 20, 20))
        self.pushButton_open.setObjectName("pushButton_open")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(110, 60, 50, 20))
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.radioButton_ts = QtWidgets.QRadioButton(Dialog)
        self.radioButton_ts.setGeometry(QtCore.QRect(10, 110, 70, 20))
        self.radioButton_ts.setObjectName("radioButton_ts")
        self.radioButton_mp4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_mp4.setGeometry(QtCore.QRect(90, 110, 70, 20))
        self.radioButton_mp4.setObjectName("radioButton_mp4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 150, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        self.label.setText(_translate("Dialog", "文件保存位置:"))
        self.pushButton_open.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "下载使用线程数:"))
        self.radioButton_ts.setText(_translate("Dialog", "不转码"))
        self.radioButton_mp4.setText(_translate("Dialog", "转码MP4"))
        self.label_3.setText(_translate("Dialog", "视频下载完成后是否转码?"))
