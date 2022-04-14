# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aelkaim/Documents/Software/BatchMkvToolbox/QtVersion/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setMaximumSize(QtCore.QSize(150, 80))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_2.setMaximumSize(QtCore.QSize(150, 80))
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.listWidget_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.welcomeFrame = QtWidgets.QFrame(self.centralwidget)
        self.welcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcomeFrame.setObjectName("welcomeFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.welcomeFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 0, 1, 1)
        self.mkvParsingProgressbar = QtWidgets.QProgressBar(self.welcomeFrame)
        self.mkvParsingProgressbar.setMaximum(0)
        self.mkvParsingProgressbar.setProperty("value", 0)
        self.mkvParsingProgressbar.setTextVisible(False)
        self.mkvParsingProgressbar.setObjectName("mkvParsingProgressbar")
        self.gridLayout_3.addWidget(self.mkvParsingProgressbar, 2, 1, 1, 1)
        self.welcomeLabel = QtWidgets.QLabel(self.welcomeFrame)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.gridLayout_3.addWidget(self.welcomeLabel, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.welcomeFrame, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 35))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionOpen_folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_folder.setObjectName("actionOpen_folder")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionClose_current_file_folder = QtWidgets.QAction(MainWindow)
        self.actionClose_current_file_folder.setObjectName("actionClose_current_file_folder")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuTest.addAction(self.actionOpen_file)
        self.menuTest.addAction(self.actionOpen_folder)
        self.menuTest.addAction(self.actionClose_current_file_folder)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionExit)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Subtitle Tracks"))
        self.label.setText(_translate("MainWindow", "Audio Tracks"))
        self.pushButton.setText(_translate("MainWindow", "Process files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tracks remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Misc."))
        self.welcomeLabel.setText(_translate("MainWindow", "Open a file or folder to begin"))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionClose_current_file_folder.setText(_translate("MainWindow", "Close current file / folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
