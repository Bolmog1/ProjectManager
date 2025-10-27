# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectmaintdEjQU.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from widget.editableLabel import EditableLabel
from widget.editableMarkdown import EditableMarkdownLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ButtonPanel = QVBoxLayout()
#ifndef Q_OS_MAC
        self.ButtonPanel.setSpacing(-1)
#endif
        self.ButtonPanel.setObjectName(u"ButtonPanel")
        self.ButtonPanel.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.ButtonPanel.setContentsMargins(-1, 0, 0, 0)
        self.overviewButton = QPushButton(self.centralwidget)
        self.overviewButton.setObjectName(u"overviewButton")
        self.overviewButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overviewButton.sizePolicy().hasHeightForWidth())
        self.overviewButton.setSizePolicy(sizePolicy)
        self.overviewButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.ButtonPanel.addWidget(self.overviewButton)

        self.taskButton = QPushButton(self.centralwidget)
        self.taskButton.setObjectName(u"taskButton")
        sizePolicy.setHeightForWidth(self.taskButton.sizePolicy().hasHeightForWidth())
        self.taskButton.setSizePolicy(sizePolicy)

        self.ButtonPanel.addWidget(self.taskButton)

        self.docButton = QPushButton(self.centralwidget)
        self.docButton.setObjectName(u"docButton")
        sizePolicy.setHeightForWidth(self.docButton.sizePolicy().hasHeightForWidth())
        self.docButton.setSizePolicy(sizePolicy)

        self.ButtonPanel.addWidget(self.docButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ButtonPanel.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.ButtonPanel)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.overviewTab = QWidget()
        self.overviewTab.setObjectName(u"overviewTab")
        self.gridLayout = QGridLayout(self.overviewTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.overviewTab)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.overviewTitleLabel = EditableLabel(self.overviewTab)
        self.overviewTitleLabel.setObjectName(u"overviewTitleLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.overviewTitleLabel.sizePolicy().hasHeightForWidth())
        self.overviewTitleLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.overviewTitleLabel)

        self.overviewDescLabel = EditableMarkdownLabel(self.overviewTab)
        self.overviewDescLabel.setObjectName(u"overviewDescLabel")
        sizePolicy1.setHeightForWidth(self.overviewDescLabel.sizePolicy().hasHeightForWidth())
        self.overviewDescLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.overviewDescLabel)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.overviewTab, "")
        self.tasksTab = QWidget()
        self.tasksTab.setObjectName(u"tasksTab")
        self.gridLayout_2 = QGridLayout(self.tasksTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TaskListPanel = QVBoxLayout()
        self.TaskListPanel.setObjectName(u"TaskListPanel")
        self.taskList = QListView(self.tasksTab)
        self.taskList.setObjectName(u"taskList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.taskList.sizePolicy().hasHeightForWidth())
        self.taskList.setSizePolicy(sizePolicy3)

        self.TaskListPanel.addWidget(self.taskList)

        self.taskShowDoneCheckbox = QCheckBox(self.tasksTab)
        self.taskShowDoneCheckbox.setObjectName(u"taskShowDoneCheckbox")

        self.TaskListPanel.addWidget(self.taskShowDoneCheckbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.taskDeleteButton = QPushButton(self.tasksTab)
        self.taskDeleteButton.setObjectName(u"taskDeleteButton")

        self.horizontalLayout_3.addWidget(self.taskDeleteButton)

        self.taskAddButton = QPushButton(self.tasksTab)
        self.taskAddButton.setObjectName(u"taskAddButton")

        self.horizontalLayout_3.addWidget(self.taskAddButton)


        self.TaskListPanel.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.TaskListPanel, 0, 2, 1, 1)

        self.taskLine = QFrame(self.tasksTab)
        self.taskLine.setObjectName(u"taskLine")
        self.taskLine.setFrameShape(QFrame.Shape.VLine)
        self.taskLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.taskLine, 0, 3, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.taskHLine = QFrame(self.tasksTab)
        self.taskHLine.setObjectName(u"taskHLine")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.taskHLine.sizePolicy().hasHeightForWidth())
        self.taskHLine.setSizePolicy(sizePolicy4)
        self.taskHLine.setFrameShape(QFrame.Shape.HLine)
        self.taskHLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.taskHLine, 2, 0, 1, 1)

        self.taskTitleLabel = EditableLabel(self.tasksTab)
        self.taskTitleLabel.setObjectName(u"taskTitleLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.taskTitleLabel.sizePolicy().hasHeightForWidth())
        self.taskTitleLabel.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.taskTitleLabel, 0, 0, 1, 1)

        self.taskDescLabel = EditableMarkdownLabel(self.tasksTab)
        self.taskDescLabel.setObjectName(u"taskDescLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.taskDescLabel.sizePolicy().hasHeightForWidth())
        self.taskDescLabel.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.taskDescLabel, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.taskSetType = QComboBox(self.tasksTab)
        self.taskSetType.addItem("")
        self.taskSetType.addItem("")
        self.taskSetType.addItem("")
        self.taskSetType.setObjectName(u"taskSetType")
        self.taskSetType.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.taskSetType.sizePolicy().hasHeightForWidth())
        self.taskSetType.setSizePolicy(sizePolicy7)

        self.horizontalLayout_6.addWidget(self.taskSetType)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 4, 1, 1)

        self.tabWidget.addTab(self.tasksTab, "")
        self.documentationTab = QWidget()
        self.documentationTab.setObjectName(u"documentationTab")
        self.gridLayout_3 = QGridLayout(self.documentationTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.docListPanel = QVBoxLayout()
        self.docListPanel.setObjectName(u"docListPanel")
        self.docList = QListView(self.documentationTab)
        self.docList.setObjectName(u"docList")
        sizePolicy3.setHeightForWidth(self.docList.sizePolicy().hasHeightForWidth())
        self.docList.setSizePolicy(sizePolicy3)

        self.docListPanel.addWidget(self.docList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.docDeleteButton = QPushButton(self.documentationTab)
        self.docDeleteButton.setObjectName(u"docDeleteButton")

        self.horizontalLayout_4.addWidget(self.docDeleteButton)

        self.docAddButton = QPushButton(self.documentationTab)
        self.docAddButton.setObjectName(u"docAddButton")

        self.horizontalLayout_4.addWidget(self.docAddButton)


        self.docListPanel.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.docListPanel, 0, 0, 1, 1)

        self.docLine = QFrame(self.documentationTab)
        self.docLine.setObjectName(u"docLine")
        self.docLine.setFrameShape(QFrame.Shape.VLine)
        self.docLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.docLine, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.docTitleLabel = EditableLabel(self.documentationTab)
        self.docTitleLabel.setObjectName(u"docTitleLabel")
        sizePolicy5.setHeightForWidth(self.docTitleLabel.sizePolicy().hasHeightForWidth())
        self.docTitleLabel.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.docTitleLabel)

        self.docHLine = QFrame(self.documentationTab)
        self.docHLine.setObjectName(u"docHLine")
        self.docHLine.setFrameShape(QFrame.Shape.HLine)
        self.docHLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.docHLine)

        self.docDescLabel = EditableMarkdownLabel(self.documentationTab)
        self.docDescLabel.setObjectName(u"docDescLabel")
        sizePolicy6.setHeightForWidth(self.docDescLabel.sizePolicy().hasHeightForWidth())
        self.docDescLabel.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.docDescLabel)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.tabWidget.addTab(self.documentationTab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.overviewButton.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.overviewButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menu", None))
        self.taskButton.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.taskButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menu", None))
        self.docButton.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.docButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"double click to add an Icon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overviewTab), QCoreApplication.translate("MainWindow", u"Overview", None))
        self.taskList.setProperty(u"class", QCoreApplication.translate("MainWindow", u"liste", None))
        self.taskShowDoneCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show terminated task", None))
        self.taskDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.taskDeleteButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"delete", None))
        self.taskAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.taskTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"title", None))
        self.taskSetType.setItemText(0, QCoreApplication.translate("MainWindow", u"Done", None))
        self.taskSetType.setItemText(1, QCoreApplication.translate("MainWindow", u"Todo", None))
        self.taskSetType.setItemText(2, QCoreApplication.translate("MainWindow", u"Issue", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tasksTab), QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.docList.setProperty(u"class", QCoreApplication.translate("MainWindow", u"liste", None))
        self.docDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.docDeleteButton.setProperty(u"class", QCoreApplication.translate("MainWindow", u"delete", None))
        self.docAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.docTitleLabel.setProperty(u"class", QCoreApplication.translate("MainWindow", u"title", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documentationTab), QCoreApplication.translate("MainWindow", u"Documentation", None))
    # retranslateUi

