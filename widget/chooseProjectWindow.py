# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testuiMpvYRM.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 455)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectLabel = QLabel(self.centralwidget)
        self.projectLabel.setObjectName(u"projectLabel")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.projectLabel.setFont(font)

        self.verticalLayout.addWidget(self.projectLabel)

        self.projectList = QListView(self.centralwidget)
        self.projectList.setObjectName(u"projectList")

        self.verticalLayout.addWidget(self.projectList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout.addWidget(self.createButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.deleteButton.setProperty("class", "delete")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Choose a project", None))
        self.projectLabel.setText(QCoreApplication.translate("MainWindow", u"Projet", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er", None))
    # retranslateUi

