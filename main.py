from PySide6 import QtWidgets
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QShortcut, QKeySequence, QAction

import sys

from db_model import add_project, get_project_num, delete_project
from db_class import Project
from models.chooseProjectModel import ChooseProjectModel
from widget import projectWindow
from widget.createProjectDialog import CreateProjectDialog
from widget.chooseProjectWindow import Ui_MainWindow
from widget.projectWindow import ProjectWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.create_action()
        self.setupUi(self)
        self.model = ChooseProjectModel()
        self.projectList.setModel(self.model)

        self.createButton.clicked.connect(self.create_project)
        self.projectList.doubleClicked.connect(self.open_project)
        self.createButton.setAutoFillBackground(True)
        self.deleteButton.clicked.connect(self.delete_project)

        self.projectList.setCurrentIndex(self.model.index(0,0))

        # Ajout du raccourci de reload QSS
        shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        shortcut.activated.connect(self.reload_stylesheet)

        self.reload_stylesheet()  # Charger au lancement


    def create_project(self):
        dialog = CreateProjectDialog(self)
        result = dialog.exec()  # Open modal dialog

        if result == QtWidgets.QDialog.Accepted:
            data = dialog.get_values()
            add_project(Project(title=data["title"], desc=data["desc"], icon=data["icon"]))
            self.model.layoutChanged.emit()

    def delete_project(self):
        warning: QMessageBox = QMessageBox(self)
        warning.setWindowTitle("Delete this project ?")
        warning.setText("Do you really want to delete this project?")
        warning.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        result = warning.exec()
        if result != QMessageBox.Yes:
            return
        num = get_project_num(self.projectList.currentIndex().data())
        delete_project(Project(num))

    def on_main_closed(self, event):
        del self.mainWindow
        self.show()

    def open_project(self):
        num = get_project_num(self.projectList.currentIndex().data())
        print(f"Choose '{self.projectList.currentIndex().data()}' project n°{num}")
        if not num:
            q = QMessageBox(self)
            q.setText("Project not found")
            q.exec()
            return
        self.mainWindow = ProjectWindow(int(num))
        self.mainWindow.show()
        self.mainWindow.closeEvent = self.on_main_closed
        self.hide()

    def reload_stylesheet(self):
        print("Reloading QSS...")  # Optionnel pour debug
        try:
            with open("style.qss", "r") as f:
                _style = f.read()
                QtWidgets.QApplication.instance().setStyleSheet(_style)
        except Exception as e:
            print("Erreur QSS:", e)

    def event(self, event):
        if event.type() == QEvent.ApplicationPaletteChange:
            self.reload_stylesheet()
        return super().event(event)

    def create_action(self):
        self.act_enter_project = QAction("Open Project", self)
        self.act_enter_project.setStatusTip("Open Project")
        self.act_enter_project.setShortcut(QKeySequence("Return"))
        self.act_enter_project.triggered.connect(self.open_project)

        self.act_add_project = QAction("New Project", self)
        self.act_add_project.setStatusTip("Create a new project")
        self.act_add_project.setShortcut(QKeySequence("Ctrl+N"))
        self.act_add_project.triggered.connect(self.create_project)

        self.act_delete_project = QAction("Delete Project", self)
        self.act_delete_project.setStatusTip("Delete a project")
        self.act_delete_project.setShortcut(QKeySequence("Ctrl+Del"))
        self.act_delete_project.triggered.connect(self.delete_project)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(self.act_enter_project)
        fileMenu.addAction(self.act_add_project)
        fileMenu.addAction(self.act_delete_project)

        edit_menu = menubar.addMenu("&Edit")
        cut_act   = QAction("Cut",   self)
        copy_act  = QAction("Copy",  self)
        paste_act = QAction("Paste", self)
        select_all_act = QAction("Select All", self)

        cut_act.setShortcut(QKeySequence.Cut)
        copy_act.setShortcut(QKeySequence.Copy)
        paste_act.setShortcut(QKeySequence.Paste)
        select_all_act.setShortcut(QKeySequence.SelectAll)

        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(select_all_act)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()
    app.exec()
