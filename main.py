import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *


class sentence(QMainWindow):
    def __init__(self):
        super(sentence, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(15)
        self.setCentralWidget(self.editor)
        self.font_size_box = QSpinBox()
        self.showMaximized()
        self.setWindowTitle('Sentence')
        self.create_tool_bar()
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = QMenu('File', self)
        menu_bar.addMenu(file_menu)

        save_as_pdf = QAction('Save As PDF', self)
        save_as_pdf.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_as_pdf)

        edit_menu = QMenu('Edit', self)
        menu_bar.addMenu(edit_menu)

        self.setMenuBar(menu_bar)

    def create_tool_bar(self):
        tool_bar = QToolBar()

        undo_action = QAction(QIcon('Sentence/Icons/undo.png'),'Undo',self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action = QAction(QIcon('Sentence/Icons/redo.png'),'Redo',self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()

        cut_action = QAction(QIcon('Sentence/Icons/cut.png'),'Cut',self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        copy_action = QAction(QIcon('Sentence/Icons/copy.png'),'Copy',self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)
 
        paste_action = QAction(QIcon('Sentence/Icons/paste.png'),'Paste',self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()

        self.font_size_box.setValue(15)
        self.font_size_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_size_box)

        self.addToolBar(tool_bar)

    def set_font_size(self):
        value = self.font_size_box.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)


app = QApplication(sys.argv)
#app.setStyle('gtk2')
window = sentence()
window.show()
sys.exit(app.exec_())