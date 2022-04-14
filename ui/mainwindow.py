# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.welcomeFrame = QtWidgets.QFrame(self.centralwidget)
        self.welcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcomeFrame.setObjectName("welcomeFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.welcomeFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.welcomeFrame, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 5, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        self.subTracksScrollArea = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subTracksScrollArea.sizePolicy().hasHeightForWidth())
        self.subTracksScrollArea.setSizePolicy(sizePolicy)
        self.subTracksScrollArea.setWidgetResizable(True)
        self.subTracksScrollArea.setObjectName("subTracksScrollArea")
        self.subTracksScrollAreaWidget = QtWidgets.QWidget()
        self.subTracksScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 530, 68))
        self.subTracksScrollAreaWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subTracksScrollAreaWidget.setObjectName("subTracksScrollAreaWidget")
        self.subTracksScrollArea.setWidget(self.subTracksScrollAreaWidget)
        self.gridLayout_2.addWidget(self.subTracksScrollArea, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.audioTracksScrollArea = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioTracksScrollArea.sizePolicy().hasHeightForWidth())
        self.audioTracksScrollArea.setSizePolicy(sizePolicy)
        self.audioTracksScrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.audioTracksScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.audioTracksScrollArea.setWidgetResizable(True)
        self.audioTracksScrollArea.setObjectName("audioTracksScrollArea")
        self.audioTracksScrollAreaWidget = QtWidgets.QWidget()
        self.audioTracksScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 530, 68))
        self.audioTracksScrollAreaWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.audioTracksScrollAreaWidget.setObjectName("audioTracksScrollAreaWidget")
        self.audioTracksScrollArea.setWidget(self.audioTracksScrollAreaWidget)
        self.gridLayout_2.addWidget(self.audioTracksScrollArea, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 8, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 6, 2, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.welcomeLabel.setText(_translate("MainWindow", "Open a file or folder to begin"))
        self.label_3.setText(_translate("MainWindow", "Remove forced subtitles tracks"))
        self.label_2.setText(_translate("MainWindow", "Subtitle Tracks"))
        self.label.setText(_translate("MainWindow", "Audio Tracks"))
        self.pushButton.setText(_translate("MainWindow", "Process files"))
        self.label_4.setText(_translate("MainWindow", "Remove tracks with title containing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tracks remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Misc."))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_folder.setText(_translate("MainWindow", "Open folder"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionClose_current_file_folder.setText(_translate("MainWindow", "Close current file / folder"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
