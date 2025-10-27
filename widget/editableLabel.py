from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QEvent


class EditableLabel(QWidget):
    def __init__(self, parent=None, text="", on_edit_done=None):
        super().__init__(parent)
        self.on_edit_done = on_edit_done
        self.edit_mode = False
        self._finishing = False

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        self.label.setProperty("class", "EditableLabelViewer")
        self.label.setText(text)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.layout.addWidget(self.label)

        self.editor = QLineEdit(self)
        self.editor.setProperty("class", "EditableLabelEditor")
        self.editor.setText(text)
        self.editor.hide()
        self.layout.addWidget(self.editor)

        self.label.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        self.editor.installEventFilter(self)
        self.editor.editingFinished.connect(self.finish_edit)

    def set_text(self, text):
        self.label.setText(text)
        self.editor.setText(text)

    def mouseDoubleClickEvent(self, event):
        """When double-clicked, replace the label with an editable QLineEdit."""
        if not self.edit_mode:
            self.label.hide()
            self.editor.show()
            self.edit_mode = True
            self._finishing = False

            self.editor.setFocus()
            self.editor.selectAll()

            cursor = self.editor.cursor()
            self.editor.setCursor(cursor)

    def finish_edit(self):
        """Triggered when Enter is pressed or focus is lost."""
        if self._finishing:
            return
        self._finishing = True
        new_text = self.editor.text()
        self.label.setText(new_text)
        self.editor.hide()
        self.editor.clearFocus()
        self.label.show()
        self.edit_mode = False

        if callable(self.on_edit_done):
            self.on_edit_done(new_text)

    def eventFilter(self, watched, event):
        if self.edit_mode:
            if event.type() == QEvent.Type.KeyPress:
                key = event.key()
                if key == Qt.Key_Escape or key == Qt.Key_Enter:
                    self.finish_edit()
                    return True
            elif event.type() == QEvent.Type.FocusOut:
                self.finish_edit()
                return True
        return False


# Demo
if __name__ == "__main__":
    app = QApplication([])

    def on_label_edited(new_text):
        print(f"Edited text: {new_text}")

    window = QWidget()
    layout = QVBoxLayout(window)

    label = EditableLabel("Double-click to edit me", on_edit_done=on_label_edited)
    layout.addWidget(label)
    plainLabel = QLabel("YEP")
    layout.addWidget(plainLabel)

    window.show()
    app.exec()
