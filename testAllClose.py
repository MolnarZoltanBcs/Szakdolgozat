import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
#---------
# DEFINE
#---------
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonClose = QtWidgets.QPushButton(self)
        self.pushButtonClose.setText("Close Windows!")
        self.pushButtonClose.clicked.connect(self.on_pushButtonClose_clicked)

        self.pushButtonWindows = QtWidgets.QPushButton(self)
        self.pushButtonWindows.setText("Create Windows!")
        self.pushButtonWindows.clicked.connect(self.on_pushButtonWindows_clicked)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonClose)
        self.layoutVertical.addWidget(self.pushButtonWindows)

    @QtCore.pyqtSlot()
    def on_pushButtonWindows_clicked(self):
        position = self.rect().bottom()

        for dialogNumber in range(3):
            dialog = QtWidgets.QDialog(self)
            dialog.show()
            dialog.setGeometry(
                position,
                position,
                dialog.width(),
                dialog.height()
            )

            position += 10

    @QtCore.pyqtSlot()
    def on_pushButtonClose_clicked(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()

#---------
# MAIN
#---------
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.setGeometry(0, 0, 333, 111)
    main.setWindowFlags(
        main.windowFlags() |
        QtCore.Qt.WindowStaysOnTopHint |
        QtCore.Qt.X11BypassWindowManagerHint
    )
    main.show()

    sys.exit(app.exec_())