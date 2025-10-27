from db_model import *
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex, QPersistentModelIndex

class DocModel(QAbstractListModel):
    def __init__(self, *args, projects=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_num = projects

    def set_projects(self, projects):
        self.project_num = projects

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int):
        if role == Qt.DisplayRole:
            r = get_n_docs_from(self.project_num, index.row())
            return r.title if r else False
        elif role == Qt.ToolTipRole:
            r = get_n_docs_from(self.project_num, index.row())
            return r.content if r else False

    def rowCount(self, index):
        return get_doc_count(self.project_num)
