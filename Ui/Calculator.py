# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridlayout = QGridLayout()
        self.gridlayout.setObjectName(u"gridlayout")
        self.component_CrystalDisplay = QLineEdit(self.centralwidget)
        self.component_CrystalDisplay.setObjectName(u"component_CrystalDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.component_CrystalDisplay.sizePolicy().hasHeightForWidth())
        self.component_CrystalDisplay.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(18)
        font.setBold(True)
        self.component_CrystalDisplay.setFont(font)

        self.gridlayout.addWidget(self.component_CrystalDisplay, 0, 0, 1, 1)

        self.keyboardlayout = QGridLayout()
        self.keyboardlayout.setObjectName(u"keyboardlayout")
        self.component_ButtonEight = QPushButton(self.centralwidget)
        self.component_ButtonEight.setObjectName(u"component_ButtonEight")
        sizePolicy.setHeightForWidth(self.component_ButtonEight.sizePolicy().hasHeightForWidth())
        self.component_ButtonEight.setSizePolicy(sizePolicy)
        self.component_ButtonEight.setMinimumSize(QSize(60, 60))
        self.component_ButtonEight.setBaseSize(QSize(0, 0))
        self.component_ButtonEight.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonEight, 1, 1, 1, 1)

        self.component_ButtonFour = QPushButton(self.centralwidget)
        self.component_ButtonFour.setObjectName(u"component_ButtonFour")
        sizePolicy.setHeightForWidth(self.component_ButtonFour.sizePolicy().hasHeightForWidth())
        self.component_ButtonFour.setSizePolicy(sizePolicy)
        self.component_ButtonFour.setMinimumSize(QSize(60, 60))
        self.component_ButtonFour.setBaseSize(QSize(0, 0))
        self.component_ButtonFour.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonFour, 2, 0, 1, 1)

        self.component_ButtonOne = QPushButton(self.centralwidget)
        self.component_ButtonOne.setObjectName(u"component_ButtonOne")
        sizePolicy.setHeightForWidth(self.component_ButtonOne.sizePolicy().hasHeightForWidth())
        self.component_ButtonOne.setSizePolicy(sizePolicy)
        self.component_ButtonOne.setMinimumSize(QSize(60, 60))
        self.component_ButtonOne.setBaseSize(QSize(0, 0))
        self.component_ButtonOne.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonOne, 3, 0, 1, 1)

        self.component_ButtonTwo = QPushButton(self.centralwidget)
        self.component_ButtonTwo.setObjectName(u"component_ButtonTwo")
        sizePolicy.setHeightForWidth(self.component_ButtonTwo.sizePolicy().hasHeightForWidth())
        self.component_ButtonTwo.setSizePolicy(sizePolicy)
        self.component_ButtonTwo.setMinimumSize(QSize(60, 60))
        self.component_ButtonTwo.setBaseSize(QSize(0, 0))
        self.component_ButtonTwo.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonTwo, 3, 1, 1, 1)

        self.component_ButtonThree = QPushButton(self.centralwidget)
        self.component_ButtonThree.setObjectName(u"component_ButtonThree")
        sizePolicy.setHeightForWidth(self.component_ButtonThree.sizePolicy().hasHeightForWidth())
        self.component_ButtonThree.setSizePolicy(sizePolicy)
        self.component_ButtonThree.setMinimumSize(QSize(60, 60))
        self.component_ButtonThree.setBaseSize(QSize(0, 0))
        self.component_ButtonThree.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonThree, 3, 3, 1, 1)

        self.component_ButtonMultiplication = QPushButton(self.centralwidget)
        self.component_ButtonMultiplication.setObjectName(u"component_ButtonMultiplication")
        sizePolicy.setHeightForWidth(self.component_ButtonMultiplication.sizePolicy().hasHeightForWidth())
        self.component_ButtonMultiplication.setSizePolicy(sizePolicy)
        self.component_ButtonMultiplication.setMinimumSize(QSize(60, 60))
        self.component_ButtonMultiplication.setBaseSize(QSize(0, 0))
        self.component_ButtonMultiplication.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonMultiplication, 2, 4, 1, 1)

        self.component_ButtonNine = QPushButton(self.centralwidget)
        self.component_ButtonNine.setObjectName(u"component_ButtonNine")
        sizePolicy.setHeightForWidth(self.component_ButtonNine.sizePolicy().hasHeightForWidth())
        self.component_ButtonNine.setSizePolicy(sizePolicy)
        self.component_ButtonNine.setMinimumSize(QSize(60, 60))
        self.component_ButtonNine.setBaseSize(QSize(0, 0))
        self.component_ButtonNine.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonNine, 1, 3, 1, 1)

        self.component_ButtonSix = QPushButton(self.centralwidget)
        self.component_ButtonSix.setObjectName(u"component_ButtonSix")
        sizePolicy.setHeightForWidth(self.component_ButtonSix.sizePolicy().hasHeightForWidth())
        self.component_ButtonSix.setSizePolicy(sizePolicy)
        self.component_ButtonSix.setMinimumSize(QSize(60, 60))
        self.component_ButtonSix.setBaseSize(QSize(0, 0))
        self.component_ButtonSix.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonSix, 2, 3, 1, 1)

        self.component_ButtonAnser = QPushButton(self.centralwidget)
        self.component_ButtonAnser.setObjectName(u"component_ButtonAnser")
        sizePolicy.setHeightForWidth(self.component_ButtonAnser.sizePolicy().hasHeightForWidth())
        self.component_ButtonAnser.setSizePolicy(sizePolicy)
        self.component_ButtonAnser.setMinimumSize(QSize(60, 60))
        self.component_ButtonAnser.setBaseSize(QSize(0, 0))
        self.component_ButtonAnser.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonAnser, 5, 3, 1, 1)

        self.component_ButtonZero = QPushButton(self.centralwidget)
        self.component_ButtonZero.setObjectName(u"component_ButtonZero")
        sizePolicy.setHeightForWidth(self.component_ButtonZero.sizePolicy().hasHeightForWidth())
        self.component_ButtonZero.setSizePolicy(sizePolicy)
        self.component_ButtonZero.setMinimumSize(QSize(60, 60))
        self.component_ButtonZero.setBaseSize(QSize(0, 0))
        self.component_ButtonZero.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonZero, 5, 0, 1, 1)

        self.component_ButtonFive = QPushButton(self.centralwidget)
        self.component_ButtonFive.setObjectName(u"component_ButtonFive")
        sizePolicy.setHeightForWidth(self.component_ButtonFive.sizePolicy().hasHeightForWidth())
        self.component_ButtonFive.setSizePolicy(sizePolicy)
        self.component_ButtonFive.setMinimumSize(QSize(60, 60))
        self.component_ButtonFive.setBaseSize(QSize(0, 0))
        self.component_ButtonFive.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonFive, 2, 1, 1, 1)

        self.component_ButtonFunction = QPushButton(self.centralwidget)
        self.component_ButtonFunction.setObjectName(u"component_ButtonFunction")
        sizePolicy.setHeightForWidth(self.component_ButtonFunction.sizePolicy().hasHeightForWidth())
        self.component_ButtonFunction.setSizePolicy(sizePolicy)
        self.component_ButtonFunction.setMinimumSize(QSize(60, 60))
        self.component_ButtonFunction.setBaseSize(QSize(0, 0))
        self.component_ButtonFunction.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonFunction, 0, 4, 1, 1)

        self.component_ButtonClearEntry = QPushButton(self.centralwidget)
        self.component_ButtonClearEntry.setObjectName(u"component_ButtonClearEntry")
        sizePolicy.setHeightForWidth(self.component_ButtonClearEntry.sizePolicy().hasHeightForWidth())
        self.component_ButtonClearEntry.setSizePolicy(sizePolicy)
        self.component_ButtonClearEntry.setMinimumSize(QSize(60, 60))
        self.component_ButtonClearEntry.setBaseSize(QSize(0, 0))
        self.component_ButtonClearEntry.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonClearEntry, 0, 1, 1, 1)

        self.component_ButtonAddition = QPushButton(self.centralwidget)
        self.component_ButtonAddition.setObjectName(u"component_ButtonAddition")
        sizePolicy.setHeightForWidth(self.component_ButtonAddition.sizePolicy().hasHeightForWidth())
        self.component_ButtonAddition.setSizePolicy(sizePolicy)
        self.component_ButtonAddition.setMinimumSize(QSize(60, 60))
        self.component_ButtonAddition.setBaseSize(QSize(0, 0))
        self.component_ButtonAddition.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonAddition, 5, 4, 1, 1)

        self.component_ButtonDot = QPushButton(self.centralwidget)
        self.component_ButtonDot.setObjectName(u"component_ButtonDot")
        sizePolicy.setHeightForWidth(self.component_ButtonDot.sizePolicy().hasHeightForWidth())
        self.component_ButtonDot.setSizePolicy(sizePolicy)
        self.component_ButtonDot.setMinimumSize(QSize(60, 60))
        self.component_ButtonDot.setBaseSize(QSize(0, 0))
        self.component_ButtonDot.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonDot, 5, 1, 1, 1)

        self.component_ButtonSubtraction = QPushButton(self.centralwidget)
        self.component_ButtonSubtraction.setObjectName(u"component_ButtonSubtraction")
        sizePolicy.setHeightForWidth(self.component_ButtonSubtraction.sizePolicy().hasHeightForWidth())
        self.component_ButtonSubtraction.setSizePolicy(sizePolicy)
        self.component_ButtonSubtraction.setMinimumSize(QSize(60, 60))
        self.component_ButtonSubtraction.setBaseSize(QSize(0, 0))
        self.component_ButtonSubtraction.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonSubtraction, 3, 4, 1, 1)

        self.component_ButtonDivision = QPushButton(self.centralwidget)
        self.component_ButtonDivision.setObjectName(u"component_ButtonDivision")
        sizePolicy.setHeightForWidth(self.component_ButtonDivision.sizePolicy().hasHeightForWidth())
        self.component_ButtonDivision.setSizePolicy(sizePolicy)
        self.component_ButtonDivision.setMinimumSize(QSize(60, 60))
        self.component_ButtonDivision.setBaseSize(QSize(0, 0))
        self.component_ButtonDivision.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonDivision, 1, 4, 1, 1)

        self.component_ButtonSeven = QPushButton(self.centralwidget)
        self.component_ButtonSeven.setObjectName(u"component_ButtonSeven")
        sizePolicy.setHeightForWidth(self.component_ButtonSeven.sizePolicy().hasHeightForWidth())
        self.component_ButtonSeven.setSizePolicy(sizePolicy)
        self.component_ButtonSeven.setMinimumSize(QSize(60, 60))
        self.component_ButtonSeven.setBaseSize(QSize(0, 0))
        self.component_ButtonSeven.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonSeven, 1, 0, 1, 1)

        self.component_ButtonClearMemory = QPushButton(self.centralwidget)
        self.component_ButtonClearMemory.setObjectName(u"component_ButtonClearMemory")
        sizePolicy.setHeightForWidth(self.component_ButtonClearMemory.sizePolicy().hasHeightForWidth())
        self.component_ButtonClearMemory.setSizePolicy(sizePolicy)
        self.component_ButtonClearMemory.setMinimumSize(QSize(60, 60))
        self.component_ButtonClearMemory.setBaseSize(QSize(0, 0))
        self.component_ButtonClearMemory.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonClearMemory, 0, 0, 1, 1)

        self.component_ButtonAllClear = QPushButton(self.centralwidget)
        self.component_ButtonAllClear.setObjectName(u"component_ButtonAllClear")
        sizePolicy.setHeightForWidth(self.component_ButtonAllClear.sizePolicy().hasHeightForWidth())
        self.component_ButtonAllClear.setSizePolicy(sizePolicy)
        self.component_ButtonAllClear.setMinimumSize(QSize(60, 60))
        self.component_ButtonAllClear.setBaseSize(QSize(0, 0))
        self.component_ButtonAllClear.setAutoRepeatInterval(100)

        self.keyboardlayout.addWidget(self.component_ButtonAllClear, 0, 3, 1, 1)


        self.gridlayout.addLayout(self.keyboardlayout, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridlayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.component_ButtonEight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.component_ButtonFour.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.component_ButtonOne.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.component_ButtonTwo.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.component_ButtonThree.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.component_ButtonMultiplication.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.component_ButtonNine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.component_ButtonSix.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.component_ButtonAnser.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.component_ButtonZero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.component_ButtonFive.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.component_ButtonFunction.setText(QCoreApplication.translate("MainWindow", u"Fn", None))
        self.component_ButtonClearEntry.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.component_ButtonAddition.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.component_ButtonDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.component_ButtonSubtraction.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.component_ButtonDivision.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.component_ButtonSeven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.component_ButtonClearMemory.setText(QCoreApplication.translate("MainWindow", u"CM", None))
        self.component_ButtonAllClear.setText(QCoreApplication.translate("MainWindow", u"AC", None))
    # retranslateUi

