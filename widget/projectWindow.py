from PySide6 import QtCore
from PySide6.QtGui import QPixmap, QAction, QKeySequence
from PySide6.QtWidgets import QMainWindow, QLabel, QTabBar, QTabWidget, QSizePolicy, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from db_model import get_project_by_num, update_project, get_n_tasks_from, update_task, create_task, \
    get_index_of_last_task, delete_task, get_n_docs_from, update_doc, add_doc, delete_doc
from db_class import Project
from models.taskModel import TaskModel
from models.docModel import DocModel
from widget.project import Ui_MainWindow


class ProjectWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, project_num: int):
        super().__init__()

        self.taskModel = None
        self.docModel = None
        self.taskDisplayed = None
        self.docDisplayed = None
        self.project:Project|None = None
        self.project_num = project_num
        self.create_action()

        self.setupUi(self)
        self.tabWidget.currentIndex()
        self.tabWidget.tabBar().hide()

        # Setup button of tabs
        self.overviewButton.clicked.connect(lambda: self.tab_button_click(0))
        self.taskButton.clicked.connect(lambda: self.tab_button_click(1))
        self.docButton.clicked.connect(lambda: self.tab_button_click(2))
        self.tabWidget.setCurrentIndex(0)
        self.refresh_tabs_button()

        self.open_project()

    def tab_button_click(self, event):
        # print("tab clicked : ", event)
        self.tabWidget.setCurrentIndex(event)
        self.refresh_tabs_button()

    def open_project(self):
        self.project = get_project_by_num(self.project_num)
        if not self.project:
            return
        print(f"open project n°{self.project_num} : {self.project.title}")
        self.setWindowTitle(self.project.title)
        # Overview tab
        self.overviewTitleLabel.set_text(self.project.title)
        self.overviewTitleLabel.on_edit_done = self.edit_project_title
        self.overviewDescLabel.set_text(self.project.desc)
        self.overviewDescLabel.on_edit_done = self.edit_project_desc
        self.label.mouseDoubleClickEvent = self.edit_project_icon
        # Task tab
        self.taskModel = TaskModel()
        self.taskModel.set_projects(self.project.num)
        self.taskList.setModel(self.taskModel)
        self.taskList.selectionChanged = self.change_task
        self.taskTitleLabel.on_edit_done = self.edit_task_title
        self.taskDescLabel.on_edit_done = self.edit_task_content
        self.taskAddButton.clicked.connect(self.add_task)
        self.taskDeleteButton.clicked.connect(self.delete_task)
        self.taskShowDoneCheckbox.clicked.connect(self.change_task_filter)
        self.taskSetType.currentTextChanged.connect(self.change_task_status)

        self.taskList.setCurrentIndex(self.taskModel.index(0,0))
        # Doc tab
        self.docModel = DocModel()
        self.docModel.set_projects(self.project.num)
        self.docList.setModel(self.docModel)
        self.docList.selectionChanged = self.change_doc
        self.docTitleLabel.on_edit_done = self.edit_doc_title
        self.docDescLabel.on_edit_done = self.edit_doc_content
        self.docAddButton.clicked.connect(self.add_doc)
        self.docDeleteButton.clicked.connect(self.delete_doc)

        # By default, select the first element
        self.docList.setCurrentIndex(self.docModel.index(0,0))

        # Set the icon
        if self.project.icon:
            icon = QPixmap()
            icon.loadFromData(self.project.icon)
            self.label.setPixmap(icon)
            self.label.setScaledContents(1)
            policy = QSizePolicy()
            policy.setHeightForWidth(True)
            policy.setHorizontalPolicy(QSizePolicy.Policy.Fixed)
            self.label.setSizePolicy(policy)
            self.label.setMaximumSize(QtCore.QSize(200, 200))

    def refresh_tabs_button(self):
        all_tabs = [
            self.overviewButton,
            self.taskButton,
            self.docButton,
        ]
        current_tab = self.tabWidget.currentIndex()
        for i, tab in enumerate(all_tabs):
            tab.setProperty("class", "main" if i == current_tab else "")
            tab.style().unpolish(tab)
            tab.style().polish(tab)
            tab.update()

    def edit_project_title(self, title: str):
        self.project.title = title
        self.setWindowTitle(self.project.title)
        update_project(self.project)

    def edit_project_desc(self, desc: str):
        self.project.desc = desc
        update_project(self.project)

    def edit_project_icon(self, event=None):
        path = QFileDialog.getOpenFileName(self, 'Choose an icon for the project', filter="*.png")
        with open(path[0], "rb") as f:
            self.project.icon = f.read()
            update_project(self.project)
        icon = QPixmap()
        icon.loadFromData(self.project.icon)
        self.label.setPixmap(icon)
        self.label.setScaledContents(1)
        policy = QSizePolicy()
        policy.setHeightForWidth(True)
        policy.setHorizontalPolicy(QSizePolicy.Policy.Fixed)
        self.label.setSizePolicy(policy)
        self.label.setMaximumSize(QtCore.QSize(200, 200))

    def change_task(self, new=None, prev=None):
        index = self.taskList.currentIndex()
        task = get_n_tasks_from(self.project_num, index.row(), self.taskModel.showDoneTask)
        self.taskDisplayed = task.num
        self.taskTitleLabel.set_text(task.title)
        self.taskDescLabel.set_text(task.content)
        self.taskSetType.setCurrentIndex(task.status)

    def edit_task_title(self, title: str):
        update_task(self.taskDisplayed, title=title)
        self.taskModel.layoutChanged.emit()

    def edit_task_content(self, content: str):
        update_task(self.taskDisplayed, content=content)
        self.taskModel.layoutChanged.emit()

    def add_task(self):
        create_task(self.project_num)
        self.taskModel.layoutChanged.emit()

    def delete_task(self):
        warning:QMessageBox = QMessageBox(self)#.warning(self, "Delete task ?", "Do you really want to delete this task?", QMessageBox.Cancel | QMessageBox.Yes, QMessageBox.Yes)
        warning.setWindowTitle("Delete task ?")
        warning.setText("Do you really want to delete this task?")
        warning.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        result = warning.exec()
        if result != QMessageBox.Yes:
            return

        index = self.taskList.currentIndex()
        task = get_n_tasks_from(self.project_num, index.row(), self.taskModel.showDoneTask)
        delete_task(task.num)
        self.taskModel.layoutChanged.emit()

    def change_task_filter(self):
        self.taskModel.set_showdonetask(not self.taskShowDoneCheckbox.isChecked())
        self.taskModel.layoutChanged.emit()

    def change_task_status(self):
        choose = self.taskSetType.currentText()
        status:int = 0
        if choose=='Done':
            status = 0
        elif choose=='Issue':
            status = 2
        elif choose=='Todo':
            status = 1
        else:
            print('Unknown task type')
            return
        update_task(self.taskDisplayed, status=status)
        self.taskModel.layoutChanged.emit()


    def change_doc(self, prev=None, new=None):
        index = self.docList.currentIndex()
        doc = get_n_docs_from(self.project_num, index.row())
        self.docDisplayed = doc.num
        self.docTitleLabel.set_text(doc.title)
        self.docDescLabel.set_text(doc.content)

    def edit_doc_title(self, title: str):
        update_doc(self.docDisplayed, title=title)
        self.docModel.layoutChanged.emit()

    def edit_doc_content(self, content: str):
        update_doc(self.docDisplayed, content=content)
        self.docModel.layoutChanged.emit()

    def delete_doc(self):
        warning: QMessageBox = QMessageBox(
            self)  # .warning(self, "Delete task ?", "Do you really want to delete this task?", QMessageBox.Cancel | QMessageBox.Yes, QMessageBox.Yes)
        warning.setWindowTitle("Delete documentation ?")
        warning.setText("Do you really want to delete this document?")
        warning.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        result = warning.exec()
        if result != QMessageBox.Yes:
            return

        index = self.docList.currentIndex()
        task = get_n_docs_from(self.project_num, index.row())
        delete_doc(task.num)
        self.docModel.layoutChanged.emit()

    def add_doc(self):
        add_doc(self.project_num)
        self.docModel.layoutChanged.emit()

    def create_action(self):
        self.act_overview_tab = QAction("Open Overview Tab", self)
        self.act_overview_tab.setStatusTip("Open the overview tab")
        self.act_overview_tab.setShortcut(QKeySequence("ctrl+&"))
        self.act_overview_tab.triggered.connect(lambda: self.tab_button_click(0))

        self.act_task_tab = QAction("Open Tasks Tab", self)
        self.act_task_tab.setStatusTip("Open the tasks tab")
        self.act_task_tab.setShortcut(QKeySequence("ctrl+é"))
        self.act_task_tab.triggered.connect(lambda: self.tab_button_click(1))

        self.act_documentation_tab = QAction("Open Documentation Tab", self)
        self.act_documentation_tab.setStatusTip("Open the documentation tab")
        self.act_documentation_tab.setShortcut(QKeySequence("ctrl+\""))
        self.act_documentation_tab.triggered.connect(lambda: self.tab_button_click(2))

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        menu = menubar.addMenu("Tab")
        menu.addAction(self.act_overview_tab)
        menu.addAction(self.act_task_tab)
        menu.addAction(self.act_documentation_tab)

        edit_menu = menubar.addMenu("&Edit")
        cut_act = QAction("Cut", self)
        copy_act = QAction("Copy", self)
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
