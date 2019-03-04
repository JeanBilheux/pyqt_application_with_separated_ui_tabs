# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/tab1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyTab1(object):
    def setupUi(self, MyTab1):
        MyTab1.setObjectName("MyTab1")
        MyTab1.resize(670, 585)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyTab1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(MyTab1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textEdit = QtWidgets.QTextEdit(MyTab1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.radioButton = QtWidgets.QRadioButton(MyTab1)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.checkBox = QtWidgets.QCheckBox(MyTab1)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)

        self.retranslateUi(MyTab1)
        QtCore.QMetaObject.connectSlotsByName(MyTab1)

    def retranslateUi(self, MyTab1):
        _translate = QtCore.QCoreApplication.translate
        MyTab1.setWindowTitle(_translate("MyTab1", "Form"))
        MyTab1.setToolTip(_translate("MyTab1", "<html><head/><body><p>My custom tab1</p></body></html>"))
        self.pushButton.setText(_translate("MyTab1", "PushButton"))
        self.radioButton.setText(_translate("MyTab1", "RadioButton"))
        self.checkBox.setText(_translate("MyTab1", "CheckBox"))

