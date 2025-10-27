import os

from PySide6.QtWidgets import QDialog, QFileDialog
from widget.createProject import Ui_CreateProjectDialog


class CreateProjectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CreateProjectDialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_add_image)
        self.icon = None

    def on_add_image(self, event=None):
        path = QFileDialog.getOpenFileName(self, 'Choose an icon for the project', filter="*.png")
        with open(path[0], "rb") as f:
            self.icon = f.read()

    def get_values(self):
        """Return the input values as a dict."""
        return {
            "title": self.ui.lineEdit.text(),
            "desc": self.ui.plainTextEdit.toPlainText(),
            "icon": self.icon,
        }
