# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(937, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(850, 750))
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/images/iconoFlipdish.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMenu {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: verdana;\n"
"	color: rgb(0, 0, 0);\n"
"	margin: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"	background-color: rgb(239, 239, 239);\n"
"	color: rgb(50, 0, 149);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QMenuBar {\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-family: verdana;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"	background-color: rgb(238, 238, 238);\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	padding: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	font-family: verdana;\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	margin-top: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	padding: 10px;\n"
"    background-color: rgb(175, 175, 175);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: verdana;\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTabBar::"
                        "tab:!selected:hover {\n"
"	padding: 10px;\n"
"    background-color: rgb(55, 0, 165);\n"
"	color: rgb(255, 255, 255);\n"
"	font-family: verdana;\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: rgb(126, 126, 126);\n"
"}\n"
"\n"
"#sideMenu {\n"
"	background-color: rgb(39, 0, 116);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#mainWindow {\n"
"	background-color: rgb(39, 0, 116);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/images/images/dropdown.png);\n"
"	width: 12px;\n"
"	height:12px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:open {\n"
"	image: url(:/images/images/uparrow.png)\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QListView::item:hover {\n"
"	background-col"
                        "or: rgb(39, 0, 117);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox QListView::item:selected: {\n"
"	background-color: rgb(39, 0, 117);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.actionLoad_Json = QAction(MainWindow)
        self.actionLoad_Json.setObjectName(u"actionLoad_Json")
        self.actionLoad_Json.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/images/images/loadJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoad_Json.setIcon(icon1)
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        self.actionLoad_Json.setFont(font1)
        self.actionLoad_Json.setIconVisibleInMenu(True)
        self.actionLoad_Json.setShortcutVisibleInContextMenu(True)
        self.actionSave_Json = QAction(MainWindow)
        self.actionSave_Json.setObjectName(u"actionSave_Json")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/saveJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_Json.setIcon(icon2)
        self.actionSave_Json.setFont(font1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setFont(font1)
        self.actionApply_Tax_to_All_Sections = QAction(MainWindow)
        self.actionApply_Tax_to_All_Sections.setObjectName(u"actionApply_Tax_to_All_Sections")
        self.actionApply_Tax_to_All_Sections.setFont(font1)
        self.actionRemove_Tax_from_All_Sections = QAction(MainWindow)
        self.actionRemove_Tax_from_All_Sections.setObjectName(u"actionRemove_Tax_from_All_Sections")
        self.actionRemove_Tax_from_All_Sections.setFont(font1)
        self.actionPrice_Options = QAction(MainWindow)
        self.actionPrice_Options.setObjectName(u"actionPrice_Options")
        self.actionCoca_ColaChecker = QAction(MainWindow)
        self.actionCoca_ColaChecker.setObjectName(u"actionCoca_ColaChecker")
        self.actionParse_JSON = QAction(MainWindow)
        self.actionParse_JSON.setObjectName(u"actionParse_JSON")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.sideMenu = QWidget(self.centralwidget)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setMinimumSize(QSize(175, 0))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        self.sideMenu.setFont(font2)
        self.sideMenu.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 5px;\n"
"	background-color: rgb(249, 249, 249);\n"
"	border:none;\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: rgb(75, 76, 113); color: rgb(138, 138, 138)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sideMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.modifyJson = QWidget(self.sideMenu)
        self.modifyJson.setObjectName(u"modifyJson")
        self.verticalLayout_2 = QVBoxLayout(self.modifyJson)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DRINKSBUTTON = QPushButton(self.modifyJson)
        self.DRINKSBUTTON.setObjectName(u"DRINKSBUTTON")
        self.DRINKSBUTTON.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(9)
        self.DRINKSBUTTON.setFont(font3)
        self.DRINKSBUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.DRINKSBUTTON.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.DRINKSBUTTON)

        self.PRICEBUTTON = QPushButton(self.modifyJson)
        self.PRICEBUTTON.setObjectName(u"PRICEBUTTON")
        self.PRICEBUTTON.setEnabled(False)
        self.PRICEBUTTON.setFont(font3)
        self.PRICEBUTTON.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.PRICEBUTTON)

        self.TAXBUTTON = QPushButton(self.modifyJson)
        self.TAXBUTTON.setObjectName(u"TAXBUTTON")
        self.TAXBUTTON.setEnabled(False)
        self.TAXBUTTON.setFont(font3)
        self.TAXBUTTON.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.TAXBUTTON)

        self.PARSEBUTTON = QPushButton(self.modifyJson)
        self.PARSEBUTTON.setObjectName(u"PARSEBUTTON")
        self.PARSEBUTTON.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.PARSEBUTTON.setFont(font4)
        self.PARSEBUTTON.setCursor(QCursor(Qt.PointingHandCursor))
        self.PARSEBUTTON.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.PARSEBUTTON)


        self.verticalLayout.addWidget(self.modifyJson, 0, Qt.AlignVCenter)

        self.parseJson = QWidget(self.sideMenu)
        self.parseJson.setObjectName(u"parseJson")
        self.parseJson.setEnabled(True)
        self.parseJson.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.parseJson)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TAXABLEYES = QPushButton(self.parseJson)
        self.TAXABLEYES.setObjectName(u"TAXABLEYES")
        self.TAXABLEYES.setEnabled(False)
        self.TAXABLEYES.setFont(font1)

        self.verticalLayout_3.addWidget(self.TAXABLEYES)

        self.ADDTAGSBUTTON = QPushButton(self.parseJson)
        self.ADDTAGSBUTTON.setObjectName(u"ADDTAGSBUTTON")
        self.ADDTAGSBUTTON.setEnabled(False)
        self.ADDTAGSBUTTON.setFont(font1)

        self.verticalLayout_3.addWidget(self.ADDTAGSBUTTON)

        self.REMOVETAGSBUTTON = QPushButton(self.parseJson)
        self.REMOVETAGSBUTTON.setObjectName(u"REMOVETAGSBUTTON")
        self.REMOVETAGSBUTTON.setEnabled(False)
        self.REMOVETAGSBUTTON.setFont(font1)

        self.verticalLayout_3.addWidget(self.REMOVETAGSBUTTON)

        self.ADDSNOOZETAGSBUTTON = QPushButton(self.parseJson)
        self.ADDSNOOZETAGSBUTTON.setObjectName(u"ADDSNOOZETAGSBUTTON")
        self.ADDSNOOZETAGSBUTTON.setEnabled(False)
        self.ADDSNOOZETAGSBUTTON.setFont(font1)

        self.verticalLayout_3.addWidget(self.ADDSNOOZETAGSBUTTON)

        self.GETITEMSNAMEBUTTON = QPushButton(self.parseJson)
        self.GETITEMSNAMEBUTTON.setObjectName(u"GETITEMSNAMEBUTTON")
        self.GETITEMSNAMEBUTTON.setEnabled(False)
        self.GETITEMSNAMEBUTTON.setFont(font1)

        self.verticalLayout_3.addWidget(self.GETITEMSNAMEBUTTON)


        self.verticalLayout.addWidget(self.parseJson, 0, Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.sideMenu)

        self.mainWindow = QWidget(self.centralwidget)
        self.mainWindow.setObjectName(u"mainWindow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWindow.sizePolicy().hasHeightForWidth())
        self.mainWindow.setSizePolicy(sizePolicy1)
        self.mainWindow.setMinimumSize(QSize(500, 0))
        self.verticalLayout_4 = QVBoxLayout(self.mainWindow)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.mainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_6 = QHBoxLayout(self.homePage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(524, 161))
        self.label.setPixmap(QPixmap(u":/images/images/FDLOGOmet2.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.homePage)
        self.pricePage = QWidget()
        self.pricePage.setObjectName(u"pricePage")
        self.pricePage.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.pricePage)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 0)
        self.topOptions = QWidget(self.pricePage)
        self.topOptions.setObjectName(u"topOptions")
        self.horizontalLayout_7 = QHBoxLayout(self.topOptions)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.widget = QWidget(self.topOptions)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.priceListSelected = QComboBox(self.widget)
        self.priceListSelected.addItem("")
        self.priceListSelected.addItem("")
        self.priceListSelected.addItem("")
        self.priceListSelected.addItem("")
        self.priceListSelected.setObjectName(u"priceListSelected")
        self.priceListSelected.setMinimumSize(QSize(350, 0))
        self.priceListSelected.setMaximumSize(QSize(350, 16777215))
        self.priceListSelected.setFont(font1)
        self.priceListSelected.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceListSelected.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.verticalLayout_10.addWidget(self.priceListSelected)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.labelInfo2 = QLabel(self.frame_2)
        self.labelInfo2.setObjectName(u"labelInfo2")
        self.labelInfo2.setFont(font1)
        self.labelInfo2.setStyleSheet(u"padding-top: 5px;")
        self.labelInfo2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.labelInfo2.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.labelInfo2)

        self.price = QLabel(self.frame_2)
        self.price.setObjectName(u"price")
        self.price.setFont(font1)
        self.price.setStyleSheet(u"padding-top:5px")
        self.price.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.price.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.price)


        self.verticalLayout_10.addWidget(self.frame_2)


        self.horizontalLayout_7.addWidget(self.widget)

        self.horizontalSpacer_28 = QSpacerItem(50, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_28)

        self.widget_2 = QWidget(self.topOptions)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leIncrease = QLineEdit(self.widget_2)
        self.leIncrease.setObjectName(u"leIncrease")
        self.leIncrease.setMinimumSize(QSize(150, 0))
        self.leIncrease.setMaximumSize(QSize(150, 16777215))
        self.leIncrease.setFont(font1)
        self.leIncrease.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.horizontalLayout.addWidget(self.leIncrease)


        self.horizontalLayout_7.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.horizontalSpacer_21 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_21)


        self.verticalLayout_6.addWidget(self.topOptions)

        self.bottomOptions = QWidget(self.pricePage)
        self.bottomOptions.setObjectName(u"bottomOptions")
        self.horizontalLayout_3 = QHBoxLayout(self.bottomOptions)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(195, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_22)

        self.rounding = QGroupBox(self.bottomOptions)
        self.rounding.setObjectName(u"rounding")
        self.rounding.setMinimumSize(QSize(250, 0))
        self.rounding.setFont(font1)
        self.rounding.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding-top: 10px;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.rounding)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.roundTo10 = QRadioButton(self.rounding)
        self.roundTo10.setObjectName(u"roundTo10")
        self.roundTo10.setFont(font1)

        self.horizontalLayout_4.addWidget(self.roundTo10)

        self.roundTo5 = QRadioButton(self.rounding)
        self.roundTo5.setObjectName(u"roundTo5")
        self.roundTo5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.roundTo5)

        self.roundTo99 = QRadioButton(self.rounding)
        self.roundTo99.setObjectName(u"roundTo99")
        self.roundTo99.setFont(font1)

        self.horizontalLayout_4.addWidget(self.roundTo99)

        self.roundToInt = QRadioButton(self.rounding)
        self.roundToInt.setObjectName(u"roundToInt")
        self.roundToInt.setFont(font1)

        self.horizontalLayout_4.addWidget(self.roundToInt)


        self.horizontalLayout_3.addWidget(self.rounding)

        self.horizontalSpacer_23 = QSpacerItem(195, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_23)


        self.verticalLayout_6.addWidget(self.bottomOptions)

        self.tabWidget_2 = QTabWidget(self.pricePage)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy2)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        sizePolicy.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_13 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.sectionModification_2 = QGroupBox(self.tab_5)
        self.sectionModification_2.setObjectName(u"sectionModification_2")
        self.sectionModification_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sectionModification_2.sizePolicy().hasHeightForWidth())
        self.sectionModification_2.setSizePolicy(sizePolicy)
        self.sectionModification_2.setMinimumSize(QSize(350, 0))
        self.sectionModification_2.setMaximumSize(QSize(350, 16777215))
        self.sectionModification_2.setFont(font1)
        self.gridLayout_12 = QGridLayout(self.sectionModification_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setVerticalSpacing(5)
        self.gridLayout_12.setContentsMargins(0, 10, 0, 0)
        self.addSection_2 = QPushButton(self.sectionModification_2)
        self.addSection_2.setObjectName(u"addSection_2")
        self.addSection_2.setFont(font1)
        self.addSection_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSection_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_12.addWidget(self.addSection_2, 3, 1, 1, 2)

        self.sectionList_2 = QComboBox(self.sectionModification_2)
        self.sectionList_2.setObjectName(u"sectionList_2")
        self.sectionList_2.setEnabled(True)
        self.sectionList_2.setFont(font1)
        self.sectionList_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.sectionList_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_12.addWidget(self.sectionList_2, 1, 1, 1, 2)

        self.priceImpSec = QPushButton(self.sectionModification_2)
        self.priceImpSec.setObjectName(u"priceImpSec")
        self.priceImpSec.setFont(font1)
        self.priceImpSec.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceImpSec.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_12.addWidget(self.priceImpSec, 6, 1, 1, 2)

        self.addedSections_2 = QTextEdit(self.sectionModification_2)
        self.addedSections_2.setObjectName(u"addedSections_2")
        self.addedSections_2.setFont(font1)
        self.addedSections_2.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedSections_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_12.addWidget(self.addedSections_2, 5, 1, 1, 2)

        self.labelSection_2 = QLabel(self.sectionModification_2)
        self.labelSection_2.setObjectName(u"labelSection_2")
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(10)
        self.labelSection_2.setFont(font5)

        self.gridLayout_12.addWidget(self.labelSection_2, 0, 1, 1, 2, Qt.AlignHCenter)

        self.modOS = QCheckBox(self.sectionModification_2)
        self.modOS.setObjectName(u"modOS")
        self.modOS.setFont(font1)
        self.modOS.setCheckable(True)

        self.gridLayout_12.addWidget(self.modOS, 2, 2, 1, 1)

        self.modMO = QCheckBox(self.sectionModification_2)
        self.modMO.setObjectName(u"modMO")
        self.modMO.setFont(font1)
        self.modMO.setCheckable(True)
        self.modMO.setChecked(True)

        self.gridLayout_12.addWidget(self.modMO, 2, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.sectionModification_2)

        self.horizontalSpacer_14 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_15 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.itemsModification_2 = QGroupBox(self.tab_6)
        self.itemsModification_2.setObjectName(u"itemsModification_2")
        sizePolicy.setHeightForWidth(self.itemsModification_2.sizePolicy().hasHeightForWidth())
        self.itemsModification_2.setSizePolicy(sizePolicy)
        self.itemsModification_2.setMinimumSize(QSize(350, 0))
        self.itemsModification_2.setMaximumSize(QSize(350, 16777215))
        self.itemsModification_2.setFont(font1)
        self.gridLayout_14 = QGridLayout(self.itemsModification_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setVerticalSpacing(5)
        self.gridLayout_14.setContentsMargins(0, 10, 0, 0)
        self.priceImpIt = QPushButton(self.itemsModification_2)
        self.priceImpIt.setObjectName(u"priceImpIt")
        self.priceImpIt.setFont(font1)
        self.priceImpIt.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceImpIt.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_14.addWidget(self.priceImpIt, 6, 0, 1, 2)

        self.itemsList_2 = QComboBox(self.itemsModification_2)
        self.itemsList_2.setObjectName(u"itemsList_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.itemsList_2.sizePolicy().hasHeightForWidth())
        self.itemsList_2.setSizePolicy(sizePolicy3)
        self.itemsList_2.setFont(font1)
        self.itemsList_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.itemsList_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")
        self.itemsList_2.setEditable(False)
        self.itemsList_2.setModelColumn(0)

        self.gridLayout_14.addWidget(self.itemsList_2, 1, 0, 1, 2)

        self.addedItems_2 = QTextEdit(self.itemsModification_2)
        self.addedItems_2.setObjectName(u"addedItems_2")
        self.addedItems_2.setFont(font1)
        self.addedItems_2.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedItems_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_14.addWidget(self.addedItems_2, 5, 0, 1, 2)

        self.labelItems_2 = QLabel(self.itemsModification_2)
        self.labelItems_2.setObjectName(u"labelItems_2")
        self.labelItems_2.setFont(font5)

        self.gridLayout_14.addWidget(self.labelItems_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addItem_2 = QPushButton(self.itemsModification_2)
        self.addItem_2.setObjectName(u"addItem_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.addItem_2.sizePolicy().hasHeightForWidth())
        self.addItem_2.setSizePolicy(sizePolicy4)
        self.addItem_2.setFont(font1)
        self.addItem_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addItem_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_14.addWidget(self.addItem_2, 3, 0, 1, 2)

        self.modMO1 = QCheckBox(self.itemsModification_2)
        self.modMO1.setObjectName(u"modMO1")
        self.modMO1.setFont(font1)
        self.modMO1.setChecked(True)

        self.gridLayout_14.addWidget(self.modMO1, 2, 0, 1, 1)

        self.modSO1 = QCheckBox(self.itemsModification_2)
        self.modSO1.setObjectName(u"modSO1")
        self.modSO1.setFont(font1)

        self.gridLayout_14.addWidget(self.modSO1, 2, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.itemsModification_2)

        self.horizontalSpacer_16 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_17 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.optionSetModification_2 = QGroupBox(self.tab_7)
        self.optionSetModification_2.setObjectName(u"optionSetModification_2")
        sizePolicy.setHeightForWidth(self.optionSetModification_2.sizePolicy().hasHeightForWidth())
        self.optionSetModification_2.setSizePolicy(sizePolicy)
        self.optionSetModification_2.setMinimumSize(QSize(350, 0))
        self.optionSetModification_2.setMaximumSize(QSize(350, 16777215))
        self.optionSetModification_2.setFont(font1)
        self.gridLayout_16 = QGridLayout(self.optionSetModification_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(0)
        self.gridLayout_16.setVerticalSpacing(5)
        self.gridLayout_16.setContentsMargins(0, 10, 0, 0)
        self.addOS_2 = QPushButton(self.optionSetModification_2)
        self.addOS_2.setObjectName(u"addOS_2")
        self.addOS_2.setFont(font1)
        self.addOS_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addOS_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px\n"
"")

        self.gridLayout_16.addWidget(self.addOS_2, 3, 0, 1, 2)

        self.osList_2 = QComboBox(self.optionSetModification_2)
        self.osList_2.setObjectName(u"osList_2")
        self.osList_2.setFont(font1)
        self.osList_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.osList_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_16.addWidget(self.osList_2, 1, 0, 1, 2)

        self.labelOS_2 = QLabel(self.optionSetModification_2)
        self.labelOS_2.setObjectName(u"labelOS_2")
        self.labelOS_2.setFont(font1)

        self.gridLayout_16.addWidget(self.labelOS_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.priceImpOS = QPushButton(self.optionSetModification_2)
        self.priceImpOS.setObjectName(u"priceImpOS")
        self.priceImpOS.setFont(font1)
        self.priceImpOS.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceImpOS.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_16.addWidget(self.priceImpOS, 5, 0, 1, 2)

        self.optionsList_2 = QComboBox(self.optionSetModification_2)
        self.optionsList_2.setObjectName(u"optionsList_2")
        self.optionsList_2.setFont(font1)
        self.optionsList_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.optionsList_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_16.addWidget(self.optionsList_2, 2, 0, 1, 2)

        self.addedOS_2 = QTextEdit(self.optionSetModification_2)
        self.addedOS_2.setObjectName(u"addedOS_2")
        self.addedOS_2.setFont(font1)
        self.addedOS_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_16.addWidget(self.addedOS_2, 4, 0, 1, 2)


        self.horizontalLayout_13.addWidget(self.optionSetModification_2)

        self.horizontalSpacer_18 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_19 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)

        self.groupBox_2 = QGroupBox(self.tab_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(350, 0))
        self.groupBox_2.setMaximumSize(QSize(350, 16777215))
        self.groupBox_2.setFont(font1)
        self.gridLayout_18 = QGridLayout(self.groupBox_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(5)
        self.gridLayout_18.setContentsMargins(0, 10, 0, 0)
        self.modMO2 = QCheckBox(self.groupBox_2)
        self.modMO2.setObjectName(u"modMO2")
        self.modMO2.setFont(font1)
        self.modMO2.setCheckable(True)
        self.modMO2.setChecked(True)

        self.gridLayout_18.addWidget(self.modMO2, 3, 0, 1, 1)

        self.modSO2 = QCheckBox(self.groupBox_2)
        self.modSO2.setObjectName(u"modSO2")
        self.modSO2.setFont(font1)

        self.gridLayout_18.addWidget(self.modSO2, 3, 1, 1, 1)

        self.smartSearchList_2 = QComboBox(self.groupBox_2)
        self.smartSearchList_2.setObjectName(u"smartSearchList_2")
        self.smartSearchList_2.setFont(font1)
        self.smartSearchList_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.smartSearchList_2.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_18.addWidget(self.smartSearchList_2, 2, 0, 1, 2)

        self.leSmartSearch_2 = QLineEdit(self.groupBox_2)
        self.leSmartSearch_2.setObjectName(u"leSmartSearch_2")
        self.leSmartSearch_2.setFont(font1)
        self.leSmartSearch_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_18.addWidget(self.leSmartSearch_2, 1, 0, 1, 2)

        self.labelSmartSearch_2 = QLabel(self.groupBox_2)
        self.labelSmartSearch_2.setObjectName(u"labelSmartSearch_2")
        self.labelSmartSearch_2.setFont(font1)

        self.gridLayout_18.addWidget(self.labelSmartSearch_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addSmartSearch_2 = QPushButton(self.groupBox_2)
        self.addSmartSearch_2.setObjectName(u"addSmartSearch_2")
        self.addSmartSearch_2.setFont(font1)
        self.addSmartSearch_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSmartSearch_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_18.addWidget(self.addSmartSearch_2, 6, 0, 1, 2)

        self.addedSS_2 = QTextEdit(self.groupBox_2)
        self.addedSS_2.setObjectName(u"addedSS_2")
        self.addedSS_2.setFont(font1)
        self.addedSS_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_18.addWidget(self.addedSS_2, 7, 0, 1, 2)

        self.priceImpSmartSearch = QPushButton(self.groupBox_2)
        self.priceImpSmartSearch.setObjectName(u"priceImpSmartSearch")
        self.priceImpSmartSearch.setFont(font1)
        self.priceImpSmartSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceImpSmartSearch.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_18.addWidget(self.priceImpSmartSearch, 8, 0, 1, 2)


        self.horizontalLayout_14.addWidget(self.groupBox_2)

        self.horizontalSpacer_20 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_20)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout_6.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.pricePage)
        self.taxPage = QWidget()
        self.taxPage.setObjectName(u"taxPage")
        self.verticalLayout_7 = QVBoxLayout(self.taxPage)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 0)
        self.topOptionsTax = QWidget(self.taxPage)
        self.topOptionsTax.setObjectName(u"topOptionsTax")
        self.horizontalLayout_5 = QHBoxLayout(self.topOptionsTax)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.topSubOptionsTax = QWidget(self.topOptionsTax)
        self.topSubOptionsTax.setObjectName(u"topSubOptionsTax")
        self.topSubOptionsTax.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.topSubOptionsTax)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelTax = QLabel(self.topSubOptionsTax)
        self.labelTax.setObjectName(u"labelTax")
        self.labelTax.setFont(font1)

        self.verticalLayout_8.addWidget(self.labelTax)

        self.taxList = QComboBox(self.topSubOptionsTax)
        self.taxList.setObjectName(u"taxList")
        self.taxList.setMinimumSize(QSize(150, 0))
        self.taxList.setFont(font1)
        self.taxList.setCursor(QCursor(Qt.PointingHandCursor))
        self.taxList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"}")

        self.verticalLayout_8.addWidget(self.taxList)


        self.horizontalLayout_5.addWidget(self.topSubOptionsTax)

        self.horizontalSpacer = QSpacerItem(213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addWidget(self.topOptionsTax)

        self.tabWidget = QTabWidget(self.taxPage)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font1)
        self.horizontalLayout_15 = QHBoxLayout(self.tab)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_8 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.sectionModification = QGroupBox(self.tab)
        self.sectionModification.setObjectName(u"sectionModification")
        sizePolicy.setHeightForWidth(self.sectionModification.sizePolicy().hasHeightForWidth())
        self.sectionModification.setSizePolicy(sizePolicy)
        self.sectionModification.setMinimumSize(QSize(350, 0))
        self.sectionModification.setMaximumSize(QSize(350, 16777215))
        self.sectionModification.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.sectionModification)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 0)
        self.addSection = QPushButton(self.sectionModification)
        self.addSection.setObjectName(u"addSection")
        self.addSection.setFont(font1)
        self.addSection.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSection.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_2.addWidget(self.addSection, 3, 1, 1, 2)

        self.sectionList = QComboBox(self.sectionModification)
        self.sectionList.setObjectName(u"sectionList")
        self.sectionList.setEnabled(True)
        self.sectionList.setFont(font1)
        self.sectionList.setCursor(QCursor(Qt.PointingHandCursor))
        self.sectionList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_2.addWidget(self.sectionList, 1, 1, 1, 2)

        self.taxImpSec = QPushButton(self.sectionModification)
        self.taxImpSec.setObjectName(u"taxImpSec")
        self.taxImpSec.setFont(font1)
        self.taxImpSec.setCursor(QCursor(Qt.PointingHandCursor))
        self.taxImpSec.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.taxImpSec, 6, 1, 1, 2)

        self.addedSections = QTextEdit(self.sectionModification)
        self.addedSections.setObjectName(u"addedSections")
        self.addedSections.setFont(font1)
        self.addedSections.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_2.addWidget(self.addedSections, 5, 1, 1, 2)

        self.labelSection = QLabel(self.sectionModification)
        self.labelSection.setObjectName(u"labelSection")
        self.labelSection.setFont(font5)

        self.gridLayout_2.addWidget(self.labelSection, 0, 1, 1, 2, Qt.AlignHCenter)


        self.horizontalLayout_15.addWidget(self.sectionModification)

        self.horizontalSpacer_6 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setFont(font1)
        self.horizontalLayout_16 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_7 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.itemsModification = QGroupBox(self.tab_2)
        self.itemsModification.setObjectName(u"itemsModification")
        sizePolicy.setHeightForWidth(self.itemsModification.sizePolicy().hasHeightForWidth())
        self.itemsModification.setSizePolicy(sizePolicy)
        self.itemsModification.setMinimumSize(QSize(350, 0))
        self.itemsModification.setMaximumSize(QSize(350, 16777215))
        self.itemsModification.setFont(font1)
        self.gridLayout = QGridLayout(self.itemsModification)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 10, 0, 0)
        self.taxImpIt = QPushButton(self.itemsModification)
        self.taxImpIt.setObjectName(u"taxImpIt")
        self.taxImpIt.setFont(font1)
        self.taxImpIt.setCursor(QCursor(Qt.PointingHandCursor))
        self.taxImpIt.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.taxImpIt, 6, 0, 1, 2)

        self.itemsList = QComboBox(self.itemsModification)
        self.itemsList.setObjectName(u"itemsList")
        sizePolicy3.setHeightForWidth(self.itemsList.sizePolicy().hasHeightForWidth())
        self.itemsList.setSizePolicy(sizePolicy3)
        self.itemsList.setFont(font1)
        self.itemsList.setCursor(QCursor(Qt.PointingHandCursor))
        self.itemsList.setFocusPolicy(Qt.TabFocus)
        self.itemsList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")
        self.itemsList.setModelColumn(0)

        self.gridLayout.addWidget(self.itemsList, 1, 0, 1, 2)

        self.addedItems = QTextEdit(self.itemsModification)
        self.addedItems.setObjectName(u"addedItems")
        self.addedItems.setFont(font1)
        self.addedItems.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.addedItems, 5, 0, 1, 2)

        self.labelItems = QLabel(self.itemsModification)
        self.labelItems.setObjectName(u"labelItems")
        self.labelItems.setFont(font5)

        self.gridLayout.addWidget(self.labelItems, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addItem = QPushButton(self.itemsModification)
        self.addItem.setObjectName(u"addItem")
        sizePolicy4.setHeightForWidth(self.addItem.sizePolicy().hasHeightForWidth())
        self.addItem.setSizePolicy(sizePolicy4)
        self.addItem.setFont(font1)
        self.addItem.setCursor(QCursor(Qt.PointingHandCursor))
        self.addItem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout.addWidget(self.addItem, 3, 0, 1, 2)


        self.horizontalLayout_16.addWidget(self.itemsModification)

        self.horizontalSpacer_2 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font1)
        self.horizontalLayout_17 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_9 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.optionSetModification = QGroupBox(self.tab_3)
        self.optionSetModification.setObjectName(u"optionSetModification")
        sizePolicy.setHeightForWidth(self.optionSetModification.sizePolicy().hasHeightForWidth())
        self.optionSetModification.setSizePolicy(sizePolicy)
        self.optionSetModification.setMinimumSize(QSize(350, 0))
        self.optionSetModification.setMaximumSize(QSize(350, 16777215))
        self.optionSetModification.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.optionSetModification)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(0, 10, 0, 0)
        self.addOS = QPushButton(self.optionSetModification)
        self.addOS.setObjectName(u"addOS")
        self.addOS.setFont(font1)
        self.addOS.setCursor(QCursor(Qt.PointingHandCursor))
        self.addOS.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_4.addWidget(self.addOS, 3, 0, 1, 2)

        self.osList = QComboBox(self.optionSetModification)
        self.osList.setObjectName(u"osList")
        self.osList.setFont(font1)
        self.osList.setCursor(QCursor(Qt.PointingHandCursor))
        self.osList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_4.addWidget(self.osList, 1, 0, 1, 2)

        self.labelOS = QLabel(self.optionSetModification)
        self.labelOS.setObjectName(u"labelOS")
        self.labelOS.setFont(font1)

        self.gridLayout_4.addWidget(self.labelOS, 0, 0, 1, 2, Qt.AlignHCenter)

        self.taxImpOS = QPushButton(self.optionSetModification)
        self.taxImpOS.setObjectName(u"taxImpOS")
        self.taxImpOS.setFont(font1)
        self.taxImpOS.setCursor(QCursor(Qt.PointingHandCursor))
        self.taxImpOS.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.taxImpOS, 5, 0, 1, 2)

        self.optionsList = QComboBox(self.optionSetModification)
        self.optionsList.setObjectName(u"optionsList")
        self.optionsList.setFont(font1)
        self.optionsList.setCursor(QCursor(Qt.PointingHandCursor))
        self.optionsList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_4.addWidget(self.optionsList, 2, 0, 1, 2)

        self.addedOS = QTextEdit(self.optionSetModification)
        self.addedOS.setObjectName(u"addedOS")
        self.addedOS.setFont(font1)
        self.addedOS.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_4.addWidget(self.addedOS, 4, 0, 1, 2)


        self.horizontalLayout_17.addWidget(self.optionSetModification)

        self.horizontalSpacer_3 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_10 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)

        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.groupBox.setMaximumSize(QSize(350, 16777215))
        self.groupBox.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(0, 10, 0, 0)
        self.leSmartSearch = QLineEdit(self.groupBox)
        self.leSmartSearch.setObjectName(u"leSmartSearch")
        self.leSmartSearch.setFont(font1)
        self.leSmartSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border: 1px solid;\n"
