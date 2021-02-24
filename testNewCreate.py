import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.setFixedSize(500,500)

        self.window2 = Window2(self)



        self.btn_show_window2 = QPushButton("Open Window 2")
        self.btn_show_window2.clicked.connect(self.show_window2)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_from_window2 = QLineEdit()
        self.text_from_window2.setStyleSheet("color: red;")
        self.text_from_window2.setDisabled(True)

        self.layout.addWidget(self.text_from_window2)
        self.layout.addWidget(self.btn_show_window2)

    def show_window2(self):
        self.window2.show()

    def close(self):
        self.window2.close()
        super(MainWidget, self).close()

    @pyqtSlot(str)
    def update_label(self, txt):
        self.text_from_window2.setText(txt)


class Window2(QWidget):

    def __init__(self, parent):
        super(Window2, self).__init__()
        self.setFixedSize(300,200)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(parent.update_label)
        self.layout.addWidget(self.line_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWidget()
    mw.show()
    sys.exit(app.exec_())