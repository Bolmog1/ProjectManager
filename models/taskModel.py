from db_model import *
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex, QPersistentModelIndex

class TaskModel(QAbstractListModel):
    def __init__(self, *args, projects=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_num = projects
        self.showDoneTask = True

    def set_projects(self, projects):
        self.project_num = projects

    def set_showdonetask(self, showDoneTask: bool):
        self.showDoneTask = showDoneTask

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int):
        if role == Qt.DisplayRole:
            r = get_n_tasks_from(self.project_num, index.row(), self.showDoneTask)
            return r.title if r else False
        elif role == Qt.ToolTipRole:
            r = get_n_tasks_from(self.project_num, index.row(), self.showDoneTask)
            status_desc = ["Done", "Todo", "Issue"]
            return status_desc[r.status] if r else False

    def rowCount(self, index):
        return get_task_count(self.project_num, self.showDoneTask)
