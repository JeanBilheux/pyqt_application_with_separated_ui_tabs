# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 629)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1_Data = QtWidgets.QAction(MainWindow)
        self.action1_Data.setObjectName("action1_Data")
        self.action2_Normalization = QtWidgets.QAction(MainWindow)
        self.action2_Normalization.setEnabled(True)
        self.action2_Normalization.setObjectName("action2_Normalization")
        self.action3_Binning = QtWidgets.QAction(MainWindow)
        self.action3_Binning.setObjectName("action3_Binning")
        self.action4_Fitting = QtWidgets.QAction(MainWindow)
        self.action4_Fitting.setObjectName("action4_Fitting")
        self.action5_Results = QtWidgets.QAction(MainWindow)
        self.action5_Results.setObjectName("action5_Results")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action1_Raw_Data = QtWidgets.QAction(MainWindow)
        self.action1_Raw_Data.setObjectName("action1_Raw_Data")
        self.action2_Normalization_2 = QtWidgets.QAction(MainWindow)
        self.action2_Normalization_2.setObjectName("action2_Normalization_2")
        self.action3_Normalized_Data = QtWidgets.QAction(MainWindow)
        self.action3_Normalized_Data.setObjectName("action3_Normalized_Data")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.action1_Data.setText(_translate("MainWindow", "1. Data"))
        self.action2_Normalization.setText(_translate("MainWindow", "2. Normalization"))
        self.action3_Binning.setText(_translate("MainWindow", "4. Binning"))
        self.action4_Fitting.setText(_translate("MainWindow", "5. Fitting"))
        self.action5_Results.setText(_translate("MainWindow", "6. Strain Mapping"))
        self.actionAbout.setText(_translate("MainWindow", "About ..."))
        self.action1_Raw_Data.setText(_translate("MainWindow", "1. Raw Data"))
        self.action2_Normalization_2.setText(_translate("MainWindow", "2. Normalization"))
        self.action3_Normalized_Data.setText(_translate("MainWindow", "3. Normalized Data"))