"border-radius: 5px\n"
"")

        self.gridLayout_5.addWidget(self.leSmartSearch, 1, 0, 1, 1)

        self.labelSmartSearch = QLabel(self.groupBox)
        self.labelSmartSearch.setObjectName(u"labelSmartSearch")
        self.labelSmartSearch.setFont(font1)
        self.labelSmartSearch.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.labelSmartSearch, 0, 0, 1, 1, Qt.AlignHCenter)

        self.addedSS = QTextEdit(self.groupBox)
        self.addedSS.setObjectName(u"addedSS")
        self.addedSS.setFont(font1)
        self.addedSS.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_5.addWidget(self.addedSS, 4, 0, 1, 1)

        self.taxImpSmartSearch = QPushButton(self.groupBox)
        self.taxImpSmartSearch.setObjectName(u"taxImpSmartSearch")
        self.taxImpSmartSearch.setFont(font1)
        self.taxImpSmartSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.taxImpSmartSearch.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_5.addWidget(self.taxImpSmartSearch, 5, 0, 1, 1)

        self.addSmartSearch = QPushButton(self.groupBox)
        self.addSmartSearch.setObjectName(u"addSmartSearch")
        self.addSmartSearch.setFont(font1)
        self.addSmartSearch.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSmartSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_5.addWidget(self.addSmartSearch, 3, 0, 1, 1)

        self.smartSearchList = QComboBox(self.groupBox)
        self.smartSearchList.setObjectName(u"smartSearchList")
        self.smartSearchList.setFont(font1)
        self.smartSearchList.setCursor(QCursor(Qt.PointingHandCursor))
        self.smartSearchList.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_5.addWidget(self.smartSearchList, 2, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.groupBox)

        self.horizontalSpacer_4 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_4)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.taxPage)
        self.tagsPage = QWidget()
        self.tagsPage.setObjectName(u"tagsPage")
        self.verticalLayout_14 = QVBoxLayout(self.tagsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_2 = QLabel(self.tagsPage)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(9)
        font6.setBold(True)
        self.label_2.setFont(font6)
        self.label_2.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_2)

        self.topOptions_2 = QWidget(self.tagsPage)
        self.topOptions_2.setObjectName(u"topOptions_2")
        self.horizontalLayout_19 = QHBoxLayout(self.topOptions_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.topOptions_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widgetTag = QWidget(self.frame_4)
        self.widgetTag.setObjectName(u"widgetTag")
        sizePolicy.setHeightForWidth(self.widgetTag.sizePolicy().hasHeightForWidth())
        self.widgetTag.setSizePolicy(sizePolicy)
        self.horizontalLayout_20 = QHBoxLayout(self.widgetTag)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_29 = QSpacerItem(195, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_29)

        self.labelTag = QLabel(self.widgetTag)
        self.labelTag.setObjectName(u"labelTag")
        self.labelTag.setFont(font1)

        self.horizontalLayout_20.addWidget(self.labelTag)

        self.lineEditTag = QLineEdit(self.widgetTag)
        self.lineEditTag.setObjectName(u"lineEditTag")
        self.lineEditTag.setMinimumSize(QSize(200, 0))
        self.lineEditTag.setMaximumSize(QSize(150, 16777215))
        self.lineEditTag.setFont(font1)
        self.lineEditTag.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.horizontalLayout_20.addWidget(self.lineEditTag)

        self.horizontalSpacer_33 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_33)


        self.horizontalLayout_23.addWidget(self.widgetTag)

        self.widget_3 = QWidget(self.frame_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_12 = QVBoxLayout(self.widget_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_23.addWidget(self.widget_3)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.labelInfoTag = QLabel(self.frame_3)
        self.labelInfoTag.setObjectName(u"labelInfoTag")
        self.labelInfoTag.setMinimumSize(QSize(100, 0))
        self.labelInfoTag.setMaximumSize(QSize(600, 16777215))
        self.labelInfoTag.setFont(font1)
        self.labelInfoTag.setStyleSheet(u"padding-top: 5px;")
        self.labelInfoTag.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.labelInfoTag.setWordWrap(False)

        self.verticalLayout_13.addWidget(self.labelInfoTag, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_19.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.topOptions_2)

        self.tabWidget_5 = QTabWidget(self.tagsPage)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        sizePolicy2.setHeightForWidth(self.tabWidget_5.sizePolicy().hasHeightForWidth())
        self.tabWidget_5.setSizePolicy(sizePolicy2)
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_21 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_34 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_34)

        self.sectionModification_4 = QGroupBox(self.tab_11)
        self.sectionModification_4.setObjectName(u"sectionModification_4")
        self.sectionModification_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sectionModification_4.sizePolicy().hasHeightForWidth())
        self.sectionModification_4.setSizePolicy(sizePolicy)
        self.sectionModification_4.setMinimumSize(QSize(350, 0))
        self.sectionModification_4.setMaximumSize(QSize(350, 16777215))
        self.sectionModification_4.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.sectionModification_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(5)
        self.gridLayout_13.setContentsMargins(0, 10, 0, 0)
        self.labelSection_4 = QLabel(self.sectionModification_4)
        self.labelSection_4.setObjectName(u"labelSection_4")
        self.labelSection_4.setFont(font5)

        self.gridLayout_13.addWidget(self.labelSection_4, 0, 1, 1, 2, Qt.AlignHCenter)

        self.tagsImpSec = QPushButton(self.sectionModification_4)
        self.tagsImpSec.setObjectName(u"tagsImpSec")
        self.tagsImpSec.setFont(font1)
        self.tagsImpSec.setCursor(QCursor(Qt.PointingHandCursor))
        self.tagsImpSec.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_13.addWidget(self.tagsImpSec, 5, 1, 1, 2)

        self.sectionList_4 = QComboBox(self.sectionModification_4)
        self.sectionList_4.setObjectName(u"sectionList_4")
        self.sectionList_4.setEnabled(True)
        self.sectionList_4.setFont(font1)
        self.sectionList_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.sectionList_4.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_13.addWidget(self.sectionList_4, 1, 1, 1, 2)

        self.addedSections_4 = QTextEdit(self.sectionModification_4)
        self.addedSections_4.setObjectName(u"addedSections_4")
        self.addedSections_4.setFont(font1)
        self.addedSections_4.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedSections_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_13.addWidget(self.addedSections_4, 4, 1, 1, 2)

        self.addSection_4 = QPushButton(self.sectionModification_4)
        self.addSection_4.setObjectName(u"addSection_4")
        self.addSection_4.setFont(font1)
        self.addSection_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSection_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_13.addWidget(self.addSection_4, 2, 1, 1, 2)


        self.horizontalLayout_21.addWidget(self.sectionModification_4)

        self.horizontalSpacer_35 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_35)

        self.tabWidget_5.addTab(self.tab_11, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tab_13.setStyleSheet(u"")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_13)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_36 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_36)

        self.itemsModification_4 = QGroupBox(self.tab_13)
        self.itemsModification_4.setObjectName(u"itemsModification_4")
        sizePolicy.setHeightForWidth(self.itemsModification_4.sizePolicy().hasHeightForWidth())
        self.itemsModification_4.setSizePolicy(sizePolicy)
        self.itemsModification_4.setMinimumSize(QSize(350, 0))
        self.itemsModification_4.setMaximumSize(QSize(350, 16777215))
        self.itemsModification_4.setFont(font1)
        self.gridLayout_15 = QGridLayout(self.itemsModification_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(0)
        self.gridLayout_15.setVerticalSpacing(5)
        self.gridLayout_15.setContentsMargins(0, 10, 0, 0)
        self.itemsList_4 = QComboBox(self.itemsModification_4)
        self.itemsList_4.setObjectName(u"itemsList_4")
        sizePolicy3.setHeightForWidth(self.itemsList_4.sizePolicy().hasHeightForWidth())
        self.itemsList_4.setSizePolicy(sizePolicy3)
        self.itemsList_4.setFont(font1)
        self.itemsList_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.itemsList_4.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")
        self.itemsList_4.setEditable(False)
        self.itemsList_4.setModelColumn(0)

        self.gridLayout_15.addWidget(self.itemsList_4, 1, 0, 1, 2)

        self.addItem_4 = QPushButton(self.itemsModification_4)
        self.addItem_4.setObjectName(u"addItem_4")
        sizePolicy4.setHeightForWidth(self.addItem_4.sizePolicy().hasHeightForWidth())
        self.addItem_4.setSizePolicy(sizePolicy4)
        self.addItem_4.setFont(font1)
        self.addItem_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.addItem_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_15.addWidget(self.addItem_4, 2, 0, 1, 2)

        self.tagsImpIt = QPushButton(self.itemsModification_4)
        self.tagsImpIt.setObjectName(u"tagsImpIt")
        self.tagsImpIt.setFont(font1)
        self.tagsImpIt.setCursor(QCursor(Qt.PointingHandCursor))
        self.tagsImpIt.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_15.addWidget(self.tagsImpIt, 5, 0, 1, 2)

        self.addedItems_4 = QTextEdit(self.itemsModification_4)
        self.addedItems_4.setObjectName(u"addedItems_4")
        self.addedItems_4.setFont(font1)
        self.addedItems_4.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedItems_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_15.addWidget(self.addedItems_4, 4, 0, 1, 2)

        self.labelItems_4 = QLabel(self.itemsModification_4)
        self.labelItems_4.setObjectName(u"labelItems_4")
        self.labelItems_4.setFont(font5)

        self.gridLayout_15.addWidget(self.labelItems_4, 0, 0, 1, 2, Qt.AlignHCenter)


        self.horizontalLayout_22.addWidget(self.itemsModification_4)

        self.horizontalSpacer_37 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_37)

        self.tabWidget_5.addTab(self.tab_13, "")

        self.verticalLayout_14.addWidget(self.tabWidget_5)

        self.stackedWidget.addWidget(self.tagsPage)
        self.removeTagsPage = QWidget()
        self.removeTagsPage.setObjectName(u"removeTagsPage")
        self.verticalLayout_9 = QVBoxLayout(self.removeTagsPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.removeTagsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_3)

        self.topOptions_3 = QWidget(self.removeTagsPage)
        self.topOptions_3.setObjectName(u"topOptions_3")
        self.horizontalLayout_26 = QHBoxLayout(self.topOptions_3)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.topOptions_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widgetTag_2 = QWidget(self.frame_6)
        self.widgetTag_2.setObjectName(u"widgetTag_2")
        sizePolicy.setHeightForWidth(self.widgetTag_2.sizePolicy().hasHeightForWidth())
        self.widgetTag_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_28 = QHBoxLayout(self.widgetTag_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_32 = QSpacerItem(195, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_32)

        self.labelTag_2 = QLabel(self.widgetTag_2)
        self.labelTag_2.setObjectName(u"labelTag_2")
        self.labelTag_2.setFont(font1)

        self.horizontalLayout_28.addWidget(self.labelTag_2)

        self.lineEditTag_2 = QLineEdit(self.widgetTag_2)
        self.lineEditTag_2.setObjectName(u"lineEditTag_2")
        self.lineEditTag_2.setMinimumSize(QSize(200, 0))
        self.lineEditTag_2.setMaximumSize(QSize(150, 16777215))
        self.lineEditTag_2.setFont(font1)
        self.lineEditTag_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.horizontalLayout_28.addWidget(self.lineEditTag_2)

        self.horizontalSpacer_42 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_42)


        self.horizontalLayout_27.addWidget(self.widgetTag_2)

        self.widget_4 = QWidget(self.frame_6)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_16 = QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_27.addWidget(self.widget_4)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.labelInfoTag_2 = QLabel(self.frame_5)
        self.labelInfoTag_2.setObjectName(u"labelInfoTag_2")
        self.labelInfoTag_2.setMinimumSize(QSize(100, 0))
        self.labelInfoTag_2.setMaximumSize(QSize(600, 16777215))
        self.labelInfoTag_2.setFont(font1)
        self.labelInfoTag_2.setStyleSheet(u"padding-top: 5px;")
        self.labelInfoTag_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.labelInfoTag_2.setWordWrap(False)

        self.verticalLayout_15.addWidget(self.labelInfoTag_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_26.addWidget(self.frame_5)


        self.verticalLayout_9.addWidget(self.topOptions_3)

        self.tabWidget_6 = QTabWidget(self.removeTagsPage)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        sizePolicy2.setHeightForWidth(self.tabWidget_6.sizePolicy().hasHeightForWidth())
        self.tabWidget_6.setSizePolicy(sizePolicy2)
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_14)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_38 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_38)

        self.sectionModification_5 = QGroupBox(self.tab_14)
        self.sectionModification_5.setObjectName(u"sectionModification_5")
        self.sectionModification_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sectionModification_5.sizePolicy().hasHeightForWidth())
        self.sectionModification_5.setSizePolicy(sizePolicy)
        self.sectionModification_5.setMinimumSize(QSize(350, 0))
        self.sectionModification_5.setMaximumSize(QSize(350, 16777215))
        self.sectionModification_5.setFont(font1)
        self.gridLayout_17 = QGridLayout(self.sectionModification_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setVerticalSpacing(5)
        self.gridLayout_17.setContentsMargins(0, 10, 0, 0)
        self.addedSections_5 = QTextEdit(self.sectionModification_5)
        self.addedSections_5.setObjectName(u"addedSections_5")
        self.addedSections_5.setFont(font1)
        self.addedSections_5.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedSections_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_17.addWidget(self.addedSections_5, 4, 1, 1, 2)

        self.addSection_5 = QPushButton(self.sectionModification_5)
        self.addSection_5.setObjectName(u"addSection_5")
        self.addSection_5.setFont(font1)
        self.addSection_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSection_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_17.addWidget(self.addSection_5, 2, 1, 1, 2)

        self.sectionList_5 = QComboBox(self.sectionModification_5)
        self.sectionList_5.setObjectName(u"sectionList_5")
        self.sectionList_5.setEnabled(True)
        self.sectionList_5.setFont(font1)
        self.sectionList_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.sectionList_5.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_17.addWidget(self.sectionList_5, 1, 1, 1, 2)

        self.labelSection_5 = QLabel(self.sectionModification_5)
        self.labelSection_5.setObjectName(u"labelSection_5")
        self.labelSection_5.setFont(font5)

        self.gridLayout_17.addWidget(self.labelSection_5, 0, 1, 1, 2, Qt.AlignHCenter)

        self.tagsImpSec_2 = QPushButton(self.sectionModification_5)
        self.tagsImpSec_2.setObjectName(u"tagsImpSec_2")
        self.tagsImpSec_2.setFont(font1)
        self.tagsImpSec_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tagsImpSec_2.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_17.addWidget(self.tagsImpSec_2, 5, 1, 1, 2)


        self.horizontalLayout_24.addWidget(self.sectionModification_5)

        self.horizontalSpacer_39 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_39)

        self.tabWidget_6.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.tab_15.setStyleSheet(u"")
        self.horizontalLayout_25 = QHBoxLayout(self.tab_15)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_40 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_40)

        self.itemsModification_5 = QGroupBox(self.tab_15)
        self.itemsModification_5.setObjectName(u"itemsModification_5")
        sizePolicy.setHeightForWidth(self.itemsModification_5.sizePolicy().hasHeightForWidth())
        self.itemsModification_5.setSizePolicy(sizePolicy)
        self.itemsModification_5.setMinimumSize(QSize(350, 0))
        self.itemsModification_5.setMaximumSize(QSize(350, 16777215))
        self.itemsModification_5.setFont(font1)
        self.gridLayout_19 = QGridLayout(self.itemsModification_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(0)
        self.gridLayout_19.setVerticalSpacing(5)
        self.gridLayout_19.setContentsMargins(0, 10, 0, 0)
        self.itemsList_5 = QComboBox(self.itemsModification_5)
        self.itemsList_5.setObjectName(u"itemsList_5")
        sizePolicy3.setHeightForWidth(self.itemsList_5.sizePolicy().hasHeightForWidth())
        self.itemsList_5.setSizePolicy(sizePolicy3)
        self.itemsList_5.setFont(font1)
        self.itemsList_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.itemsList_5.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")
        self.itemsList_5.setEditable(False)
        self.itemsList_5.setModelColumn(0)

        self.gridLayout_19.addWidget(self.itemsList_5, 1, 0, 1, 2)

        self.addItem_5 = QPushButton(self.itemsModification_5)
        self.addItem_5.setObjectName(u"addItem_5")
        sizePolicy4.setHeightForWidth(self.addItem_5.sizePolicy().hasHeightForWidth())
        self.addItem_5.setSizePolicy(sizePolicy4)
        self.addItem_5.setFont(font1)
        self.addItem_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.addItem_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_19.addWidget(self.addItem_5, 2, 0, 1, 2)

        self.tagsImpIt_2 = QPushButton(self.itemsModification_5)
        self.tagsImpIt_2.setObjectName(u"tagsImpIt_2")
        self.tagsImpIt_2.setFont(font1)
        self.tagsImpIt_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tagsImpIt_2.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_19.addWidget(self.tagsImpIt_2, 5, 0, 1, 2)

        self.addedItems_5 = QTextEdit(self.itemsModification_5)
        self.addedItems_5.setObjectName(u"addedItems_5")
        self.addedItems_5.setFont(font1)
        self.addedItems_5.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.addedItems_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_19.addWidget(self.addedItems_5, 4, 0, 1, 2)

        self.labelItems_5 = QLabel(self.itemsModification_5)
        self.labelItems_5.setObjectName(u"labelItems_5")
        self.labelItems_5.setFont(font5)

        self.gridLayout_19.addWidget(self.labelItems_5, 0, 0, 1, 2, Qt.AlignHCenter)


        self.horizontalLayout_25.addWidget(self.itemsModification_5)

        self.horizontalSpacer_41 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_41)

        self.tabWidget_6.addTab(self.tab_15, "")

        self.verticalLayout_9.addWidget(self.tabWidget_6)

        self.stackedWidget.addWidget(self.removeTagsPage)
        self.drinksPage = QWidget()
        self.drinksPage.setObjectName(u"drinksPage")
        self.verticalLayout_5 = QVBoxLayout(self.drinksPage)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 0)
        self.tabWidget_3 = QTabWidget(self.drinksPage)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy2.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy2)
        self.tabWidget_3.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget_3.setStyleSheet(u"")
        self.tabWidget_3.setTabPosition(QTabWidget.North)
        self.tabWidget_3.setTabShape(QTabWidget.Rounded)
        self.tabWidget_3.setElideMode(Qt.ElideLeft)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setMovable(False)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setMinimumSize(QSize(0, 0))
        self.tab_9.setFont(font1)
        self.tab_9.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_24 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.sectionModification_3 = QGroupBox(self.tab_9)
        self.sectionModification_3.setObjectName(u"sectionModification_3")
        sizePolicy.setHeightForWidth(self.sectionModification_3.sizePolicy().hasHeightForWidth())
        self.sectionModification_3.setSizePolicy(sizePolicy)
        self.sectionModification_3.setMinimumSize(QSize(350, 0))
        self.sectionModification_3.setMaximumSize(QSize(350, 16777215))
        self.sectionModification_3.setFont(font1)
        self.gridLayout_22 = QGridLayout(self.sectionModification_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(0)
        self.gridLayout_22.setVerticalSpacing(5)
        self.gridLayout_22.setContentsMargins(0, 10, 0, 0)
        self.addSection_3 = QPushButton(self.sectionModification_3)
        self.addSection_3.setObjectName(u"addSection_3")
        self.addSection_3.setFont(font1)
        self.addSection_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSection_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_22.addWidget(self.addSection_3, 3, 1, 1, 2)

        self.sectionList_3 = QComboBox(self.sectionModification_3)
        self.sectionList_3.setObjectName(u"sectionList_3")
        self.sectionList_3.setEnabled(True)
        self.sectionList_3.setFont(font1)
        self.sectionList_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.sectionList_3.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_22.addWidget(self.sectionList_3, 1, 1, 1, 2)

        self.implementVASM = QPushButton(self.sectionModification_3)
        self.implementVASM.setObjectName(u"implementVASM")
        self.implementVASM.setFont(font1)
        self.implementVASM.setCursor(QCursor(Qt.PointingHandCursor))
        self.implementVASM.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_22.addWidget(self.implementVASM, 6, 1, 1, 2)

        self.addedSections_3 = QTextEdit(self.sectionModification_3)
        self.addedSections_3.setObjectName(u"addedSections_3")
        self.addedSections_3.setFont(font1)
        self.addedSections_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_22.addWidget(self.addedSections_3, 5, 1, 1, 2)

        self.labelSection_3 = QLabel(self.sectionModification_3)
        self.labelSection_3.setObjectName(u"labelSection_3")
        self.labelSection_3.setFont(font5)

        self.gridLayout_22.addWidget(self.labelSection_3, 0, 1, 1, 2, Qt.AlignHCenter)

        self.imAlcoholSM = QCheckBox(self.sectionModification_3)
        self.imAlcoholSM.setObjectName(u"imAlcoholSM")
        self.imAlcoholSM.setFont(font1)
        self.imAlcoholSM.setCheckable(True)

        self.gridLayout_22.addWidget(self.imAlcoholSM, 2, 2, 1, 1)

        self.imVoucherSM = QCheckBox(self.sectionModification_3)
        self.imVoucherSM.setObjectName(u"imVoucherSM")
        self.imVoucherSM.setEnabled(True)
        self.imVoucherSM.setFont(font1)
        self.imVoucherSM.setCheckable(True)
        self.imVoucherSM.setChecked(False)

        self.gridLayout_22.addWidget(self.imVoucherSM, 2, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.sectionModification_3)

        self.horizontalSpacer_25 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_25)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        sizePolicy.setHeightForWidth(self.tab_10.sizePolicy().hasHeightForWidth())
        self.tab_10.setSizePolicy(sizePolicy)
        self.tab_10.setMinimumSize(QSize(0, 0))
        self.tab_10.setFont(font1)
        self.tab_10.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_26 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_26)

        self.itemsModification_3 = QGroupBox(self.tab_10)
        self.itemsModification_3.setObjectName(u"itemsModification_3")
        sizePolicy.setHeightForWidth(self.itemsModification_3.sizePolicy().hasHeightForWidth())
        self.itemsModification_3.setSizePolicy(sizePolicy)
        self.itemsModification_3.setMinimumSize(QSize(350, 0))
        self.itemsModification_3.setMaximumSize(QSize(350, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Verdana"])
        font7.setStyleStrategy(QFont.PreferDefault)
        self.itemsModification_3.setFont(font7)
        self.itemsModification_3.setStyleSheet(u"")
        self.gridLayout_24 = QGridLayout(self.itemsModification_3)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(0)
        self.gridLayout_24.setVerticalSpacing(5)
        self.gridLayout_24.setContentsMargins(0, 10, 0, 0)
        self.imAlcoholIM = QCheckBox(self.itemsModification_3)
        self.imAlcoholIM.setObjectName(u"imAlcoholIM")
        self.imAlcoholIM.setFont(font1)

        self.gridLayout_24.addWidget(self.imAlcoholIM, 2, 1, 1, 1)

        self.imVoucherIM = QCheckBox(self.itemsModification_3)
        self.imVoucherIM.setObjectName(u"imVoucherIM")
        self.imVoucherIM.setFont(font1)
        self.imVoucherIM.setChecked(False)

        self.gridLayout_24.addWidget(self.imVoucherIM, 2, 0, 1, 1)

        self.addedItems_3 = QTextEdit(self.itemsModification_3)
        self.addedItems_3.setObjectName(u"addedItems_3")
        self.addedItems_3.setFont(font1)
        self.addedItems_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_24.addWidget(self.addedItems_3, 5, 0, 1, 2)

        self.implementVAIM = QPushButton(self.itemsModification_3)
        self.implementVAIM.setObjectName(u"implementVAIM")
        self.implementVAIM.setFont(font1)
        self.implementVAIM.setCursor(QCursor(Qt.PointingHandCursor))
        self.implementVAIM.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_24.addWidget(self.implementVAIM, 6, 0, 1, 2)

        self.labelItems_3 = QLabel(self.itemsModification_3)
        self.labelItems_3.setObjectName(u"labelItems_3")
        self.labelItems_3.setFont(font5)

        self.gridLayout_24.addWidget(self.labelItems_3, 0, 0, 1, 2)

        self.itemsList_3 = QComboBox(self.itemsModification_3)
        self.itemsList_3.setObjectName(u"itemsList_3")
        sizePolicy3.setHeightForWidth(self.itemsList_3.sizePolicy().hasHeightForWidth())
        self.itemsList_3.setSizePolicy(sizePolicy3)
        self.itemsList_3.setFont(font1)
        self.itemsList_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.itemsList_3.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")
        self.itemsList_3.setModelColumn(0)

        self.gridLayout_24.addWidget(self.itemsList_3, 1, 0, 1, 2)

        self.addItem_3 = QPushButton(self.itemsModification_3)
        self.addItem_3.setObjectName(u"addItem_3")
        sizePolicy4.setHeightForWidth(self.addItem_3.sizePolicy().hasHeightForWidth())
        self.addItem_3.setSizePolicy(sizePolicy4)
        self.addItem_3.setFont(font1)
        self.addItem_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addItem_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_24.addWidget(self.addItem_3, 3, 0, 1, 2)


        self.horizontalLayout_10.addWidget(self.itemsModification_3)

        self.horizontalSpacer_27 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_27)

        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.tab_12.setMinimumSize(QSize(0, 0))
        self.tab_12.setFont(font1)
        self.tab_12.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 10, 0, 10)
        self.horizontalSpacer_30 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_30)

        self.groupBox_3 = QGroupBox(self.tab_12)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(350, 0))
        self.groupBox_3.setMaximumSize(QSize(350, 16777215))
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"")
        self.gridLayout_28 = QGridLayout(self.groupBox_3)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(0)
        self.gridLayout_28.setVerticalSpacing(5)
        self.gridLayout_28.setContentsMargins(0, 10, 0, 0)
        self.labelSmartSearch_3 = QLabel(self.groupBox_3)
        self.labelSmartSearch_3.setObjectName(u"labelSmartSearch_3")
        self.labelSmartSearch_3.setFont(font1)

        self.gridLayout_28.addWidget(self.labelSmartSearch_3, 0, 0, 1, 2, Qt.AlignHCenter)

        self.implementVASS = QPushButton(self.groupBox_3)
        self.implementVASS.setObjectName(u"implementVASS")
        self.implementVASS.setFont(font1)
        self.implementVASS.setCursor(QCursor(Qt.PointingHandCursor))
        self.implementVASS.setStyleSheet(u"background-color: rgb(39, 0, 116);\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255)\n"
"")

        self.gridLayout_28.addWidget(self.implementVASS, 8, 0, 1, 2)

        self.smartSearchList_3 = QComboBox(self.groupBox_3)
        self.smartSearchList_3.setObjectName(u"smartSearchList_3")
        self.smartSearchList_3.setFont(font1)
        self.smartSearchList_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.smartSearchList_3.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid;\n"
