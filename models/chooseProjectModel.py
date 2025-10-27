from db_model import *
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex, QPersistentModelIndex

class ChooseProjectModel(QAbstractListModel):
    def __init__(self, *args, projects=None, **kwargs):
        super().__init__(*args, **kwargs)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int):
        if role == Qt.DisplayRole:
            return get_n_project(index.row()).title
        elif role == Qt.ToolTipRole:
            return get_n_project(index.row()).desc

    def rowCount(self, index):
        return get_project_count()