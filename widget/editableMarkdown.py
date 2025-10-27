from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextBrowser, QPlainTextEdit, QSplitter
)
from PySide6.QtCore import Qt, QEvent
from widget.editableLabel import EditableLabel

class EditableMarkdownLabel(QWidget):
    def __init__(self, parent=None, markdown_text="", on_edit_done=None, live_preview=False):
        super().__init__(parent)
        self._finishing = False
        self.on_edit_done = on_edit_done
        self.markdown_text = markdown_text
        self.live_preview = live_preview

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Markdown viewer (display mode)
        self.viewer = QTextBrowser()
        self.viewer.setProperty("class", "EditableMarkdownLabelViewer")
        self.viewer.setMarkdown(self.markdown_text)
        self.viewer.setOpenExternalLinks(True)
        self.viewer.viewport().setCursor(Qt.IBeamCursor)
        self.viewer.mouseDoubleClickEvent = self.start_edit
        layout.addWidget(self.viewer)

        # --- Editor setup ---
        if self.live_preview:
            # Splitter: editor + live preview
            self.splitter = QSplitter(Qt.Horizontal)
            self.editor = QPlainTextEdit()
            self.editor.setProperty("class", "EditableMarkdownLabelEditor")
            self.preview = QTextBrowser()
            self.preview.setOpenExternalLinks(True)
            self.splitter.addWidget(self.editor)
            self.splitter.addWidget(self.preview)
            self.splitter.setSizes([2, 1])
            layout.addWidget(self.splitter)
            self.splitter.hide()

            # Live preview connection
            self.editor.textChanged.connect(self.update_preview)
        else:
            self.editor = QPlainTextEdit()
            self.editor.setProperty("class", "EditableMarkdownLabelEditor")
            layout.addWidget(self.editor)
            self.editor.hide()

        # Listen for Escape and focus-out
        self.editor.installEventFilter(self)

    def set_text(self, text):
        self.viewer.setMarkdown(text)
        self.markdown_text = text

    # --- Editing logic ---
    def start_edit(self, event):
        """Switch to edit mode."""
        self.viewer.hide()
        self.editor.setPlainText(self.viewer.toPlainText())
        if self.live_preview:
            self.splitter.show()
            self.editor.setPlainText(self.markdown_text)
            self.preview.setMarkdown(self.markdown_text)
        else:
            self.editor.show()
            self.editor.setPlainText(self.markdown_text)
        self.editor.setFocus()
        self.editor.selectAll()
        self._finishing = True

    def finish_edit(self):
        """Exit edit mode and save content."""
        if not self._finishing:
            return
        self._finishing = False
        new_text = self.editor.toPlainText().strip()
        self.markdown_text = new_text
        self.viewer.setMarkdown(new_text)
        self.clearFocus()
        self.editor.clearFocus()
        if self.live_preview:
            self.splitter.hide()
        else:
            self.editor.hide()
        self.viewer.show()

        if callable(self.on_edit_done):
            self.on_edit_done(new_text)

    def update_preview(self):
        """Live Markdown update while typing."""
        self.preview.setMarkdown(self.editor.toPlainText())

    # --- Event filter for keyboard and focus handling ---
    def eventFilter(self, watched, event):
        if watched == self.editor:
            if event.type() == QEvent.Type.KeyPress:
                if event.key() == Qt.Key_Escape:
                    self.finish_edit()
                    return True
            elif event.type() == QEvent.Type.FocusOut:
                self.finish_edit()
                return True
        return super().eventFilter(watched, event)


# --- Demo ---
if __name__ == "__main__":
    app = QApplication([])

    def on_edit_done(text):
        print("Markdown saved:\n")

    def on_label_done(text):
        print("label saved:\n")

    demo_md = """# Editable Markdown
**Double-click** to edit this text.

- Supports *Markdown*
- Press `Esc` to confirm edits
- Click outside to auto-save
"""

    w = QWidget()
    layout = QVBoxLayout(w)

    title = EditableLabel("no idea", on_edit_done=on_label_done)
    layout.addWidget(title)

    editable = EditableMarkdownLabel(
        demo_md,
        on_edit_done=on_edit_done,
        live_preview=True,  # try False for simpler version
    )
    layout.addWidget(editable)

    w.resize(700, 400)
    w.show()
    app.exec()
