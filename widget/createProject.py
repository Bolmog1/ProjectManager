# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CréerNJlEIT.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateProjectDialog(object):
    def setupUi(self, CreateProjectDialog):
        if not CreateProjectDialog.objectName():
            CreateProjectDialog.setObjectName(u"CreateProjectDialog")
        CreateProjectDialog.resize(400, 369)
        self.verticalLayout = QVBoxLayout(CreateProjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CreateProjectDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(CreateProjectDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(CreateProjectDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(CreateProjectDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(CreateProjectDialog)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.pushButton)

        self.buttonBox = QDialogButtonBox(CreateProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CreateProjectDialog)
        self.buttonBox.accepted.connect(CreateProjectDialog.accept)
        self.buttonBox.rejected.connect(CreateProjectDialog.reject)

        QMetaObject.connectSlotsByName(CreateProjectDialog)
    # setupUi

    def retranslateUi(self, CreateProjectDialog):
        CreateProjectDialog.setWindowTitle(QCoreApplication.translate("CreateProjectDialog", u"Cr\u00e9er un projet", None))
        self.label.setText(QCoreApplication.translate("CreateProjectDialog", u"Nom", None))
        self.label_2.setText(QCoreApplication.translate("CreateProjectDialog", u"Description", None))
        self.pushButton.setText(QCoreApplication.translate("CreateProjectDialog", u"Ajouter une image", None))
    # retranslateUi