"	padding: 5px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QComboBox QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QComboBox QScrollBar::handle:vertical {\n"
"    background-color: rgb(41, 0, 122); \n"
"    min-height: 50px;\n"
"	border: 1px solid rgb(235, 235, 235)\n"
"}")

        self.gridLayout_28.addWidget(self.smartSearchList_3, 2, 0, 1, 2)

        self.leSmartSearch_3 = QLineEdit(self.groupBox_3)
        self.leSmartSearch_3.setObjectName(u"leSmartSearch_3")
        self.leSmartSearch_3.setFont(font1)
        self.leSmartSearch_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid;\n"
"padding: 5px")

        self.gridLayout_28.addWidget(self.leSmartSearch_3, 1, 0, 1, 2)

        self.addSmartSearch_3 = QPushButton(self.groupBox_3)
        self.addSmartSearch_3.setObjectName(u"addSmartSearch_3")
        self.addSmartSearch_3.setFont(font1)
        self.addSmartSearch_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSmartSearch_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border: 1px solid;\n"
"border-radius: 5px")

        self.gridLayout_28.addWidget(self.addSmartSearch_3, 6, 0, 1, 2)

        self.addedSS_3 = QTextEdit(self.groupBox_3)
        self.addedSS_3.setObjectName(u"addedSS_3")
        self.addedSS_3.setFont(font1)
        self.addedSS_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")

        self.gridLayout_28.addWidget(self.addedSS_3, 7, 0, 1, 2)

        self.imAlcoholSS = QCheckBox(self.groupBox_3)
        self.imAlcoholSS.setObjectName(u"imAlcoholSS")
        self.imAlcoholSS.setFont(font1)

        self.gridLayout_28.addWidget(self.imAlcoholSS, 3, 1, 1, 1)

        self.imVoucherSS = QCheckBox(self.groupBox_3)
        self.imVoucherSS.setObjectName(u"imVoucherSS")
        self.imVoucherSS.setFont(font1)
        self.imVoucherSS.setCheckable(True)
        self.imVoucherSS.setChecked(False)

        self.gridLayout_28.addWidget(self.imVoucherSS, 3, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_3)

        self.horizontalSpacer_31 = QSpacerItem(200, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_31)

        self.tabWidget_3.addTab(self.tab_12, "")

        self.verticalLayout_5.addWidget(self.tabWidget_3)

        self.stackedWidget.addWidget(self.drinksPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.mainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 937, 31))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setEnabled(True)
        font8 = QFont()
        font8.setFamilies([u"verdana"])
        self.menuEdit.setFont(font8)
        self.menuTax_Options = QMenu(self.menuEdit)
        self.menuTax_Options.setObjectName(u"menuTax_Options")
        sizePolicy.setHeightForWidth(self.menuTax_Options.sizePolicy().hasHeightForWidth())
        self.menuTax_Options.setSizePolicy(sizePolicy)
        self.menuTax_Options.setMinimumSize(QSize(0, 0))
        self.menuTax_Options.setSizeIncrement(QSize(0, 0))
        self.menuTax_Options.setFont(font8)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionLoad_Json)
        self.menuFile.addAction(self.actionSave_Json)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.menuTax_Options.menuAction())
        self.menuTax_Options.addAction(self.actionApply_Tax_to_All_Sections)
        self.menuTax_Options.addAction(self.actionRemove_Tax_from_All_Sections)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.priceListSelected.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Json.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Json.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Apply Tax to All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Remove Tax from All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrice_Options.setText(QCoreApplication.translate("MainWindow", u"Price Options", None))
        self.actionCoca_ColaChecker.setText(QCoreApplication.translate("MainWindow", u"Coca-Cola Checker", None))
        self.actionParse_JSON.setText(QCoreApplication.translate("MainWindow", u"Parse JSON ", None))
        self.DRINKSBUTTON.setText(QCoreApplication.translate("MainWindow", u"Voucher and Alcohol", None))
        self.PRICEBUTTON.setText(QCoreApplication.translate("MainWindow", u"Price Modifications", None))
        self.TAXBUTTON.setText(QCoreApplication.translate("MainWindow", u"Tax Modifications", None))
        self.PARSEBUTTON.setText(QCoreApplication.translate("MainWindow", u"Parse JSON", None))
        self.TAXABLEYES.setText(QCoreApplication.translate("MainWindow", u"Taxable Yes", None))
        self.ADDTAGSBUTTON.setText(QCoreApplication.translate("MainWindow", u"Add KDS Tags", None))
        self.REMOVETAGSBUTTON.setText(QCoreApplication.translate("MainWindow", u"Remove KDS Tags", None))
        self.ADDSNOOZETAGSBUTTON.setText(QCoreApplication.translate("MainWindow", u"Add Snooze Tags", None))
        self.GETITEMSNAMEBUTTON.setText(QCoreApplication.translate("MainWindow", u"Snooze Tags .txt", None))
        self.label.setText("")
        self.priceListSelected.setItemText(0, QCoreApplication.translate("MainWindow", u"Increase or Decrease %", None))
        self.priceListSelected.setItemText(1, QCoreApplication.translate("MainWindow", u"Increase or Decrease Fixed Amount", None))
        self.priceListSelected.setItemText(2, QCoreApplication.translate("MainWindow", u"Replace Price", None))
        self.priceListSelected.setItemText(3, QCoreApplication.translate("MainWindow", u"Round Prices", None))

        self.priceListSelected.setPlaceholderText("")
        self.labelInfo2.setText("")
        self.price.setText("")
        self.rounding.setTitle(QCoreApplication.translate("MainWindow", u"Round to...", None))
        self.roundTo10.setText(QCoreApplication.translate("MainWindow", u".10", None))
        self.roundTo5.setText(QCoreApplication.translate("MainWindow", u".5", None))
        self.roundTo99.setText(QCoreApplication.translate("MainWindow", u".99", None))
        self.roundToInt.setText(QCoreApplication.translate("MainWindow", u"closest int", None))
        self.sectionModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection_2.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.priceImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.labelSection_2.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.modOS.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.modMO.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.priceImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.labelItems_2.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem_2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.modMO1.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.modSO1.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.optionSetModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.addOS_2.setText(QCoreApplication.translate("MainWindow", u"Add Option", None))
        self.labelOS_2.setText(QCoreApplication.translate("MainWindow", u"Select the OS to Modify", None))
        self.priceImpOS.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.modMO2.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.modSO2.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.labelSmartSearch_2.setText(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.addSmartSearch_2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.priceImpSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.sectionModification.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.labelSection.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Items Modifications", None))
        self.optionSetModification.setTitle(QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.addOS.setText(QCoreApplication.translate("MainWindow", u"Add Option", None))
        self.labelOS.setText(QCoreApplication.translate("MainWindow", u"Select the OS to Modify", None))
        self.taxImpOS.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.labelSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.taxImpSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.addSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WARNING: Tags need to be written EXACTLY the same as they appear in the POS Back Office", None))
        self.labelTag.setText(QCoreApplication.translate("MainWindow", u"Add Tag:", None))
        self.labelInfoTag.setText("")
        self.sectionModification_4.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.labelSection_4.setText(QCoreApplication.translate("MainWindow", u"Select the Section to Modify", None))
        self.tagsImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Tag", None))
        self.addSection_4.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification_4.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.addItem_4.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tagsImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Tag", None))
        self.labelItems_4.setText(QCoreApplication.translate("MainWindow", u"Select the Item to Modify", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WARNING: Tags need to be written EXACTLY the same as they appear in the POS Back Office", None))
        self.labelTag_2.setText(QCoreApplication.translate("MainWindow", u"Remove Tag:", None))
        self.labelInfoTag_2.setText("")
        self.sectionModification_5.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection_5.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.labelSection_5.setText(QCoreApplication.translate("MainWindow", u"Select the Section to Modify", None))
        self.tagsImpSec_2.setText(QCoreApplication.translate("MainWindow", u"Remove Tag", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification_5.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.addItem_5.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tagsImpIt_2.setText(QCoreApplication.translate("MainWindow", u"Remove Tag", None))
        self.labelItems_5.setText(QCoreApplication.translate("MainWindow", u"Select the Item to Modify", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.sectionModification_3.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection_3.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.implementVASM.setText(QCoreApplication.translate("MainWindow", u"Implement", None))
        self.labelSection_3.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.imAlcoholSM.setText(QCoreApplication.translate("MainWindow", u"Implement Alcohol", None))
        self.imVoucherSM.setText(QCoreApplication.translate("MainWindow", u"Implement Voucher", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification_3.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.imAlcoholIM.setText(QCoreApplication.translate("MainWindow", u"Implement Alcohol", None))
        self.imVoucherIM.setText(QCoreApplication.translate("MainWindow", u"Implement Voucher", None))
        self.implementVAIM.setText(QCoreApplication.translate("MainWindow", u"Implement", None))
        self.labelItems_3.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem_3.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.labelSmartSearch_3.setText(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.implementVASS.setText(QCoreApplication.translate("MainWindow", u"Implement", None))
        self.addSmartSearch_3.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.imAlcoholSS.setText(QCoreApplication.translate("MainWindow", u"Implement Alcohol", None))
        self.imVoucherSS.setText(QCoreApplication.translate("MainWindow", u"Implement Voucher", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTax_Options.setTitle(QCoreApplication.translate("MainWindow", u"Tax Options", None))
    # retranslateUi

